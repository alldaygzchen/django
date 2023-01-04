# Download 
    SQLite Manager Chrome extensions


# Setup Environment

    [step1] 
        python -m venv lessonfive  
    [step2]
        lessonfive\Scripts\activate  
    [step3]
        python -m pip install django==3.1.5  
    [step4]
        run django-admin in cmd  
    [step5]
        copy book_store folder in lessonfour and delete migrations (delete sqlite3 in this tutorial for pratice)
        In practice, save the migration files and delete sqlite3
    [step6]
        write models.py for creating tables 
    [step7] 
        python manage.py makemigrations  
    [step8] 
        python manage.py migrate  
    [step9] 
        python manage.py createsuperuser 
    [step10]
        write admin.py to have a beeter view in admin pannel
    [step11] 
        http://127.0.0.1:8000/admin/ go to the admin and add data
            
# Add Data in Admin            
    Add Country, Address, Author, Book data respectively

# Django commands

    models.py

    [One to Many]:   
        models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="books")  

    [One to One]:  
        models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    [Many to Many]:  
        models.ManyToManyField(Country, blank=True)

    [notes]:
        models.CASCADE: if author row deleted, any related book row will be deleted in book_outlet_book table

        class Meta:
            verbose_name_plural = "Address Entries" #preventing showing addresss in admin or somewhere else

        def __str__(self): # showing records in shell or admin

    [common commands]
        models.CharField()
        models.IntegerField()
        models.SlugField()

    [python shell]
        1. the best thing of django ORM is querying data with variable

        e.g. 
            jkrowling = Author(first_name='sth',last_name='sth')
            jkrowling.save()
            book_test = Book(title='sth',rating=3,...,author=jkrowling)
            book_test.save()

        2. Cross model query

        e.g. 
            From books finding related author
            Books.objects.filter(author__last_name__contains="sth")

            From author finding related books
            Author.objects.get(first_name='jk')
            jkr.book_set.all()

            For many to many or one to many,
            the attribute will be lower case adding _set. For one to one will just be lower case

            If we want to change name, add related_name attribute
            models.ForeignKey(
            Author, on_delete=models.CASCADE, null=True, related_name="books")

        3. Remember to migrate, after changing field attribute or adding field
    
    admin.py

    [Show tables in admin panel]
    admin.site.register(Book, BookAdmin)
    admin.site.register(Author,AuthorAdmin)
    admin.site.register(Address)
    admin.site.register(Country)`
        
    [Naming]
    BookAdmin,AuthorAdmin

    [Notes]
    BookAdmin and AuthorAdmin overwrites the def __str__(self) result
    https://docs.djangoproject.com/en/4.1/topics/db/queries/ [Saving ForeignKey and ManyToManyField fields]








# Sqlite Insight
    Tables included 
        auth_group
        auth_group_permissions
        auth_permission
        auth_user
        auth_user_groups
        auth_user_user_permissions
        book_outlet_address
        book_outlet_author
        book_outlet_book
        book_outlet_book_published_countries
        book_outlet_country
        django_admin_log
        django_content_type
        django_migrations
        django_session

# Sql Comment Notes
    Compare results
        SELECT * from "book_outlet_book" LIMIT 10
        SELECT * from "book_outlet_author" LIMIT 10

    We found that foerign key cannot save multiple list id
    thus, for many to many we create an intermediate table

    However 
    one to one:
    the foreign key can be added either in both side, Find the one which is more reasonable

    one to many:
    e.g. one author can have multiple book 
    foreign key should be added in Book model

# Common error 
    Slug should not be empty, otherwise the url endpoint cannot be runned




    


