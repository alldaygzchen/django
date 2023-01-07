from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render

from reviews.models import Review
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,FormView,DeleteView,UpdateView

# Create your views here.


class ReviewView(CreateView):
    model = Review
    #fields = "__all__"
    form_class = ReviewForm #customize label....
    template_name = "reviews/review.html"
    success_url = "/thank-you"


class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context


class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"


class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review

class DeleteReviewView(DeleteView):
    template_name = "reviews/review_delete.html"
    model = Review
    success_url = '/reviews'

class UpdateReviewView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review_update.html"
    success_url = "/reviews"

