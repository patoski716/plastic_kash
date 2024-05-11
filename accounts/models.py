from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=False)
    subject = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


class Vendor(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to='upload/', blank=True,null=True)
    phone= models.CharField(max_length=100, null=False)
    address=models.TextField()
    email = models.EmailField(max_length=100, null=False)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    image=models.ImageField(upload_to='upload/', blank=True,null=True)
    name=models.CharField(max_length=200)
    quantity=models.IntegerField()
    description=models.TextField()
    price=models.DecimalField(max_digits=5, decimal_places=1)
    vendor=models.ForeignKey(Vendor, on_delete=models.DO_NOTHING)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
