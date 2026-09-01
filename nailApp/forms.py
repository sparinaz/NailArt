from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name','mobile','text']
        error_messages = {
    'name': {
        'required': 'لطفاً نام خود را وارد کنید.',
    },
    'text': {
        'required': 'لطفاً متن دیدگاه خود را وارد کنید.',
    },
}

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')

        # موبایل اختیاری است
        if not mobile:
            return mobile

        # باید دقیقاً 11 کاراکتر باشد
        if len(mobile) != 11:
            raise forms.ValidationError(
                "شماره موبایل باید ۱۱ رقم باشد."
            )

        # باید فقط عدد باشد و با 09 شروع شود
        if not mobile.isdigit() or not mobile.startswith("09"):
            raise forms.ValidationError(
                "موبایل وارد شده نامعتبر است."
            )

        return mobile