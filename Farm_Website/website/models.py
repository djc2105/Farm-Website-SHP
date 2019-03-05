from django.db import models

# Create your models here.
class Lot(models.Model):
    lotid = models.CharField(max_length=1, unique=True)

    def __str__(self):
        return self.lotid

class Row(models.Model):
    inlot = models.ForeignKey(Lot)
    rownum = models.IntegerField()

    def __str__(self):
        return (str(self.rownum)+"_"+self.inlot.__str__())

class Plant(models.Model):
    row = models.ForeignKey(Row)
    dateplanted = models.DateField()
    plantname = models.CharField(max_length=128)
    quantity = models.IntegerField()

    def __str__(self):
        return self.plantname