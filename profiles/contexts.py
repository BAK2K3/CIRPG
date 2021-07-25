from profiles.models import Profile


# def active_user(request):
#     if request.user.is_authenticated:
#         current_profile = Profile.objects.get(user=request.user)
#         request.session['user_paid'] = current_profile.paid
#     else:
#         current_profile = None
#         request.session['user_paid'] = False

#     context = {
#         'current_profile': current_profile
#     }

#     return context
