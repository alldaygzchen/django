1. Client (cookie with session id)<=> Server (session data + identifier)

2. Make sure django.contrib.sessions.middleware.SessionMiddleware is added

3. SESSION_COOKIE_AGE = 120 (2 minutes default)

4. single_review.html and urls.py

            <form action="/reviews/favorite" method="POST">
                {% csrf_token %}
                <input type="hidden" name="review_id" value="{{ review.id }}">
                <button>Favorite</button>
            </form>

5. views.py

        class AddFavoriteView(View):
            def post(self, request):
                review_id = request.POST["review_id"]
                request.session["favorite_review"] = review_id
                return HttpResponseRedirect("/reviews/" + review_id)

6. views.py

    check request session data  == loaded review  
    do not use request.session["favorite_review"] because will fail


        class SingleReviewView(DetailView):
            template_name = "reviews/single_review.html"
            model = Review

            def get_context_data(self, **kwargs):
                context = super().get_context_data(**kwargs)
                loaded_review = self.object
                request = self.request
                favorite_id = request.session.get("favorite_review") 
                context["is_favorite"] = favorite_id == str(loaded_review.id)
                return context

    single_review.html

    (is_favorite comes from SingleReviewView(DetailView))

        {% if is_favorite %}
            <p>This is my favorite!</p>
        {% else %}
            <form action="/reviews/favorite" method="POST">
            {% csrf_token %}
            <input type="hidden" name="review_id" value="{{ review.id }}">
            <button>Favorite</button>
            </form>
        {% endif %}

7. Additionals  
### raise 404
If a requested record does not exist then the generic class-based detail view will raise an Http404 exception for you automatically