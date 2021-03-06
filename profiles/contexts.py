"""
Profiles App - Contexts
----------------

Context implementation for Profiles App.
"""

from profiles.models import Profile


def active_user(request):
    """
    Context Processor for passing
    Profile contexts to templates.
    """
    if request.user.is_authenticated:
        current_profile = Profile.objects.get(user=request.user)
        request.session['user_paid'] = current_profile.paid
    else:
        current_profile = None
        request.session['user_paid'] = False
    context = {
        'current_profile': current_profile
    }
    return context
