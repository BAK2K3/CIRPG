from django.views.generic import TemplateView


class IndexView(TemplateView):
    """ A view to return index page """
    template_name = 'home/index.html'


class HelpView(TemplateView):
    """A view to return Help page """
    template_name = 'home/help.html'
