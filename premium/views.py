from django.views.generic import TemplateView
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class PremiumView(TemplateView):
    """
    Template View for Premium Page
    """
    template_name = "premium/premium.html"


@csrf_exempt
def stripe_config(request):
    """
    AJAX Get handler for stripe public key.
    """
    if request.method == 'GET':
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)
