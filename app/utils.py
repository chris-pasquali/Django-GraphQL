import random
from .models import Person

"""
This function will check if there are multiple entries in the database
If so it will get a random person's id otherwise it will get the first user's id
"""
def get_random_user():
  all_people = Person.objects.all()

  if len(all_people) > 1:
    random_person = random.choice(all_people)
    user_id = random_person.id
  else:
    user_id = (Person.objects.get()).id
  
  return user_id
