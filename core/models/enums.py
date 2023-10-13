from enum import Enum

class Status(Enum):
  """Except 1, all odd enums are describing failed attempts, and all even enums are describing successful attempts"""
  STARTED = 1
  ACCEPTED_TERMS = 2
  LOGIN_FAILED = 3
  SUCCESSFULLY_LOGGED = 4
  ORDER_NOT_FOUND = 5
  ORDER_FOUND = 6
  TRACK_STATUS_NOT_FOUND = 7
  TRACK_STATUS_SENT = 8
  
class Platform(Enum):
  SHOPEE = 1
  AMAZON = 2