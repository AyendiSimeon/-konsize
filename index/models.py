from django.db import models
from django.shortcuts import reverse

# Create your models here.



class Category(models.Model):
    title = models.CharField(max_length=100) 
    slug = models.SlugField(max_length=100, null=False)
    logo = models.ImageField(upload_to='media/catlogo', blank=True, null=True, help_text='Optional')
    more = models.BooleanField(default=False, blank=True, verbose_name="For Add In Right Menu")
    created_at = models.DateTimeField(auto_now_add=True)
    disc = models.BooleanField(default=False, verbose_name='Add In Disclaimer')
    hit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def post_count(self):
        return self.posts.all().count()  

    def get_absolute_url(self):
        return reverse('CategoryList', args=[self.slug])
    




class Post(models.Model):
    title = models.CharField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    meta_tags = models.CharField(max_length=2000, blank=True)
    meta_desc = models.TextField(max_length=2000, blank=True)
    slug = models.SlugField(max_length=500, unique=True, null=False)
    image = models.ImageField(upload_to='media/post')
    image_alt_name = models.CharField(max_length=200, blank=True)
    #logo = models.ImageField(upload_to='media/post') #If user want to add university logo(Slider and Post) 
    body = models.TextField(blank=True, null=True)
    #for live classes or offline classes
    tags = models.CharField(max_length=70)
   
    #youtube = models.URLField(max_length=500, default='' )
    author = models.CharField(max_length=20, default="admin" )
    date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False, null=True)
    cover = models.BooleanField(default=False, null=True)
    
    def __str__(self):
        return self.title    
    
    def get_absolute_url(self):
        return reverse("PostDetail",  args=[self.slug])
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)   


