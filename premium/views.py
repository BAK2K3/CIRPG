from django.views.generic import TemplateView
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from profiles.models import Profile


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


@csrf_exempt
def create_checkout_session(request):
    """
    AJAX Checkout Session handler.
    """
    if request.method == 'GET':
        if request.user.is_authenticated:
            # Obtain active profile and ensure they are not already premium
            current_profile = Profile.objects.get(user=request.user)
            if not current_profile.paid:
                # Create Stripe Checkout Session
                # Return the session JSON if successful
                domain_url = settings.DOMAIN_URL
                stripe.api_key = settings.STRIPE_SECRET_KEY
                try:
                    checkout_session = stripe.checkout.Session.create(
                        success_url=domain_url + 'premium/success/',
                        cancel_url=domain_url + 'premium/abort/',
                        payment_method_types=['card'],
                        mode='payment',
                        line_items=[
                            {
                                'price': settings.STRIPE_PRICE_ID,
                                'quantity': 1,
                            }
                        ],
                        customer_email=request.user.email
                    )
                    return JsonResponse({'sessionId': checkout_session['id']})
                except Exception as e:
                    return JsonResponse({'error': str(e)})
            else:
                return JsonResponse({'error': "Profile is already premium."})
        else:
            return JsonResponse({'error': "User is not logged in."})


class SuccessView(TemplateView):
    """
    Template View for Successful Payment
    """
    template_name = "premium/success.html"


class AbortView(TemplateView):
    """
    Template View for Aborted/Unsuccessful payment
    """
    template_name = "premium/abort.html"
