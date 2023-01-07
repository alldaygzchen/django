from django.urls import path

from . import views

urlpatterns = [
     path("", views.ReviewView.as_view()), #CreateView
     path("thank-you", views.ThankYouView.as_view()),
     path("reviews", views.ReviewsListView.as_view()), #ListView
     path("reviews/<int:pk>", views.SingleReviewView.as_view()), #DetailView
     path("delete_reviews/<int:pk>", views.DeleteReviewView.as_view(),name='delete'), #DeleteView
     path("update_reviews/<int:pk>", views.UpdateReviewView.as_view(),name='update') #UpdateView
]