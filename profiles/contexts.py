from profiles.models import Profile


def active_user(request):
    print("CONTEXT PROCESSOR WORKING")
    if request.user.is_authenticated:
        print("AUTHENTICATED")
        current_profile = Profile.objects.get(user=request.user)
        request.session['user_paid'] = current_profile.paid
    else:
        print("NOT AUTHENTICATED")
        current_profile = None
        request.session['user_paid'] = False
    current_profile = None
    context = {
        'current_profile': current_profile
    }

    print(f"Context: {context}")

    return context
