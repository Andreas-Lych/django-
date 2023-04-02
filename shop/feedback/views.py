from django.shortcuts import render, redirect

from feedback.forms import AddFeedbackForm
from feedback.models import Feedback


def indexf(request):
    notes = Feedback.objects.all()
    if request.method == "POST":
        form = AddFeedbackForm(request.POST)
        if form.is_valid():
            Feedback.objects.create(
                author=request.user,
                title=form.cleaned_data["title"],
                text=form.cleaned_data["text"]
            )
            return redirect("indexf")
    else:
        form = AddFeedbackForm()
    return render(request, "feedback.html", {"note": notes, "form": form})