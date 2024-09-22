from functools import update_wrapper

from django.contrib import admin
from django.http import Http404
from django.shortcuts import redirect
from django.urls import path, reverse


class MethodModelAdmin(admin.ModelAdmin):
    change_form_template = 'admin_register/method_change_form.html'
    change_list_template = 'admin_register/method_change_list.html'

    list_options = ()
    form_options = ()

    def get_urls(self):
        def wrap(view):
            def wrapper(*args, **kwargs):
                return self.admin_site.admin_view(view)(*args, **kwargs)

            wrapper.model_admin = self
            return update_wrapper(wrapper, view)

        app_info = self._app_info()
        urlpatterns = []
        for name, func in self._get_list_options():
            urlpatterns.append(path(f'{name}/', wrap(func), name=f'{app_info}_{name}'))
        for name, func in self._get_form_options():
            urlpatterns.append(path(f'<path:object_id>/{name}/', wrap(func), name=f'{app_info}_{name}'))
        return urlpatterns + super().get_urls()

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['list_options'] = tuple(
            self._get_option_attributes(name, func)
            for name, func in self._get_list_options())
        return super().changelist_view(request, extra_context=extra_context)

    def render_change_form(self, request, context, obj=None, **kwargs):
        if obj:
            context['form_options'] = tuple(
                self._get_option_attributes(name, func, obj)
                for name, func in self._get_form_options())
        return super().render_change_form(request, context, obj=obj, **kwargs)

    def _app_info(self):
        return f'{self.model._meta.app_label}_{self.model._meta.model_name}'

    def _get_list_options(self):
        return self._get_options(self.list_options)

    def _get_form_options(self):
        return self._get_options(self.form_options)

    def _get_options(self, options):
        for func_name in options:
            yield func_name, getattr(self, func_name)

    def _get_option_attributes(self, name, func, obj=None):
        url_kwargs = None if obj is None else {'object_id': obj.pk}
        return {
            'class': getattr(func, 'html_class', None),
            'label': getattr(func, 'html_label', func.__name__),
            'url': reverse(f'admin:{self._app_info()}_{name}', kwargs=url_kwargs),
        }

    def get_object_or_404(self, request, object_id):
        obj = self.get_object(request, object_id)
        if obj is None:
            raise Http404()
        return obj

    def redirect_change(self, object_id):
        return redirect(f'admin:{self._app_info()}_change', object_id)
