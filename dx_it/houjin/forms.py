from django import forms
from .models import Customer,Image


class Right_form(forms.ModelForm):

    tantou=forms.ChoiceField(
        choices=[(0,""),(1,"井上"),(2,"古川"),(3,"眞下"),(4,"夏八木"),(5,"武藤"),(6,"小山田"),(7,"粂川")],
        label="担当者",
        widget=forms.Select(attrs={"class":"form-select"}),
        required=False
    )
    dm_day=forms.CharField(label="DM", widget=forms.DateInput(attrs={"type": "date","class":"form-control form-control-sm"}),required=False)
    tel_day=forms.CharField(label="TEL", widget=forms.DateInput(attrs={"type": "date","class":"form-control form-control-sm"}),required=False)
    gaisho_day=forms.CharField(label="外商", widget=forms.DateInput(attrs={"type": "date","class":"form-control form-control-sm"}),required=False)
    nouhin_day=forms.CharField(label="納品", widget=forms.DateInput(attrs={"type": "date","class":"form-control form-control-sm"}),required=False)

    kanshoku=forms.ChoiceField(
        choices=[(0,""),(5,"5"),(4,"4"),(3,"3"),(2,"2"),(1,"1")],
        label="感触",
        widget=forms.Select(attrs={"class":"form-select form-select-sm","id":"kanshoku"}),
        required=False
    )

    dm_check=forms.BooleanField(
        label="DM配信",
        widget=forms.CheckboxInput(attrs={"type": "checkbox","class":"form-check-input","id":"dm_send"}),
        required=False,
        )

    bikou=forms.CharField(label="備考",widget=forms.Textarea(attrs={"class":"form-control","rows":"3"}),required=False)
    bikou2=forms.CharField(label="備考2",widget=forms.Textarea(attrs={"class":"form-control","rows":"3"}),required=False)
    bikou3=forms.CharField(label="備考3",widget=forms.Textarea(attrs={"class":"form-control","rows":"3"}),required=False)

    class Meta:
        model=Customer
        fields=["tantou","dm_day","tel_day","gaisho_day","nouhin_day","kanshoku","dm_check","bikou","bikou2","bikou3"]


class Image_form(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title','image']