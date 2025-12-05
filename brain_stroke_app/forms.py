from django import forms
from django.forms.widgets import NumberInput

GENDER_CHOICE = [
    ("1", "Male"),
    ("2", "Female"),
]

MARTIAL_STATUS_CHOICE = [
    ("1", "Married"),
    ("0", "Single")
]

WORK_TYPE_CHOICE = [
    ("3", "Private"),
    ("2", "self-employed"),
    ("1", "Government"),
    ("4", "unemployed"),
    ("5", "Others")
]

RESIDENCE_CHOICE = [
    ("1", "Urban"),
    ("2", "Rural")
]

HYPERTENSION_CHOICE = [
    ("0", "no"),
    ("1", "yes")
]

HEART_DISEASE_CHOICE = [
    ("0", "no"),
    ("1", "yes")
]

SMOKING_STATUS_CHOICE = [
    ("1.0", "Never Smoked"),
    ("2.0", "Formerly Smoked"),
    ("3.0", "Currently Smokes")
]

FAMILY_HISTORY_CHOICE = [
    ("1", "no"),
    ("2", "yes")
]

DIABETES_CHOICE = [
    ("0", "no"),
    ("1", "yes")
]

class RangeInput(NumberInput):
    input_type = "range"

class PredictionForm(forms.Form):
    # Patient Profile
    age = forms.IntegerField(min_value=10, max_value=100)
    gender = forms.ChoiceField(choices=GENDER_CHOICE, widget=forms.RadioSelect)
    martial_status = forms.ChoiceField(choices=MARTIAL_STATUS_CHOICE, widget=forms.RadioSelect)
    work_type = forms.ChoiceField(choices=WORK_TYPE_CHOICE, widget=forms.Select(attrs={"class": ""}))
    residence_type = forms.ChoiceField(choices=RESIDENCE_CHOICE, widget=forms.RadioSelect)

    # vitals and clinical data
    bmi = forms.FloatField()
    avg_glucose_level = forms.FloatField()
    cholesterol = forms.IntegerField()
    bp_systolic = forms.IntegerField()
    bp_diastolic = forms.IntegerField()
    wbc_count = forms.IntegerField()
    rbc_count = forms.FloatField()

    # History and lifestyle
    hypertension = forms.ChoiceField(choices=HYPERTENSION_CHOICE, widget=forms.RadioSelect)
    heart_disease = forms.ChoiceField(choices=HEART_DISEASE_CHOICE, widget=forms.RadioSelect)
    family_history = forms.ChoiceField(choices=FAMILY_HISTORY_CHOICE, widget=forms.RadioSelect)
    diabetes_status = forms.ChoiceField(choices=DIABETES_CHOICE, widget=forms.RadioSelect)
    smoking_status = forms.ChoiceField(choices=SMOKING_STATUS_CHOICE, widget=forms.Select)
    alcohol_consumption = forms.IntegerField(widget=RangeInput(attrs={"min": 0, "max": 8, "step": 1}))

