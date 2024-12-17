from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="project/%Y/%m/%d/", default="prject/1.jpg")
    



    def __str__(self):
        return self.name
    

 

 
class Book(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Name:")
    autor = models.CharField(max_length=100, unique=True, null=True,verbose_name='Autor:')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,  related_name='books')
    desciption = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="project/%Y/%m/%d/", default="prject/1.jpg")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    file = models.FileField(upload_to='file/', null=True)
    
 
    def __str__(self):
        return self.name



class User_bot(models.Model):
    name = models.CharField(max_length=100 )
    surname = models.CharField(max_length=100, unique=True, null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    desciption = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="project/%Y/%m/%d/", default="prject/1.jpg")
    date = models.DateTimeField(auto_now=True)
 
 

    def __str__(self):
        return self.name



class New(models.Model):
    title = models.CharField(max_length=100, unique=True, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="project/%Y/%m/%d/", default="prject/1.jpg")
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title