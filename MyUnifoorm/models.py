from django.db import models

class User(models.Model):
    Email = models.CharField(max_length=25 ,primary_key= True)
    Password  = models.CharField(max_length=12)
    Name = models.TextField()
    PhoneNumber = models.CharField(max_length=13)
    Address = models.TextField()
    
class Product(models.Model):
    ProductID = models.CharField(max_length=5,primary_key=True)
    ProductName = models.TextField()
    ProdImg = models.ImageField(upload_to="productpic" ,default="null")
    Description = models.TextField()
    Price = models.FloatField()
    Brand = models.CharField(max_length=20)
    Size = models.CharField(max_length=4)
    Color = models.CharField(max_length=10)
    Quantity = models.IntegerField()
    Material = models.CharField(max_length=20)


class Order(models.Model):
        
    OrderID  = models.AutoField( primary_key= True)
    Email = models.ForeignKey(User,on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product,on_delete=models.CASCADE)
    Qty = models.IntegerField(default=0)
    OrderDate = models.DateField()
    OrderStatus = models.CharField(max_length=20)
    TotalAmount = models.FloatField()



class Review(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Order , on_delete=models.CASCADE)
    Email = models.ForeignKey(User, on_delete=models.CASCADE)
    Comment = models.TextField()
    ReviewDate = models.DateField()
    



