from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class Category (models.Model):

    '''
    Pics category model
    '''
    
    name = models.CharField(max_length=120),

    def __str__(self):
       return self.name
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()        




class  Post(models.Model):

    '''
    Images model
    '''
    
    post = ImageField(manual_crop='')
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=100, blank=False)
    price = models.CharField(max_length=30, blank=False)
    pub_date_posted = models.DateTimeField(auto_now_add=True)
    def __str__(self):
       return self.name
    # ordering data everytime we query the database might be very tedoius. It thus makes available a Meta subclass in any models to specify model-specific options.
    # I used the - minus sign before the order by parameter. This returns the objects in reverse order.
    class Meta:
        ordering = ['-pub_date_posted']

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
    
    @classmethod
    def get_all(cls):
        posts = cls.objects.all()

        return  posts

    @classmethod
    def filter_category(cls,query):
        posts = cls.objects.filter(category__name=query)
        return  posts

    @classmethod
    def search_by_category(cls, search_term):
        posts = cls.objects.filter(category__name__icontains = search_term).order_by('-pub_date_posted')
        return  posts


class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profilir", on_delete=models.CASCADE)
    # picture = ImageField(manual_crop='')
    contact = models.BigIntegerField()
    bio = models.TextField()
    email = models.EmailField()
    post = models.ForeignKey(Post,on_delete=models.CASCADE ,related_name="ME")

    @classmethod
    def get_all(cls):
        all_objects = Profile.objects.all()
        return all_objects

    @classmethod
    def search_by_username(cls,search_term):
        profile = cls.objects.filter(user__name__icontains=search_term)
        return profile

    @classmethod
    def update_caption(cls,current_value,new_value):
        fetched_object = Profile.objects.filter(name=current_value).update(name=new_value)

    @classmethod
    def get_all(cls):
        profiles = Profile.objects.all()
        return profiles

    @classmethod
    def save_profile(self):
        return self.save()

    @classmethod
    def delete_profile(self):
        return self.delete()

    def __str__(self):
        return self.user.username
    
 

