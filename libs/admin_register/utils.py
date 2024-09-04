# coding=utf-8
from __future__ import print_function

from types import MethodType

from django.apps import apps
from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from django.db import models
from django.db.models import Field, NOT_PROVIDED
from django.db.models.fields.reverse_related import ForeignObjectRel
from django.urls import reverse
from django.utils.safestring import mark_safe

model__str__ = models.Model.__str__

# Restricted fields
list_display_restricted_fields = (
    models.OneToOneField,
    models.TextField,
    models.ManyToManyField,
)

search_restricted_fields = (
    models.AutoField,
    models.ForeignKey,
    models.ManyToManyField,
)

list_filter_fields = (
    models.BooleanField,
    models.NullBooleanField,
)


def get_concrete_field_names(model):
    for field in model._meta.get_fields():
        if not issubclass(type(field), ForeignObjectRel):
            yield field.name


def get_related_attribute(relation):
    """
        Follow related fields define as strings: "foreignkey__attribute"
    """
    attrs = relation.split('__')

    def w(obj):
        related_attr = obj
        for attr in attrs:
            related_attr = getattr(related_attr, attr)
        return str(related_attr)

    w.short_description = ' '.join(attr.title() for attr in attrs)
    w.admin_order_field = relation
    return w


def inline_factory(inline_type, model, extra=0, read_only=True, **kwargs):
    kwargs['model'] = model
    kwargs['extra'] = extra
    if read_only:
        kwargs['readonly_fields'] = kwargs.get('fields', tuple(get_concrete_field_names(model)))
        kwargs['has_add_permission'] = kwargs['has_delete_permission'] = lambda *a, **k: False
    return type('%s_inline' % model.__name__, (inline_type,), kwargs)


def stacked_inline(model, **kwargs):
    return inline_factory(admin.StackedInline, model, **kwargs)


def tabular_inline(model, **kwargs):
    return inline_factory(admin.TabularInline, model, **kwargs)


def get_form(self, *args, **kwargs):
    form = super(self.__class__, self).get_form(*args, **kwargs)

    def __init__(_self, *_args, **_kwargs):
        super(_self.__class__, _self).__init__(*_args, **_kwargs)
        blank_model_fields = set(
            field.name for field in self.model._meta.get_fields()
            if getattr(field, 'default', NOT_PROVIDED) != NOT_PROVIDED
            or getattr(field, 'null', None))
        for name, field in _self.fields.items():
            if name in blank_model_fields:
                field.required = False

    form.__init__ = __init__
    return form


class AdminRegister(object):
    def __init__(self, model):
        self.model = model
        self.admin_model = None

    def __call__(self, model_admin):
        """
            Decorator of admin.ModelAdmin

            Add many features to ``model_admin`` and register
            it to the admin site
        """

        model_admin.get_form = get_form
        self.admin_model = model_admin
        self.set_inlines()

        # Set all fields read only
        if getattr(self.admin_model, 'all_fields_read_only', False):
            read_only_fields = self.get_all_fields()
            self.admin_model.readonly_fields = read_only_fields

        if not self.admin_model.search_fields:
            self.set_search_fields()

        if self.admin_model.list_display == ('__str__',):
            self.set_list_display_from_meta()
            self.set_list_display_extra_fields()

        self.set_list_display_relations()
        self.set_links_to_fk()
        self.set_list_filter()
        self.set_many_to_many_filter_horizontal()
        self.set_raw_id_fields()

        admin.site.register(self.model, model_admin)
        return model_admin

    def set_raw_id_fields(self):
        if not self.admin_model.raw_id_fields:
            self.admin_model.raw_id_fields = tuple(
                field.name for field in self.model._meta.fields
                if issubclass(field.__class__, models.ForeignKey)
            )

    def set_many_to_many_filter_horizontal(self):
        if not self.admin_model.filter_horizontal:
            for field in self.model._meta.get_fields():
                if issubclass(field.__class__, models.ManyToManyField):
                    self.admin_model.filter_horizontal = self.admin_model.filter_horizontal + (field.name, )

    def set_list_filter(self):
        list_filter = self.admin_model.list_filter = list(self.admin_model.list_filter)
        for field in self.model._meta.fields:
            if (isinstance(field, list_filter_fields) or field.choices) and field.name not in list_filter:
                list_filter.append(field.name)

    def set_links_to_fk(self):
        def generate_admin_link_function(field_name):
            def object_admin_link(self, obj):
                _field = getattr(obj, field_name)
                if _field:
                    label = _field.__str__() if _field.__str__ is not model__str__ else _field.pk
                    url = reverse('admin:%s_%s_change' % (_field._meta.app_label, _field._meta.model_name),
                                  args=[_field.pk], )
                    return mark_safe(u'<a href="%s">%s</a>' % (url, label))
                return ''

            object_admin_link.__name__ = field_name
            object_admin_link.admin_order_field = field_name
            return object_admin_link

        def generate_admin_link_function_content_type(field_name):
            def object_admin_link(self, obj):
                _field = getattr(obj, field_name)
                if _field:
                    label = str(_field)
                    model = _field.model_class()
                    app_label = model._meta.app_label
                    model_name = model._meta.model_name
                    url = reverse(f'admin:{app_label}_{model_name}_changelist')
                    return mark_safe(u'<a href="%s">%s</a>' % (url, label))
                return ''

            object_admin_link.__name__ = field_name
            object_admin_link.admin_order_field = field_name
            return object_admin_link

        ContentType = apps.get_model('contenttypes', 'ContentType')

        from django.contrib.contenttypes.fields import GenericForeignKey

        illegal_select_related = []

        for field in self.get_fk_fields():
            if hasattr(field, 'remote_field') and field.remote_field and field.remote_field.model is ContentType:
                pass
            elif isinstance(field, GenericForeignKey):
                illegal_select_related.append(field.name)
                method = MethodType(generate_admin_link_function_content_type(field.ct_field), self.admin_model)
                setattr(self.admin_model, '%s' % '_' + field.ct_field, method)
            else:
                method = MethodType(generate_admin_link_function(field.name), self.admin_model)
                setattr(self.admin_model, '%s' % '_' + field.name, method)
            if field.name in self.admin_model.list_display:
                self.admin_model.list_display = list(self.admin_model.list_display)
                for (i, item) in enumerate(self.admin_model.list_display):
                    if item == field.name:
                        self.admin_model.list_display[i] = '_' + field.name
            if not self.admin_model.list_select_related:
                self.admin_model.list_select_related = []
            if field.name not in self.admin_model.list_select_related and field.name not in illegal_select_related:
                self.admin_model.list_select_related.append(field.name)

    def get_fk_fields(self):
        from django.contrib.contenttypes.fields import GenericForeignKey
        return [f for f in self.model._meta.get_fields() if isinstance(f, models.ForeignKey) or isinstance(f, GenericForeignKey)]

    def get_meta_fields(self, restricted_fields):
        """
            Get meta fields of self.model and exclude restricted_fields
        """
        return [f.name for f in self.model._meta.fields if not isinstance(f, restricted_fields)]

    def set_list_display_from_meta(self):
        exclude_fields = getattr(self.admin_model, 'list_display_exclude', [])
        self.admin_model.list_display = []

        for field in self.get_meta_fields(list_display_restricted_fields):
            if field not in exclude_fields:
                self.admin_model.list_display.append(field)

    def set_list_display_extra_fields(self):
        extra_fields = getattr(self.admin_model, 'list_display_add', [])

        for field in extra_fields:
            self.admin_model.list_display.append(field)

    def set_list_display_relations(self):
        """
            Transform the strings representing related fields into
            callables that the admin class can use
        """

        new_list_display = []

        for attr in self.admin_model.list_display:
            try:
                if '__' in attr and not attr.startswith('__'):
                    attr = get_related_attribute(attr)
            except TypeError:
                pass

            new_list_display.append(attr)

        self.admin_model.list_display = new_list_display

    def set_search_fields(self):
        self.admin_model.search_fields = self.get_meta_fields(search_restricted_fields)

    def set_inlines(self):
        """
            Make inline classes with models from 'stacked_inlines' and 'tabular_inlines'
        """

        inlines = getattr(self.admin_model, 'inlines', [])
        extra = getattr(self.admin_model, 'extra', 0)
        inlines = list(inlines)  # bug fix

        stacked_inlines = getattr(self.admin_model, 'stacked_inlines', ())
        inlines += (stacked_inline(model, extra=extra) for model in stacked_inlines)

        tabular_inlines = getattr(self.admin_model, 'tabular_inlines', ())
        inlines += (tabular_inline(model, extra=extra) for model in tabular_inlines)

        self.admin_model.inlines = inlines

    def get_all_fields(self):
        """
        Get all fields of the model,
            except related fields
        :return: list of all fields
        """
        fields = []
        for field in self.model._meta.get_fields():
            if issubclass(field.__class__, Field):
                fields.append(field.name)
        return fields


def admin_factory(model, unregister=False, **kwargs):
    """
        Re-register the model and create a
        new admin class to reset for each test
    """
    if unregister:
        try:
            admin.site.unregister(model)
        except NotRegistered:
            pass
    new_admin = type('%sAdmin' % model.__name__, (admin.ModelAdmin,), kwargs)
    return AdminRegister(model)(new_admin)
