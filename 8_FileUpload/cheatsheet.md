# basic upload method in web
### basics html
        # profiles/ # append_slash default is true
        # enctype="multipart/form-data" is essential

        <form action="/profiles/" method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            <input type="file" name="image" />
            <button>Upload!</button>
        </form>

### views.py

        def store_file(file):
            with open("temp/image.jpg", "wb+") as dest:
                for chunk in file.chunks():
                    dest.write(chunk)

        class CreateProfileView(View):
            def get(self, request):
                return render(request, "profiles/create_profile.html")

            def post(self, request):
                print(request.FILES["image"]) #xxx.jpg
                store_file(request.FILES["image"])
                return HttpResponseRedirect("/profiles")


# django upload method [forms.Form]

### forms.py


        from django import forms

        class ProfileForm(forms.Form):
            user_image = forms.ImageField()
            <!-- user_image = forms.FileField() -->


### setting.py

        MEDIA_ROOT = BASE_DIR / "uploads" 


### models.py
        class UserProfile(models.Model):
            image = models.ImageField(upload_to="images") #uploads/images
            <!-- image = models.FileField(upload_to="images") -->

### run cmd: python manage.py makemigrations and  python manage.py migrate

### views.py

        class CreateProfileView(View):
            def get(self, request):
                form = ProfileForm()
                return render(request, "profiles/create_profile.html", {
                    "form": form
                })

            def post(self, request):
                submitted_form = ProfileForm(request.POST, request.FILES)

                if submitted_form.is_valid():
                    profile = UserProfile(image=request.FILES["user_image"])
                    profile.save()
                    return HttpResponseRedirect("/profiles")
                
                return render(request, "profiles/create_profile.html", {
                    "form": submitted_form
                })

# django upload method [CreateView]

### views.py and delete forms.py


        class CreateProfileView(CreateView):
            template_name = "profiles/create_profile.html"
            model = UserProfile
            fields = "__all__"
            success_url = "/profiles"

        class ProfilesView(ListView):
            model = UserProfile
            template_name = "profiles/user_profiles.html"
            context_object_name = "profiles"

### templates


        <ul>
            {% for profile in profiles %}
            <li>
                <img src="{{ profile.image.url }}">
            </li>
            {% endfor %}
        </ul>

### setting.py

        MEDIA_ROOT = "/user-media/" domain/user-media/

### urls.py

        from django.contrib import admin
        from django.urls import path, include
        from django.conf.urls.static import static
        from django.conf import settings

        urlpatterns = [
            path('admin/', admin.site.urls),
            path("", include("reviews.urls")),
            path("profiles/", include("profiles.urls"))
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) // creating access from outside