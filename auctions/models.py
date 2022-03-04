from django.contrib.auth.models import AbstractUser
from django.db import models

from .categories import CATEGORIES
class User(AbstractUser):
    pass
class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(blank=True)
    category = models.IntegerField(blank=True, choices=CATEGORIES)

    def __str__(self):
        return f"Item {self.id}: Seller - {self.user}, Title - {self.title}, Description - {self.description}, Price - ${self.price}, Image: {self.image_url}, Category - {self.category}"

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    item = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bid = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.user} bid ${self.bid} on {self.item.title}'

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    item = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f'{self.user}: {self.comment}'