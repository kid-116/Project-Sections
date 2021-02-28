from django import forms
from .models import Bracket, JoinRequest


class BracketCreationForm(forms.ModelForm):
    class Meta:
        model = Bracket
        fields = [
            'name',
            'graduation_year',
        ]