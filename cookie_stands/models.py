from django.db import models
from project.settings import AUTH_USER_MODEL

class CookieStand(models.Model):
    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    hourly_sales = models.JSONField(default=list, blank=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)

    def __str__(self):
        return self.location

    def save(self, *args, **kwargs):
        if self.hourly_sales is None or self.hourly_sales is 'Null' or self.hourly_sales is 'null':
            self.hourly_sales = (self.minimum_customers_per_hour + self.maximum_customers_per_hour) // self.average_cookies_per_sale
        super(CookieStand, self).save(*args, **kwargs)
