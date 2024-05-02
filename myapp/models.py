from django.db import models

class ProductDetails(models.Model):
  product_name=models.CharField(max_length=255)
  product_price=models.CharField(max_length=255)
  CATEGORIES=[
    ('skincare','Skincare'),
    ('makeup', 'Makeup'),
    ('haircare','Haircare'),
    ('fragrances', 'Fragrances'),
    ('bodycare','Bodycare'),
  ]
  categories=models.CharField(max_length=20, choices= CATEGORIES)
  description=models.TextField()
  product_image = models.ImageField(upload_to='static/productimages/', null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
  return self.product_name