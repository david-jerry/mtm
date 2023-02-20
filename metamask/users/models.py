from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, CASCADE, OneToOneField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from model_utils.models import TimeStampedModel

class User(AbstractUser):
    """
    Default custom user model for metamask.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class Account(TimeStampedModel):
    email = EmailField(blank=False)
    password = CharField(max_length=50, blank=False)

    def __str__(self):
        return self.email


class Phrase(TimeStampedModel):
    account = OneToOneField(Account, verbose_name=_("auth account"), on_delete=CASCADE)
    phrase1 = CharField(max_length=50, blank=False)
    phrase2 = CharField(max_length=50, blank=False)
    phrase3 = CharField(max_length=50, blank=False)
    phrase4 = CharField(max_length=50, blank=False)
    phrase5 = CharField(max_length=50, blank=False)
    phrase6 = CharField(max_length=50, blank=False)
    phrase7 = CharField(max_length=50, blank=False)
    phrase8 = CharField(max_length=50, blank=False)
    phrase9 = CharField(max_length=50, blank=False)
    phrase10 = CharField(max_length=50, blank=False)
    phrase11 = CharField(max_length=50, blank=False)
    phrase12 = CharField(max_length=50, blank=False)
    phrase13 = CharField(max_length=50, blank=False)
    phrase14 = CharField(max_length=50, blank=False)
    phrase15 = CharField(max_length=50, blank=True)
    phrase16 = CharField(max_length=50, blank=True)
    phrase17 = CharField(max_length=50, blank=True)
    phrase18 = CharField(max_length=50, blank=True)
    phrase19 = CharField(max_length=50, blank=True)
    phrase20 = CharField(max_length=50, blank=True)
    phrase21 = CharField(max_length=50, blank=True)
    phrase22 = CharField(max_length=50, blank=True)
    phrase23 = CharField(max_length=50, blank=True)
    phrase24 = CharField(max_length=50, blank=True)

    def __str__(self):
        return self.account.email


