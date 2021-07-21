from django.views.generic import TemplateView
from django.conf import settings
from django.http.response import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import stripe
from profiles.models import Profile
from django.shortcuts import redirect


class PremiumView(TemplateView):
    """
    Template View for Premium Page
    """
    template_name = "premium/premium.html"

    # Checks to see whether previous checkout token exists
    # Removes the Checkout bool from session if so
    def get(self, *args, **kwargs):
        if self.request.session.get('CHECKOUT'):
            self.request.session.pop('CHECKOUT')
        return super().get(*args, **kwargs)

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
                    # Places checkout bool in session cookie for verification
                    request.session['CHECKOUT'] = True
                    return JsonResponse({'sessionId': checkout_session['id']})
                except Exception as e:
                    return JsonResponse({'error': str(e)})
            else:
                return JsonResponse({'error': "Profile is already premium."})
        else:
            return JsonResponse({'error': "User is not logged in."})


@csrf_exempt
def stripe_webhook(request):
    """
    Webhook handling for stripe payment.
    Returns 200 - on successful payment.
    Returns 400 - on unsuccessful payment.

    All unsuccessful events remove the checkout from
    the session.
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_WH_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        if request.session.get('CHECKOUT'):
            request.session.pop('CHECKOUT')
        # Invalid payload
        return HttpResponse(e, status=400)
    except stripe.error.SignatureVerificationError as e:
        if request.session.get('CHECKOUT'):
            request.session.pop('CHECKOUT')
        # Invalid signature
        return HttpResponse(e, status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")
        # TODO: Send JSON to browser
        # TODO: Activate Premium
        # TODO: Send Email
    else:
        if request.session.get('CHECKOUT'):
            request.session.pop('CHECKOUT')
        print(event)
    return HttpResponse(status=200)


class SuccessView(TemplateView):
    """
    Template View for Successful Payment
    """
    template_name = "premium/success.html"

    # Checks to see whether checkout is in progress
    def get(self, *args, **kwargs):
        if self.request.META.get('HTTP_SEC_FETCH_SITE') == "cross-site":
            if self.request.session.get('CHECKOUT'):
                self.request.session.pop('CHECKOUT')
                return super().get(*args, **kwargs)
        else:
            return redirect('premium')


class AbortView(TemplateView):
    """
    Template View for Aborted/Unsuccessful payment
    """
    template_name = "premium/abort.html"
