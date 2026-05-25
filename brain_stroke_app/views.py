from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect  # 🌟 Added this secure import
from .forms import PredictionForm
from .ml_model import make_prediction


FEATURES = [
    "gender", "age", "hypertension", "heart_disease", "martial_status",
    "family_history", "work_type", "residence_type", "avg_glucose_level",
    "bmi", "smoking_status", "alcohol_consumption", "diabetes_status", "bp_systolic",
    "bp_diastolic", "cholesterol", "wbc_count", "rbc_count"
]

# Create your views here.
@login_required(only=["GET", "POST"])
@csrf_protect  # 🌟 Added this decorator right here to fix python:S3752
def predict(request):
    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            model_algo = request.GET.get("model")

            feature_list = []
            for feature in FEATURES:
                val = cd.get(feature)
                feature_list.append(val)

            pred_details = make_prediction(feature_list, algo=model_algo)
            print(pred_details["classification_breakdown"])
            return render(request, "app/predict.html", {"pred_details": pred_details, "form": form, "model": model_algo})
    else:
        form = PredictionForm()

    context = {"form": form}

    return render(request, "app/predict.html", context=context)
