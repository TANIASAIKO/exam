from django.db import models

# Create your models here.

SUITS = [ 'diamond', 'heart', 'club', 'spade' ]
SUIT_CHOICES = [(item,  item) for item in SUITS]

RANKS = [ '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace', 'Joker']
RANK_CHOICES = [(item,  item) for item in RANKS]

ICONS = [ 'diamond', 'favorite', 'spa', 'eco' ]
ICON_CHOICES = [(item,  item) for item in ICONS]

class Card(models.Model):
  rank = models.CharField(
    max_length=10,
    choices=SUIT_CHOICES,
    default=SUIT_CHOICES[0][0],
  )
  suit = models.CharField(
    max_length=8,
    choices=RANK_CHOICES,
    default=RANK_CHOICES[0][0],
  )
  icon = models.CharField(
    max_length=10,
    choices=ICON_CHOICES,
    default=ICON_CHOICES[0][0],
  )

  def get_title(self):
    return f'{self.suit} - {self.rank}'
  
  def __str__(self):
    return self.get_title()


class MenuItem(models.Model):
  icon_name = models.CharField(max_length=100)
  url_name = models.CharField(max_length=100)

class ProgressItem(models.Model):
  label = models.CharField(max_length=100)
  progress_start = models.CharField(max_length=100)
  duration = models.IntegerField()
  type = models.CharField(
    max_length=100,
    choices=ICON_CHOICES,
    default=ICON_CHOICES[0][0],
  )

class AdditionalInfo(models.Model):
  icon = models.CharField(max_length=100)
  icon_color = models.CharField(max_length=100)
  link = models.CharField(max_length=100)
  label = models.CharField(max_length=100)
  value = models.CharField(max_length=100)
