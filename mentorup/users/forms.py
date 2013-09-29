# -*- coding: utf-8 -*-
from django import forms
import floppyforms as forms

from .models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML, Submit, ButtonHolder, Fieldset


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_id = 'id_user_form'
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Fieldset(
                '',
                Field('first_name'),
                Field('last_name'),
                Field('short_bio'),
                Field('location'),
                Field('skill_to_learn', multiple=True),
                Field('skills_to_teach', multiple=True)
            )
        )

    class Meta:
        # Set this form to use the User model.
        model = User

        # Constrain the UserForm to just these fields.
        fields = ("first_name", "last_name", "short_bio", "location", "skills_to_learn", "skills_to_teach")
