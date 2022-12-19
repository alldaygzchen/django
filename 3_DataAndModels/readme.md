[Step 1] Create models.py content

            class Book(models.Model):
                title = models.CharField(max_length=50)
                rating = models.IntegerField(
                    validators=[MinValueValidator(1), MaxValueValidator(5)])
                author = models.CharField(null=True, max_length=100)
                is_bestselling = models.BooleanField(default=False)
                # Harry Potter 1 => harry-potter-1
                slug = models.SlugField(default="", null=False, db_index=True)

                def get_absolute_url(self):
                    return reverse("book-detail", args=[self.slug])
                
                #overwrite
                def save(self, *args, **kwargs):
                    self.slug = slugify(self.title)
                    super().save(*args, **kwargs)

                def __str__(self):
                    return f"{self.title} ({self.rating})"

[Step 2] python manage.py makemigrations & python manage.py migrate  
[Step 3] python manage.py shell

        from book_outlet.models import Book

Instance operation:   

***create***  

        heart_works = Book(title="A Heart That Works",rating="4",author="Rob Delaney",is_bestselling=True)
        afterlives = Book(title="Afterlives",rating="6",author="Abdulrazak Gurnah",is_bestselling=True)
        lover_nights = Book(title="All the Lovers in the Night",rating=100,author="Mieko Kawakami",is_bestselling=True)
        Book(title="All This Could Be Different",rating=3,author="Sarah Thankam Mathews",is_bestselling=True)

***update*** 

        lover_nights.rating =3
        lover_nights.save()

***delete***

        heart_works.delete()
        afterlives.delete()


class operation: 

***read*** 

        Book.objects.all()
        Book.objects.all()[0].author
        Book.objects.get(id=3)
        Book.objects.get(id=66) # error (use exception)
        Book.objects.filter(id=3) #list
        Book.objects.filter(rating__gt=2,is_bestselling=True)
        from django.db.models import Q
        Book.objects.filter(Q(rating__gt=4)|Q(is_bestselling=True))


        (Advance)
        b = Book.objects.all() #<QuerySet [<Book: All the Lovers in the Night (3)>, <Book: All This Could Be Different (3)>, <Book: this is the title 1 (4)>, <Book: this is the title 2 (5)>]>
        b[0].title='bb' 
        b # <QuerySet [<Book: All the Lovers in the Night (3)>, <Book: All This Could Be Different (3)>, <Book: this is the title 1 (4)>, <Book: this is the title 2 (5)>]>
        list(b)
        b[0].title='bb' 
        b # <QuerySet [<Book: bb (3)>, <Book: All This Could Be Different (3)>, <Book: this is the title 1 (4)>, <Book: this is the title 2 (5)>]>
        Book.objects.all() #<QuerySet [<Book: All the Lovers in the Night (3)>, <Book: All This Could Be Different (3)>, <Book: this is the title 1 (4)>, <Book: this is the title 2 (5)>]>


Bulk operation

***create:*** https://stackoverflow.com/questions/48932669/using-django-bulk-create-gives-unique-constraint-failedsolgeo-hourly-id

        Book.objects.bulk_create(
            [
                Book(title="A Heart That Works",rating=4,author="Rob Delaney",is_bestselling=True),
                Book(title="Afterlives",rating=5,author="Abdulrazak Gurnah",is_bestselling=False)
            ]
        )
        Book.objects.create(title="An Immense World",rating=1,author="Ed Yong",is_bestselling=False)

***delete:***

        Book.objects.filter(id__gt=4).delete()

***update*** 

        https://stackoverflow.com/questions/22980448/django-objects-filter-is-not-updating-field-but-objects-get-is
        https://docs.djangoproject.com/en/3.0/topics/db/queries/#when-querysets-are-not-cached
        objs = Book.objects.filter(id__gt=13)
        myobjs = [i for i in objs] #evaluate and cache
        myobjs[0].title='this is the title 1'
        myobjs[1].title='this is the title 2'
        Book.objects.bulk_update(myobjs, ['title'])

        objs = Book.objects.filter(id__gt=13)
        bool(objs) #evaluate and cache
        objs[0].title='this is the title 1'
        objs[1].title='this is the title 2'
        objs # <QuerySet [<Book: this is the title 1 (4)>, <Book: this is the title 2 (5)>]>
        Book.objects.bulk_update(objs, ['title']) [<Book: All the Lovers in the Night (3)>, <Book: All This Could Be Different (3)>, <Book: this is the title 1 (4)>, <Book: this is the title 2 (5)>]>





Aggregation 

Order




[Notes]:   
1. check whether need to run runserver first (no)  
2. when to migrate: change the structure of database table
3. migration or makemigrations: 1.makemigrations 2.migration     
4. models.Model.objects.all()    
5. why models.py not adding self in field:  
    https://stackoverflow.com/questions/53318475/why-do-we-need-init-to-initialize-a-python-class
6. Django validation is mostly application level validation and not validation at DB level.  
    https://stackoverflow.com/questions/40881708/django-model-validator-not-working-on-create