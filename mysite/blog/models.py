from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Post(models.Model):

    author=models.ForeignKey('auth.User',on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
# Here post_detail is the class based detail view for the model Post.

        #comments is the related_namefrom Comment model class therefore to access a variable of other class self.<class_name>.<function_name>('variable_name') is used.
        # self helps in accessing all variables of current class
    def __str__(self):
        return self.title

class Comment(models.Model):

    post=models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approved_comments=models.BooleanField(default=False)

    def approve(self):
        self.approved_comments=True
        self.save()

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text
