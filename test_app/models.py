from django.db import models
from django.utils import timezone
# Create your models here.

class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    description = models.TextField()
    phone = models.PositiveIntegerField()
    is_live = models.BooleanField()
    amount = models.FloatField()
    extra_name = models.CharField(max_length=250, editable=False, default="null")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{} - {}".format(self.name, self.created_at.strftime(' %H: %M: %S')) 
    
    class Meta:
        ordering = ("-created_at",) # xap xep data theo cot created_at, "-" la giam dan
        verbose_name_plural = "Test Model" # thay doi ten cua object hien thi trong admin
    def save(self, *args, **kwargs):
        self.extra_name = "{} - {}".format(self.name, self.phone) 
        super().save(*args, **kwargs)

class ModelX (models.Model):
    test_content = models.ForeignKey(TestModel, on_delete=models.CASCADE, related_name="test_content")
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{} - {}".format(self.test_content.name, self.mileage)

    class Meta:
        ordering = ("-created_at",) # xap xep data theo cot created_at, "-" la giam dan
        verbose_name_plural = "Model X" 


class ModelY (models.Model):
    test_content = models.OneToOneField(TestModel, on_delete=models.CASCADE, related_name="test_content_y")
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "{} - {}".format(self.test_content.name, self.mileage)

    class Meta:
        ordering = ("-created_at",) # xap xep data theo cot created_at, "-" la giam dan
        verbose_name_plural = "Model Y" 