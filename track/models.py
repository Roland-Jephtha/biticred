from django.db import models
import uuid

# Create your models here.





class Shipment(models.Model):
    tracking_number = models.CharField(max_length=11, null=True, unique=True, blank=True )
    name = models.CharField(max_length=200, null=True)
    from_country = models.CharField(max_length=200, null=True)
    to_country = models.CharField(max_length=200, null=True)
    receiver_name = models.CharField(max_length=200, null=True)
    delivery_date = models.DateField(null=True)
    order_status = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='post-image', null = True, blank=True)
    moving = models.BooleanField(default=False, null=True)
    ready = models.BooleanField(default=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    
    class Meta:
        ordering = ['-date_created']
    
    
    
    # def save(self, *args, **kwargs):
    #     if not self.tracking_number:
    #         self.tracking_number = self.generate_number()
    #     super().save(*args, **kwargs)
    
    # def generate_number(self):
        
    #     return "23456789" + str(Item.objects.count() + 1)
    
    
    
    def __str__(self):
        # return str(self.tracking_number) + " tracking Number"
        return self.name + " ------ " + self.tracking_number
    
    
    


class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length=255)
    number = models.EmailField(max_length=255, null = True)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null = True)
    
    
    def __str__(self):
        return self.email
    


class Phone(models.Model):
    number = models.CharField(max_length = 255)

    def __str__(self):
        return self.number