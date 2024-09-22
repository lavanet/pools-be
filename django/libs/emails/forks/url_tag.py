from django.template import Library, TemplateSyntaxError
from django.template.base import kwarg_re, Node
from django.utils.html import conditional_escape

from ..utils import prepend_domain

register = Library()


def do_url(parser, token):
    """
    FORKED FROM DJANGO
    Returns an absolute URL matching given view with its parameters.

    This is a way to define links that aren't tied to a particular URL
    configuration::

        {% url "path.to.some_view" arg1 arg2 %}

        or

        {% url "path.to.some_view" name1=value1 name2=value2 %}

    The first argument is a path to a view. It can be an absolute Python path
    or just ``app_name.view_name`` without the project name if the view is
    located inside the project.

    Other arguments are space-separated values that will be filled in place of
    positional and keyword arguments in the URL. Don't mix positional and
    keyword arguments.

    All arguments for the URL should be present.

    For example if you have a view ``app_name.client`` taking client's id and
    the corresponding line in a URLconf looks like this::

        ('^client/(\d+)/$', 'app_name.client')

    and this app's URLconf is included into the project's URLconf under some
    path::

        ('^clients/', include('project_name.app_name.urls'))

    then in a template you can create a link for a certain client like this::

        {% url "app_name.client" client.id %}

    The URL will look like ``/clients/client/123/``.

    The first argument can also be a named URL instead of the Python path to
    the view callable. For example if the URLconf entry looks like this::

        url('^client/(\d+)/$', name='client-detail-view')

    then in the template you can use::

        {% url "client-detail-view" client.id %}

    There is even another possible value type for the first argument. It can be
    the name of a template variable that will be evaluated to obtain the view
    name or the URL name, e.g.::

        {% with view_path="app_name.client" %}
        {% url view_path client.id %}
        {% endwith %}

        or,

        {% with url_name="client-detail-view" %}
        {% url url_name client.id %}
        {% endwith %}

    """
    bits = token.split_contents()
    if len(bits) < 2:
        raise TemplateSyntaxError("'%s' takes at least one argument"
                                  " (path to a view)" % bits[0])
    viewname = parser.compile_filter(bits[1])
    args = []
    kwargs = {}
    asvar = None
    bits = bits[2:]
    if len(bits) >= 2 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]

    if len(bits):
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise TemplateSyntaxError("Malformed arguments to url tag")
            name, value = match.groups()
            if name:
                kwargs[name] = parser.compile_filter(value)
            else:
                args.append(parser.compile_filter(value))

    return URLNode(viewname, args, kwargs, asvar)


class URLNode(Node):
    def __init__(self, view_name, args, kwargs, asvar):
        self.view_name = view_name
        self.args = args
        self.kwargs = kwargs
        self.asvar = asvar

    def render(self, context):
        from django.urls import NoReverseMatch, reverse

        args = [arg.resolve(context) for arg in self.args]
        kwargs = {k: v.resolve(context) for k, v in self.kwargs.items()}
        view_name = self.view_name.resolve(context)
        try:
            current_app = context.request.current_app
        except AttributeError:
            try:
                current_app = context.request.resolver_match.namespace
            except AttributeError:
                current_app = None
        # Try to look up the URL. If it fails, raise NoReverseMatch unless the
        # {% url ... as var %} construct is used, in which case return nothing.
        url = ''
        try:
            url = reverse(view_name, args=args, kwargs=kwargs, current_app=current_app)
        except NoReverseMatch:
            if self.asvar is None:
                raise

        url = prepend_domain(url)
        if self.asvar:
            context[self.asvar] = url
            return ''
        else:
            if context.autoescape:
                url = conditional_escape(url)
            return url
