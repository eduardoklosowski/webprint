from django import forms

from .models import Print, PrintImg


class PrintForm(forms.ModelForm):
    class Meta:
        model = Print
        fields = ['name', 'expires_in', 'desc']


PrintImgFormSet = forms.inlineformset_factory(
    Print, PrintImg,
    fields=['img'],
    can_order=False,
    can_delete=False,
    extra=5,
    min_num=1,
    max_num=6,
    validate_min=True,
    validate_max=True,
)
