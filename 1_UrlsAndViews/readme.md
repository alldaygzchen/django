[step0] : create folder 1_UrlsAndViews
[step1] : python -m venv lessonone  
[step2] : lessonone\Scripts\activate  
[step3] : python -m pip install django==3.1.5   
[step4] : test it using command: django-admin  
[step5] : command:　django-admin startproject <projectName>  
[step6] : command : cd <projectName> & python manage.py runserver   
[step6] : create app command: python manage.py startapp challenges  


Note 1:   
1. learn creating environment  
2. UrlsAndViews/urls.py & challenges/urls.py & challenges/views.py  
3. urls.py = > from django.urls import path,include  
    e.g. path("<int:month>", views.monthly_challenge_by_number) check whether is integer and throw var as an int parameter. This is a dynamic url also.  
4. views.py => from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect from django.urls import reverse  
    e.g. redirect_path = reverse("month-challenge", args=[redirect_month]) # create fullpath: /challenge/january  