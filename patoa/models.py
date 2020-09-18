from django.db import models

class  Claimset(models.Model):
    patno =models.IntegerField(default=0)
    pubno =models.IntegerField(default=0)
    claim_list = models.CharField(max_length=20000, null=True,blank=True)
    total_claim = models.IntegerField(default=1)
    add112 = models.CharField(max_length=10000, null=True,blank=True)
    obj = models.CharField(max_length=10000, null=True,blank=True)
    
    # def __str__(self):
    #     return f'{self.patno}  {self.pubno}'
 