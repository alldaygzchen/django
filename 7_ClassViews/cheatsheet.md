# Setups

1.  create a folder with main app name
2.  copy and paste github  


# ClassView 
        
        from django.views import View
        from django.views.generic.base import TemplateView
        from django.views.generic import ListView, DetailView
        from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView


## TemplateView
overide get_context_data and repsonse all get method


        class ThankYouView(TemplateView):
            template_name = "reviews/thank_you.html"

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                context["message"] = "This works!"
                return context            

        class ReviewsListView(TemplateView):
            template_name = "reviews/review_list.html"

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                reviews = Review.objects.all()
                context["reviews"] = reviews
                return context

        class ReviewsListView(TemplateView):
            template_name = "reviews/review_list.html"

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                reviews = Review.objects.all()
                context["reviews"] = reviews
                return context        



## ListView

        class ReviewsListView(ListView):
            template_name = "reviews/review_list.html"
            model = Review # tell db where to fetch
            context_object_name = "reviews" # the name of the data when expose to database



## DetailView

        class SingleReviewView(DetailView):
            template_name = "reviews/single_review.html"
            model = Review # takes it lowercase and expose to database # tell db where to fetch

        requirements: path("reviews/<int:pk>", views.SingleReviewView.as_view()) #need to use pk or slug

## View

        class ReviewView(View):
            def get(self, request):
                form = ReviewForm()

                return render(request, "reviews/review.html", {
                    "form": form
                })

            def post(self, request):
                form = ReviewForm(request.POST)

                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("/thank-you")

                return render(request, "reviews/review.html", {
                    "form": form
                })




## FormView

        class ReviewView(FormView):
            form_class = ReviewForm
            template_name = "reviews/review.html"
            success_url = "/thank-you"

            def form_valid(self, form):
                form.save()
                return super().form_valid(form)




## CreateView
    Render a form,validate a form ,show error results 

    class ReviewView(CreateView):
        model = Review
        #fields = "__all__"
        form_class = ReviewForm #add if customize label....
        template_name = "reviews/review.html"
        success_url = "/thank-you"