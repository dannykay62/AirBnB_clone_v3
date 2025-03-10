#!/usr/bin/python3
"""
Contains the class DBStorage
"""

import models
from models.amenity import Amenity
from models.bas_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"Amenity": Amenity, "City": City,
        "Place": Place, "Review": Review, "State": State, "User": User}


Class DBStorage:
    """Interacts with MySQL datbase"""
    ___engine = None
    ___session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV= getenv('HBNB_ENV')
        sel.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                format(HBNB_MYSQL_USER,
                    HBNB_MYSQL_PWD,
                    HBNB_MYSQL_HOST,
                    HBBNB_MYSQL_DB))
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query on the current datbase session"""
        new_dict {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obi)

    def save(self):
        """commit all changes of the current database session"""
        self.session.commit()

    def delete(self, obj=None):
        """Delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def count(self, cls=None):
        """Returns the number of objects in storage matching the given class. 
        If no class is passed, returns the count of all objects in storage."""
        if cls is None:
            return len(models.storage.all())
        return len(models.storage.all(cls))

    def get(self, cls, id):
        """Returns the object based on the class and its ID,
        or None if not found"""
        if id is None or cls is None:
            return None
        if type(cls) is str:
            if cls not in classes:
                return None
            cls = classes[cls]
        save = models.storage.all(cls)
        return save.get("{}.{}".format(cls.__name__, id))