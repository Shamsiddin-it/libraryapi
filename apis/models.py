from django.db import models

class Category(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField( max_length=250)
    birth_year = models.CharField( max_length=50)
    def __str__(self):
        return self.name
class Typography(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField( max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    typography = models.ForeignKey(Typography, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    amount = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.IntegerField()
    
