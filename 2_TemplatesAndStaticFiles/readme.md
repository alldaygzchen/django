## Django setups ##  


[step0] : create folder 2_TemplatesAndStaticFiles  
[step1] : python -m venv lessontwo  
[step2] : lessonone\Scripts\activate  
[step3] : python -m pip install django==3.1.5  
[step4] : test it using command: django-admin  
[step5] : command:　django-admin startproject TemplatesAndStaticFiles  
[step6] : command : cd TemplatesAndStaticFiles  
[step6] : create app command: python manage.py startapp challenges  
[step8] : python manage.py runserver  

## App Settings ##    

[step1] : go to main module => settings.py   
    
    # SPECIFIC SETTINGS  
    INSTALLED_APPS => ['challenges']  
    
    # GLOBAL SETTINGS  
    TEMPLATES => 'DIRS': [ BASE_DIR / "templates"]  & 'APP_DIRS': True  
    STATICFILES_DIRS => [ BASE_DIR / "static"]  # No 'APP_DIRS': True  Exists

[step2] : Add templates and static folder in main project [BASE_DIR]    

[step3] :  Since APP (challenges) is added  in SPECIFIC SETTINGS & 'APP_DIRS': True   
    
    Add templates and static folder in APP (add appname folder to prevent automatically parsing error with same filename)

[step4] : Create base.html in main project templates and base.css in main project static


    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{% block page_title %}My Challenges{% endblock %}</title>
        <link rel="stylesheet" href="{% static "base.css" %}">
        {% block css_files %}{% endblock %}
    </head>
    <body>
        {% block content %}{% endblock %}
    </body>
    </html>

[step5] : Create 404.html in main project templates
    {% extends "base.html" %}

    {% block page_title %}
    Something went wrong - we could not find that page!
    {%endblock%}

    {% block content %}
    <h1>We could not find that page!</h1>
    <p>Sorry, but we could not find a matching page!</p>
    {% endblock %}



## Start App ##  

[step1] : go to app => create urls.py file , define views.py  
        
        urls.py and views.py (one to one)
        views.py and templates may not (one to one) e.g. monthly_challenge_by_number

[step2] : templates and static may not (one to one).  

        e.g. 404.html  
        Still suggest to order these in alignment (Easier to debug)  


[step3] : go to main app => urls.py

        urlpatterns = [
            path('admin/', admin.site.urls),
            path("challenges/", include("challenges.urls"))
        ]       

[hint1]:  urls.py <=> templates (relationship)  
        url is just like redirect

        <header>
            <nav>
            <a href="{% url "index" %}">All Challenges</a>
            </nav>
        </header>

[hint2]:  includes folder header.html  
        just a piece of html without metadata

        <header>
            <nav>
            <a href="{% url "index" %}">All Challenges</a>
            </nav>
        </header>        