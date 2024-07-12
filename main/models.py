from django.db import models



class CoffeeBaner(models.Model):
    title = models.CharField(max_length=100)
    title1 = models.CharField(max_length=100, null=True, blank=True) 
    detail = models.CharField(max_length=100)
    image = models.ImageField(upload_to="media/", verbose_name="Image", blank=True, null=True)
    
    class Meta:
        verbose_name = "Coffee Banner"
        verbose_name_plural = "Coffee Banners"
    

class About(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to="media/", verbose_name="Image")


    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"


class OurCoffee(models.Model):
    title = models.CharField(max_length=100)
    detail = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="media/", verbose_name="Image", null=True)


    class Meta:
        verbose_name = "Our Coffee"
        verbose_name_plural = "Our Coffees"


class OurBlogs(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to="media/", verbose_name= "Image", null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Our Blog"
        verbose_name_plural = "Our Blogs"


class Contact(models.Model):
    f_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length = 13)
    text = models.TextField()
    
