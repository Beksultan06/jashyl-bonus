from django.db import models

# Create your models here.
class Partners(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    logo = models.ImageField(
        upload_to='partners',
        verbose_name='логотип'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Партнеры'