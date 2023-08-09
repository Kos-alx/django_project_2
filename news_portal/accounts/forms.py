from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        viewers = Group.objects.get(name="viewers")
        user.groups.add(viewers)
        return user