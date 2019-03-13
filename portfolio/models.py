from django.db import models


class Carousel(models.Model):
    heading = models.CharField(max_length=200)
    carousel_num = models.IntegerField(default=99)
    img = models.CharField(max_length=200)
    is_active = models.CharField(max_length=10, null=True, blank=True)
    text = models.TextField()
    text_align = models.CharField(max_length=20, default='text-right', null=True, blank=True)

    def __str__(self):
        return self.Heading
