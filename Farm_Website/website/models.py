from django.db import models
from django.template.defaultfilters import slugify
import uuid

# Create your models here.
class Lot(models.Model):
    lotid = models.CharField(max_length=1, unique=True)
    slug = models.SlugField()

    def save(self,*args,**kwargs):
        self.slug = slugify(self.lotid);
        super(Lot, self).save(*args,**kwargs)

    def __str__(self):
        return self.lotid

class Row(models.Model):
    inlot = models.ForeignKey(Lot)
    rownum = models.IntegerField()
    slug = models.SlugField()

    def save(self,*args,**kwargs):
        self.slug = slugify(str(self.rownum)+"_"+self.inlot.__str__());
        super(Row, self).save(*args,**kwargs)

    def __str__(self):
        return (str(self.rownum)+"_"+self.inlot.__str__())


class Plant(models.Model):
    row = models.ForeignKey(Row)
    dateplanted = models.DateField()
    plantname = models.CharField(max_length=128)
    quantity = models.IntegerField()
    slug = models.SlugField()
    notes = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    archived = models.BooleanField(default=False)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.plantname);
        super(Plant, self).save(*args,**kwargs)

    def __str__(self):
        return self.plantname
