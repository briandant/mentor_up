# -*- coding: utf-8 -*-
import floppyforms as forms

from .models import User, Skill, LOCATIONS
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Fieldset, Div
from django.core.urlresolvers import reverse

#from django_select2 import AutoModelSelect2MultipleField
SKILL_OPTIONS = tuple((skill.id, skill.name) for skill in Skill.objects.all())


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
                Field('skill_to_learn'),
                Field('skills_to_teach')
            )
        )

    class Meta:
        # Set this form to use the User model.
        model = User

        fields = ("first_name", "last_name", "short_bio", "location", "skills_to_learn", "skills_to_teach")


class MemberSearchForm(forms.Form):
    skills_to_search = forms.MultipleChoiceField(choices=SKILL_OPTIONS, required=False)
    locations_to_search = forms.MultipleChoiceField(choices=LOCATIONS, required=False)

    def __init__(self, *args, **kwargs):
        super(MemberSearchForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.form_id = 'id_member_search_form'
        self.helper.form_tag = True
        self.helper.form_class = 'form-inline'
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.form_method = 'get'
        self.helper.form_action = reverse('users:search')

        self.helper.layout = Layout(
            Div('skills_to_search', css_class="col-sm-3"),
            Div('locations_to_search', css_class="col-sm-3"),
            Div(Submit('submit', 'Search Mentor UP Members &raquo;', css_class="btn-default btn-block"), css_class="col-sm-3"),
        )

        self.fields['skills_to_search'].label = "Choose skills to search"
        self.fields['locations_to_search'].label = "Choose a city"
