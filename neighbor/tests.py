from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile, Neighbourhood, Post, Business

# Create your tests here.


class ProfileTestClass(TestCase):
    '''
    Test case for the Profile class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create instance of Profile class
        self.new_profile = Profile(bio="I am superwoman")

    def test_instance(self):
        '''
        Test case to check if self.new_profile in an instance of Profile class
        '''
        self.assertTrue(isinstance(self.new_profile, Profile))


    def test_get_other_profiles(self):
        '''
        Test case to check if all profiles are gotten from the database
        '''
        self.eliane = User(username="elly")
        self.eliane.save()

        self.eliane = User(username="habibi")
        self.eliane.save()

        self.test_profile = Profile(user=self.eliane, bio="Another Profile")
        gotten_profiles = Profile.get_other_profiles(self.eliane.id)
        profiles = Profile.objects.all()


class Neighbourhood(TestCase):
    '''
    Test case for the Neighbourhood class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Profile class
        '''
        # Create a Image instance
        self.new_Image = Image(
            caption='hey')

    def test_instance(self):
        '''
        Test case to check if self.new_Image in an instance of Image class
        '''
        self.assertTrue(isinstance(self.new_Image, Image))


   



class Post(TestCase):
    '''
    Test case for the Comment class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Comment class
        '''
        # Create a Comment instance
        self.new_comment = Comment(
            comment_content='hey')

    def test_instance(self):
        '''
        Test case to check if self.new_comment in an instance of Comment class
        '''
        self.assertTrue(isinstance(self.new_comment, Comment))

    def test_get_Image_comments(self):
        '''
        Test case to check if get Image comments is getting comments for a specific Image
        '''
        self.eliane = User(username="eli")
        self.eliane.save()

        self.eliane = User(username="habibi")
        self.eliane.save()

        self.test_profile = Profile(user=self.eliane, bio="Another Profile")

        self.test_Image = Image(user=self.eliane, caption="Another Profile")

        self.test_comment = Comment(
            Image=self.test_Image, comment_content="Wow")

        gotten_comments = Comment.get_Image_comments(self.test_Image.id)

        comments = Comment.objects.all()

        # No comments were saved so expect True
        self.assertTrue(len(gotten_comments) == len(comments))


