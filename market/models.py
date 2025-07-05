from django.db import models

class CAddress(models.Model):
    landmark = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.landmark}, {self.city}"

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    feedback = models.TextField(blank=True, null=True)
    address = models.ForeignKey(CAddress, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SHG(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    dom = models.DateField()
    doe = models.DateField()
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    shg = models.ForeignKey(SHG, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    order_time = models.TimeField()

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    mode = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment for Order {self.order.id}"

