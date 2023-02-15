#!usr/bin/python3
import uuid 
from datetime import datetime
from uuid import uuid4
import json
import models
date_format = "%Y-%m-%dT%H:%M:%S.%f"
def __init__(self, *args, **kwargs):
    """initialising"""
    if args is not none and len(args)>0:
        pass
    if kwargs:
        for key, item in kwargs.item():
            if key in ['created_at', 'updated_at']:
                item = datetime.strptime(item, date_format)
            if key not in ['__class__']:
                setattr(self, key, item)
    else:
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        models.storage.new(self)
    def to_dict(self):
        'definition of the to_dic function'
        dic ={}
        for key, item in self.__dict__.items():
            if key in ['created_at', 'updated_at']:
                dic[key] = item
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic

        def save(self):
            """ Save definition """
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()