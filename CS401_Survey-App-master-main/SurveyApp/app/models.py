from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


# Change forms register django

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class Entity(models.Model):
    question =  models.TextField()
    #userId = models.ForeignKey(User,on_delete=models.CASCADE)
    #post_time = models.DateField(auto_now=False,auto_now_add=False)
    #time_stamp = models.DateField(auto_now_add=True,auto_now=False, null=True,blank=True)
    #Is_active = models.BooleanField()
    #Is_permanent = models.BooleanField()
    def __str__(self):
        return self.question

class Rate(models.Model):
    rate_question = models.TextField(max_length=50, default="")
    #userId = models.ForeignKey(User,on_delete=models.CASCADE)
    #post_time = models.DateField(auto_now=False,auto_now_add=False)
    #time_stamp = models.DateField(auto_now_add=True,auto_now=False, null=True,blank=True)
    #Is_active = models.BooleanField()
    #Is_permanent = models.BooleanField()
    def __str__(self):
        return self.rate_question

class Poll(models.Model):
    questionId = models.ForeignKey(Entity,on_delete=models.CASCADE)
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_three = models.CharField(max_length=50)
    option_four = models.CharField(max_length=50, default='')
    option_five = models.CharField(max_length=50,default='')
    option_count_one = models.IntegerField(default=0)
    option_count_two = models.IntegerField(default=0)
    option_count_three = models.IntegerField(default=0)
    option_count_four = models.IntegerField(default=0)
    option_count_five = models.IntegerField(default=0)

    def __str__(self) :
        return self.option_one + ":" + self.option_two + ":" +self.option_three + self.option_four + ":" +self.option_five


    def total(self):
        return self.option_count_one + self.option_count_two + self.option_count_three + self.option_count_four + self.option_count_five
    

#class Profile(models.Model):
#    user = models.ForeignKey(User,on_delete=models.CASCADE)
#    id_user = models.IntegerField()

#    def __str__(self):
#        return self.user.username
    
class Rating(models.Model):
    rate_question = models.TextField(max_length=100, default="")
    score = models.IntegerField(default=0, validators=[
        MaxValueValidator(5),
        MinValueValidator(1),
    ])

    def __str__(self):
        return str(self.pk)
    


    
