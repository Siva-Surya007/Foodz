from django.db import models


class StoreCategory(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category')

    class Meta:
        db_table = 'restaurent_store_category'
        verbose_name = 'store category'
        verbose_name_plural = 'store categories'
        ordering = ['-id']


    def __str__(self):
        return self.name
    

class Store(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(StoreCategory,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store')
    tagline = models.CharField(max_length=255)
    rating = models.FloatField()
    time = models.IntegerField()

    class Meta:
        db_table = 'restaurent_store'
        verbose_name = 'store'
        verbose_name_plural = 'stores'
        ordering = ['-id']

    def __str__(self):
        return self.name
    

class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='slider')
    store = models.ForeignKey(Store,on_delete=models.CASCADE)

    class Meta:
        db_table = 'restaurent_slider'
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'
        ordering = ['-id']

    def __str__(self):
        return self.name