from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255,verbose_name = 'name_product')
    description  =  models.TextField()
    price = models.IntegerField()
    image_url = models.URLField(verbose_name="URL img")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='product')

    def __str__(self):
        return self.name

class Manager(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Store hashed passwords

    def __str__(self):
        return self.username

class ProductManager(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title} - {self.manager.username}"
    

