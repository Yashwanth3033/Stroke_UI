from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect  # 1. Add this import

@login_required
@csrf_protect  # 2. Add this decorator to protect the view explicitly
def dashboard(request):
    context = {}

    return render(request, "account/dashboard.html", context=context)