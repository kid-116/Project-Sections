from django import forms
from . import models


class NewOrganisationForm(forms.ModelForm):
    class Meta:
        model = models.Organisation
        fields = [
            'name',
        ]


class JoinRequestForm(forms.ModelForm):
    class Meta:
        model = models.JoinRequest
        fields = [
            'org',
        ]