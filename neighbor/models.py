from django.db import models

from django.contrib.auth.models import User
# Create your models here.
import datetime as dt
from tinymce.models import HTMLField


class Profile(models.Model):
    bio=models.TextField(max_length=100,blank=True,default="bio please...")
    profilepic=models.ImageField(upload_to='profile/', blank = True,default='../static/images/bad-profile-pic-2.jpeg')
    email=models.CharField(blank=True,max_length=100)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user

class Neighbourhood(models.Model):
    Neighborhood=models.CharField(max_length=30,null=True)
    Neighborhood_location=models.CharField(max_length=30,null=True)
    population=models.PositiveIntegerField(default=0)
    police_no=models.PositiveIntegerField(default=112)
    hospital_no=models.PositiveIntegerField(default=911)
    user=models.ForeignKey(User)
 
    def __str__(self):
        return self.Neighborhood

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def get_neighbourhoods(cls):
        estates = Neighbourhood.objects.all()
        return estates

    @classmethod
    def get_specific_hood(cls,id):
        chosen_hood = cls.objects.get(id=id)
        return chosen_hood

    def update_neighbourhood(self):
        pass

    def update_occupants(self):
        email = models.EmailField(max_length=70,blank=True)

        pass

    @classmethod
    def find_neighbourhood(neigbourhood_id):
        query = cls.objects.filter(name__icontains=search_term)
        return query


class Follow(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    estate=models.ForeignKey(Neighbourhood)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_following(cls,user_id):
        following =  Follow.objects.filter(user=user_id).all()
        return following



class Business(models.Model):
    image=models.ImageField(upload_to='business/' ,null=True,blank=True)
    project=models.CharField(max_length=30,null=True)
    email=models.EmailField(max_length=70,blank=True)
    estate=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return self.project

    @classmethod
    def get_specific_business(cls,id):
        business = cls.objects.filter(id=id)
        return business


    @classmethod
    def get_businesses(cls):
        business = cls.objects.all()
        return business

    @classmethod
    def get_business_by_estate(cls,neighbourhood_id):
        messages = cls.objects.all().filter(estate=neighbourhood_id)
        return messages





    
class Post(models.Model):
    image=models.ImageField(upload_to='photos/',null=True,blank=True)
    image_name=models.CharField(max_length=30)
    message=models.TextField(max_length=100,null=True,blank=True)
    estate=models.ForeignKey(Neighbourhood,on_delete=models.CASCADE,null=True,blank=True)
    user_profile=models.ForeignKey(Profile)
    user=models.ForeignKey(User)

    def save_post(self):
       
        self.save()

    def delete_post(self):
       
        self.delete()

    @classmethod
    def get_posts(cls):
        
        messages = cls.objects.all()
        return messages

    @classmethod
    def get_posts_by_estate(cls,neighbourhood_id):
        
        messages = cls.objects.all().filter(estate=neighbourhood_id)
        return messages