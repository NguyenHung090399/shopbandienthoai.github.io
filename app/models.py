from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model) : 
    user    = models.OneToOneField(User , on_delete=models.SET_NULL , null=True ,blank=False)
    name    = models.CharField(max_length=200 , null=True)
    email   = models.CharField(max_length=200 , null=True)
    age     = models.IntegerField(null=True)
    avatar  = models.ImageField(upload_to='images_customer' , null=False , default=None)

    def __str__(self) : 
        return self.name
    @property 
    def AvatarURL(self) :
        try : 
            url = self.avatar.url
        except : 
            url = ''
        return url

class Category(models.Model) : 
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50 , null=True)

    def __str__(self) : 
        return self.name

class Product(models.Model) : 
    category = models.ForeignKey(Category , on_delete=models.SET_NULL , null=True , blank=False)
    name = models.CharField(max_length=200 , null=True)
    price = models.FloatField()
    describe = models.TextField()
    digital = models.BooleanField(default=False , null=True , blank=False)
    images = models.ImageField(upload_to='images_product' , null=False , default=None)

    def __str__(self) : 
        return self.name
    
    @property 
    def ImageURL(self) :
        try : 
            url = self.images.url
        except : 
            url = ''
        return url

class Order(models.Model) : 
    customer = models.ForeignKey(Customer , on_delete=models.SET_NULL , null=True , blank=False)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False , null=True , blank=False)
    transaction_id = models.CharField(max_length=200 , null=True)

    def __str__(self) : 
        return str(self.id)
    
    @property
    #tinh tong so luong san pham trong orderitem
    def get_cart_item(self) : 
        orderitem = self.orderitem_set.all()
        total = 0 
        for item in orderitem : 
            total = total+item.quantity
        return total 

    @property    
    #tinh tong tien trong orderitem
    def get_cart_total(self) : 
        orderitem = self.orderitem_set.all()
        total = 0 
        for item in orderitem : 
            total = total + item.get_total 
        return total
class OrderItem(models.Model) : 
    product = models.ForeignKey(Product , on_delete=models.SET_NULL , null=True , blank= False)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL , null=True , blank=False)
    quantity = models.IntegerField(default=0 , null=True , blank=False)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    #tinh tong so tien cua mot loai san pham = soluong * gia
    def get_total(self) : 
        total = self.quantity* self.product.price
        return total

class ShippingAddress(models.Model) : 
    customer = models.ForeignKey(Customer , on_delete=models.SET_NULL , null=True , blank= False)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL , null=True , blank= False)
    address = models.CharField(max_length=200 , null=True)
    city = models.CharField(max_length=200 , null=True)
    state = models.CharField(max_length=200 ,null=True)
    mobile = models.CharField(max_length=10 , null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str(self) : 
        return self.address