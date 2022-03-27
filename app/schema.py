from app.utils import get_random_user
import graphene
from .models import *
from .utils import get_random_user

class StateEnum(graphene.Enum):
  NSW = "New South Wales"
  VIC = "Victoria"
  QLD = "Queensland"
  SA = "South Australia"
  WA = "Western Australia"
  TAS = "Tasmania"
  NT = "Northern Territory"
  ACT = "Australian Capital Territory"
    
class AddressType(graphene.ObjectType):
  number = graphene.Int()
  street = graphene.String()
  city = graphene.String()
  state = graphene.Field(StateEnum)
    

class PersonType(graphene.ObjectType):
  email = graphene.String()
  name = graphene.String()
  address = graphene.Field(AddressType)

class Query(graphene.ObjectType):
  person = graphene.Field(PersonType)

  def resolve_person(self, info, **kwargs):
    user_id = get_random_user()
    person = Person.objects.get(id=user_id)
    return person