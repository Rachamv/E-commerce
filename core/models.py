from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe

class Category(models.Model):
    cid = ShortUUIDField(unique=
    True, 
    length=10, 
    max_length=30, 
    prefix= "cat", alphabet="abcdefghijk123456789") 
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="category")

    class Meta:
        verbose_name_plural = "Categories"
    
    def category_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title

class Vendor(models.Model):
    vid = ShortUUIDField(unique=
    True, 
    length=10, 
    max_length=30, 
    prefix= "ven", alphabet="abcdefghijk123456789")

    title = models.CharField(max_length=100, default="Nestify")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    cover_image = models.ImageField(upload_to=user_directory_path, default="vendor.jpg")
    # description = models.TextField(null=True, blank=True, default="I am am Amazing Vendor")
    description = RichTextUploadingField(null=True, blank=True, default="I am am Amazing Vendor")

    address = models.CharField(max_length=100, default="123 Main Street.")
    contact = models.CharField(max_length=100, default="+123 (456) 789")
    chat_resp_time = models.CharField(max_length=100, default="100")
    shipping_on_time = models.CharField(max_length=100, default="100")
    authentic_rating = models.CharField(max_length=100, default="100")
    days_return = models.CharField(max_length=100, default="100")
    warranty_period = models.CharField(max_length=100, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" height="50" />' % (self.image.url))

    def __str__(self):
        return self.title
    
