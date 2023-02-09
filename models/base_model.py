#!/usr/bin/python3



from uuid import uuid4()
from datetime import datetime
import uuid


date_format = "Y-%m-%dT%H:%M:%S.%f "


  class BaseModel():
      """ This call defines common attributes and methods as follow """
      def __init__(self, *args, **kwargs):

          self.id = str(uuid.uuid4())
          self.created_at = datetime.now()
          self.updated_at = datetime.now()

          if kwargs:
              for key, value in kwargs.item():
                  if key == "create_at":
                      date = value[0:10] + " " + value[11:]
                      self.created_at = datetime.strptime(date, date_format)
                  elif key == "updated_at":
                       date = value[0:10] + " " + value[11:]
                       self.updated_at = datetime.strptime(date, date_format)
                   
                  elif key != "__class__":
                      setattr(self, key, value)



      def __str__(self):
          """string represtattion of the object"""
          return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dic__)
      
      def save(self):
          """ updates the updated_at attribute with the current datetime """
          self.updated_at = datetime.now()

      def to_dic(self):
          """ returns a dictionary containing all keys/values of __dict__ of the instance """
          new_dict = dict(self.__dict__)
          new_dict['__class__'] = self.__class__.__name__
          new_dict['created_at'] = self.created_at.isoformat()
          new_dict['updated_at'] = self.updated_at.isoformat()
          return new_dic
