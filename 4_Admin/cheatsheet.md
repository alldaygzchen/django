[step1]: 

    Create venv environment

[step2]: 

    copy book_store folder
    delete migrations folder except init

[step3]:

    python manage.py makemigrations
    python manage.py migrate

    python manage.py shell
    aware: https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create
    Book(title="A Heart That Works",rating=4,author="Rob Delaney",is_bestselling=True)
    Book(title="Afterlives",rating=5,author="Abdulrazak Gurnah",is_bestselling=False)

    


[step4]:

    python manage.py createsuperuser

[step5]:  

book_outlet/admin.py  
https://stackoverflow.com/questions/10330916/how-to-hide-some-fields-in-django-admin  
https://stackoverflow.com/questions/29128240/allowing-edit-to-editable-false-fields-in-django-admin

        class BookAdmin(admin.ModelAdmin):
        #   readonly_fields = ("slug",) # edit admin form
        prepopulated_fields = {"slug": ("title",)} #  admin table
        list_filter = ("author", "rating",)  #  admin table
        list_display = ("title", "author",'rating') # admin table
        exclude = ('rating',) # edit admin form

book_outlet/models.py  
https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django  

    1.  default null =False, default blank = False
    2.  editable =False => the field in admin form is hidden but if readonly_fields = ("slug",) (in admin.py) will still shown
    3.  blank= True  => no validation check
    4.  delete save in models.py => Otherwise it will overide, but the save of python manage.py shell will not be used when entering shell
    5.  if models.py field attribute is changed, we still need migrations

[Additionals]  
1. https://www.google.com/search?q=middleware+404+django&client=ms-android-samsung-ss&hl=zh-TW&prmd=ivn&sxsrf=ALiCzsZj99dinyoJZzXcz7G29u7iu5sgRw:1670767565964&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjW1JWa3vH7AhXNCaYKHSntCJsQ_AUIGigB&biw=384&bih=735&dpr=2.81#imgrc=oTIabbEb9-v8rM    
2. https://www.itread01.com/article/1520996800.html  
  
