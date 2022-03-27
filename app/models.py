import email
from enum import Enum
from django.db import models

# Assuming Person lives in AUS
class StatesEnum(Enum):

  NSW = 'New South Wales'
  VIC = 'Victoria'
  QLD = 'Queensland'
  SA = 'South Australia'
  WA = 'Western Australia'
  TAS = 'Tasmania'
  NT = 'Northern Territory'
  ACT = 'Australian Capital Territory'

  def __str__(self):
    return self.name

  @classmethod
  def choices(cls):
    return [(key.name, key.value) for key in cls] 

class Address(models.Model):
  number = models.IntegerField()
  street = models.CharField(max_length=250)
  city = models.CharField(max_length=250)
  state = models.CharField(choices=StatesEnum.choices(), default=None, max_length=100)

  def __str__(self):
      return "{} {}, {}, {}".format(self.number, self.street, self.city, self.state)

class Person(models.Model):
  email = models.CharField(max_length=250)
  name = models.CharField(max_length=250)
  address = models.ForeignKey(Address, on_delete=models.CASCADE)

  def __str__(self) -> str:
      return self.name
