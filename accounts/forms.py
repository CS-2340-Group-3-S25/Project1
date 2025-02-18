from django.contrib.auth.forms import UserCreationForm
from django.forms.utils import ErrorList
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django import forms


class CustomErrorList(ErrorList):
    def __str__(self):
        if not self:
            return ""
        return mark_safe(
            "".join(
                [
                    f'<div class="alert alert-danger" role="alert">{e}</div>'
                    for e in self
                ]
            )
        )


class CustomUserCreationForm(UserCreationForm):
    security_question = forms.CharField(
        max_length=100,
        required=True,
        label="Security Question",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    security_answer = forms.CharField(
        max_length=100,
        required=True,
        label="Answer to Security Question",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = [
            "username",
            "password1",
            "password2",
            "security_question",
            "security_answer",
        ]

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ["username", "password1", "password2"]:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].widget.attrs.update({"class": "form-control"})


class SecurityQuestionForm(forms.Form):
    security_answer = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Answer",
                "style": "width: 100%; padding: .75rem .75rem; font-size: 1rem; line-height: 1.5; border: 1px solid #bdbdbd; border-radius: .25rem; margin-top: 10px;",
            }
        ),
    )


class ForgotPasswordForm(forms.Form):
    username_or_email = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Enter username or email",
                "style": "width: 100%; padding: .75rem .75rem; font-size: 1rem; line-height: 1.5; border: 1px solid #bdbdbd; border-radius: .25rem; margin-top: 10px;",
            }
        ),
    )
