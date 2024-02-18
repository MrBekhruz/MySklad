from django.db import models
import uuid
position = [
    ('praktikant','praktikant'),
    ('professional_ishchi','professional_ishchi'),
    ('mike','mike'),
    ('micheal','micheal'),
    ('bexrux','bexrux'),
    ('javohir','javohir'),
    ('ozod','ozod'),
]
cash = [
    ('dollar','dollar'),
    ('sum','sum'),
    ('click','click'),
    ('nasiya','nasiya')
]

class User(models.Model):
    user_full_name = models.CharField(max_length = 255)
    about = models.TextField()
    user_age = models.IntegerField()
    position_name = models.TextField( choices=position)

    def str(self):
        return self.position_name
    

class BazaItems(models.Model):
    products = models.TextField()
    cash_sum = models.CharField(choices= cash ,max_length=255)
    price = models.IntegerField()
    brend = models.CharField(max_length = 255)
    color = models.CharField(max_length = 255)
    seriya_num = models.ForeignKey(User, on_delete = models.CASCADE)
    amount = models.IntegerField()
    kirim_summa = models.IntegerField()
    chiqim_summa = models.IntegerField()

    def str(self):
        return self.products
    
class Client(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.IntegerField()
    register_time = models.DateTimeField(auto_now = False)
    receptionist = models.ForeignKey(User, on_delete = models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)
    def str(self):
        return self.name
    
class ServiceName(models.Model):
    name = models.CharField(max_length=255)
    def str(self):
        return self.name
    
class ServiceXizmati(models.Model):
    client_name = models.ForeignKey(Client, on_delete = models.CASCADE)
    service = models.ForeignKey(ServiceName,on_delete= models.CASCADE)
    merchandice_name = models.TextField()
    merchandice_amount = models.IntegerField()
    technique_color = models.CharField(max_length=255)
    status = models.TextField()
    date = models.DateTimeField(auto_now= False)
    tuzatish_vaqti = models.DateTimeField(auto_now=False)

    def str(self):
        return self.merchandice_name

class EndService(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE)
    tovar_nomi = models.TextField()
    sklad_tovar = models.TextField(null=True)
    usta = models.CharField(max_length = 255,choices=position)
    service_price  = models.IntegerField()
    enddate = models.DateTimeField(auto_now=False)
    comments = models.TextField()

    def str(self):
        return self.tovar_nomi
    
class ReturnService(models.Model):
    user_name=models.ForeignKey(User,on_delete = models.CASCADE)
    technique = models.CharField(max_length=255)
    comment = models.TextField()

    def str(self):
        return self.user_name