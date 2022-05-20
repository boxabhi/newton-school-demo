from django.db import models

# Create your models here.

class Store(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)



class StudentManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    student_age = models.IntegerField(default=18)
    is_deleted = models.BooleanField(default = False)
    student_birthday = models.DateField(null=True , blank=True)
    student_info = models.TextField()

    objects = StudentManager()
    admin_objects = models.Manager()
    
    def __str__(self) -> str:
        return self.student_name

class Category(models.Model):
    category_name = models.CharField(max_length=100)
        
    def __str__(self) -> str:
        return self.category_name

class Product(models.Model):
    category = models.ForeignKey(Category , related_name ="product_category" , on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.IntegerField()
        
    def __str__(self) -> str:
        return self.product_name
