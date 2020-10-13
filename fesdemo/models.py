from django.db import models
from django.core.validators import FileExtensionValidator
from django.utils import timezone

class User(models.Model):
    name=models.CharField(max_length=250)
    roleDesc=models.CharField(max_length=250,default='',null=True)
    desc=models.TextField(default='',null=True)
    fb=models.URLField(max_length=250,default='',null=True)
    email=models.EmailField(null=True)
    profileImg=models.ImageField(upload_to='Users')
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('name',)
        verbose_name="User"
        verbose_name_plural="Users"

class NewsCategory(models.Model):
    name=models.CharField(max_length=250,verbose_name="gategory of the news")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('name',)
        verbose_name="gategory of the news"
        




class Comment(models.Model):
    name=models.CharField(max_length=250,verbose_name="User name")
    email=models.EmailField(verbose_name="E-mail")
    content=models.TextField(verbose_name="content")
    created=models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering =('-created',)
        verbose_name_plural="Comment section"
        verbose_name="Comment"


class News(models.Model):
    title=models.CharField(max_length=250,verbose_name="title")
    slug=models.SlugField(max_length=250,unique=True,verbose_name="site route")
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="author")
    categories=models.ManyToManyField(NewsCategory,verbose_name="gategory of the news")
    comments=models.ManyToManyField(Comment,blank=True)
    newsImg=models.ImageField(upload_to='news',verbose_name="picture")
    body=models.TextField(verbose_name="content")
    featured=models.BooleanField(default=False,null=True,verbose_name="featured?")
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering =('-created',)
        verbose_name="News"
        


class ContactUs(models.Model):
    fullName=models.CharField(max_length=254,verbose_name="fullName")
    email=models.EmailField(verbose_name="E-mail")
    phone=models.CharField(max_length=12,verbose_name="phoneNumber")
    text=models.TextField(verbose_name="content")
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.fullName

    class Meta:
        ordering =('-created',)
        verbose_name_plural="ContactUs"
        verbose_name="ContactUs"



# GLOBAL PAGE SETTINGS MODELS

class Settings(models.Model):
    title=models.CharField(max_length=250,default='Сайтын Тохиргоо',editable=False)

    # Social Media
    facebook=models.URLField(max_length=200,default='',blank=True,verbose_name="facebook");
    twitter=models.URLField(max_length=200,default='',blank=True,verbose_name="twitter");
    gmail=models.URLField(max_length=200,default='',blank=True,verbose_name="email");

    # Holboo Barih
    phoneList=models.ManyToManyField('phoneNumber',verbose_name="phoneNumber")
    email=models.EmailField(max_length=254,verbose_name="contactNumber")

    


    



    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural="Configure of the website"
        verbose_name="Configure"

class phoneNumber(models.Model):
    phone=models.CharField(max_length=200,unique=True,verbose_name="phoneNumber")

    def __str__(self):
        return self.phone

class sponsored(models.Model):
    ner=models.CharField(max_length=250,default='',blank=True,verbose_name="Sponsored by")
    img=models.ImageField(upload_to='bidniTuhai',default='',verbose_name="Sponsored picture")

    def __str__(self):
        return self.ner