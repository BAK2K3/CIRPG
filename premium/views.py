from django.views.generic import TemplateView


class PremiumView(TemplateView):
    """
    Template View for Premium Page
    """
    template_name = "premium/premium.html"
