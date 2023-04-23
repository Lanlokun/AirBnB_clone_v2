#!/usr/bin/python3
'''
    Define the class Place.
'''
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                        Column('place_id', String(60),
                                ForeignKey('places.id'),
                                nullable=False),
                        Column('amenity_id', String(60),
                                ForeignKey('amenities.id'),
                                nullable=False))


class Place(BaseModel, Base):
    '''
        Define the class Place that inherits from BaseModel.
    '''
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    
    if storage_type == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete-orphan")
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)


    else:
        @property
        def reviews(self):
            """
            get list of Review instances with
            place_id equals to the current Place.id
            """
            list_reviews = []
            all_reviews = self.reviews
            for review in all_reviews:
                if review.place_id == Place.id:
                    list_reviews.append(review)
            return list_reviews

        @property
        def amenities(self):
            """
            returns the list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the Place
            """
            amenity_objs = []
            for amenity_id in self.amenity_ids:
                key = 'Amenity.' + amenity_id
                if key in FileStorage.__objects:
                    amenity_objs.append(FileStorage.__objects[key])
            return amenity_objs

        @amenities.setter
        def amenities(self, obj):
            """
            adds an Amenity.id to the attribute amenity_ids if obj is
            an instance of Amenity
            """
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)