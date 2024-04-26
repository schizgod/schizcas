# myapp/models.py
from django.db import models
from django.utils.html import format_html

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)

    def __str__(self):
        return self.title

class CasinoBanner(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    image = models.ImageField(upload_to='casino_banners/')
    description = models.TextField(blank=True)
    button_text = models.CharField(max_length=50, default='Играть сейчас')
    button_position = models.CharField(
        max_length=20,
        choices=[
            ('top', 'Сверху'),
            ('bottom', 'Снизу'),
        ],
        default='bottom'
    )
    button_style = models.CharField(
        max_length=20,
        choices=[
            ('default', 'Стандартный'),
            ('gold', 'Золотой'),
        ],
        default='default'
    )

    def __str__(self):
        return self.title

    def image_preview(self):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 150px;" />', self.image.url)

    class Meta:
        verbose_name_plural = 'Casino Banners'

class BlackjackPublication(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blackjack_images/')
    description = models.TextField()

    def __str__(self):
        return self.title
