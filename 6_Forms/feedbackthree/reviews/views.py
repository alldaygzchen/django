from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm

# Create your views here.


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

    #update example
    #  if request.method == 'POST':
    #     existing_data = Review.object.get(pk=1)
    #     form = ReviewForm(request.POST,instance = existing_data)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")   

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")