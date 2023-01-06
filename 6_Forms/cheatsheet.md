# Basic web concepts

1. label [for =] matches input [id =]
2. name attribute is for request params
3. csrf token: give client fishing email => custom badpage send the changed info to the original page url
   prevent non-generated page from the original web server 
4. <form action="a" method="POST"> # https://localhost:8000/a



        <form action="/" method="POST">
            {% csrf_token %}
            {% if has_error %}
            <p>This form is invalid - please enter a valid username!</p>
            {% endif %}
            <label for="username">Your name</label>
            <input id="username" name="username" type="text">
            <button type="submit">Send</button>
        </form>

4. Great example of view:

        def review(request):
        if request.method == 'POST':
            entered_username = request.POST['username']

            if entered_username == "" and len(entered_username) >= 100:
            return render(request, "reviews/review.html", {
                "has_error": True
            })
            print(entered_username)
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "has_error": False
        })


# Django Form concepts
[forms.py]

1. Validations in server, thus the page will be refreshed
2. Validations error will also be output
3.

        #default
        <form action="/" method="POST">
            {% csrf_token %}
        
            <div class="form-control">
                {{ form }}
            </div>
        
            <button type="submit">Send</button>
        </form>



        # change error to the last line
        # form-control for each field, thus can have more specific control css in each element
        <form action="/" method="POST">
            {% csrf_token %}
            {% for field in form %}
            <div class="form-control {% if field.errors %}errors{% endif %}">
                {{ field.label_tag }}
                {{ field }}
                {{ field.errors }}
            </div>
            {% endfor %}
            <button type="submit">Send</button>
        </form>



4. 

        #required seems to be default
        # No need to call model 

        class ReviewForm(forms.Form):
            user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            })
            review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
            rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

5. 

        # import model and form
        # form can also be a param for render
        # need to call model for creating an instance 
        def review(request):
            if request.method == 'POST':
                form = ReviewForm(request.POST)

                if form.is_valid():
                    review = Review(
                        user_name=form.cleaned_data['user_name'],
                        review_text=form.cleaned_data['review_text'],
                        rating=form.cleaned_data['rating'])
                    review.save()
                    return HttpResponseRedirect("/thank-you")

            else:
                form = ReviewForm()

            return render(request, "reviews/review.html", {
                "form": form
            })

6.      

        the css of form can be also used as login

# Django Model Form concepts

        # Need to call model 
        class ReviewForm(forms.ModelForm):
            class Meta:
                model = Review
                fields = "__all__"
                # exclude = ['owner_comment']
                labels = {
                    "user_name": "Your Name",
                    "review_text": "Your Feedback",
                    "rating": "Your Rating"
                }
                error_messages = {
                    "user_name": {
                    "required": "Your name must not be empty!",
                    "max_length": "Please enter a shorter name!"
                    },
                    "rating":{
                        "max_value":"Bitch! max is five"
                    }
                }

        # Do not need to call model for creating an instance 

        def review(request):
            if request.method == 'POST':
                form = ReviewForm(request.POST)

                if form.is_valid():
                    form.save()
                    return HttpResponseRedirect("/thank-you")

            else:
                form = ReviewForm()

            return render(request, "reviews/review.html", {
                "form": form
            })