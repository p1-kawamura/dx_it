from django import forms
from .models import Customer

class Right_form(forms.ModelForm):
    tantou=forms.ChoiceField(
        choices=[("",""),("井上","井上"),("古川","古川"),("眞下","眞下")],
        label="担当者",
        widget=forms.Select(attrs={"class":"form-select"}),
        required=False
    )
    dm_day=forms.CharField(label="DM", widget=forms.DateInput(attrs={"type": "date"}),required=False)
    tel_day=forms.CharField(label="TEL", widget=forms.DateInput(attrs={"type": "date"}),required=False)
    gaisho_day=forms.CharField(label="外商", widget=forms.DateInput(attrs={"type": "date"}),required=False)

    bikou=forms.CharField(label="備考",widget=forms.Textarea(attrs={"class":"form-control","rows":"3"}),required=False)

    class Meta:
        model=Customer
        fields=["tantou","dm_day","tel_day","gaisho_day","bikou"]


