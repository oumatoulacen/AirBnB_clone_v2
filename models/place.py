#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base

from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

import os

env_value = os.environ.get("HBNB_TYPE_STORAGE")

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    if env_value == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place")
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            back_populates="place_amenities",
            viewonly=False,
        )

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            from models.__init__ import storage
            from models.amenity import Review

            obj_list = []
            strg = storage.all(Review)
            for value in strg:
                if self.id == value.id:
                    obj_list.append(value)
            return obj_list

        @property
        def amenities(self):
            from models.__init__ import storage
            from models.amenity import Amenity

            obj_list = []
            strg = storage.all(Amenity)
            for value in strg:
                if self.id == value.id:
                    obj_list.append(value)
            return obj_list

        @amenities.setter
        def amenities(self, obj):
            from models.__init__ import storage
            from models.amenity import Amenity

            if isinstance(obj, storage.all(Amenity)):
                self.amenity_ids.append(obj.id)
