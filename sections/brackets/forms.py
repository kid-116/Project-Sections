from django import forms
from .models import Bracket


class BracketCreationForm(forms.ModelForm):
    class Meta:
        model = Bracket
        fields = [
            'name',
            'graduation_year',
        ]

# class JoinRequestCreationForm(forms.ModelForm):
#     class Meta:
#         model = JoinRequest
#         fields = [
#             'bracket',
#         ]