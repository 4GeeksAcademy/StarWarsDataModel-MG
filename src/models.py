import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True ,nullable=False)
    population = Column(Integer)
    terrain = Column(String(50))
    climate = Column(String(50))

class character(Base):
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True,nullable=False)
    height = Column(Float)
    mass = Column(Float)
    birth_year = Column(String(10))
    homeworld_id = Column(Integer, ForeignKey(planet.planet_id))
    homeworld_id = relationship(planet)

class starship(Base):
    __tablename__ = 'starship'
    starship_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    model = Column(String(50), nullable=False)
    type = Column(String(250))
    pilot_id = Column(Integer, ForeignKey(character.character_id))
    pilot_id = relationship(character)

class vehicle(Base):
    __tablename__ = 'vehicle'
    vehicle_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    model = Column(String(50), nullable=False)
    type = Column(String(50))
    pilot_id = Column(Integer, ForeignKey(character.character_id))
    pilot_id = relationship(character)

class film_data(Base):
    __tablename__ = 'film_data'
    film_data_id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey(character.character_id))
    character_id = relationship(character)
    planet_id = Column(Integer, ForeignKey(planet.planet_id))
    planet_id = relationship(planet)
    starship_id = Column(Integer, ForeignKey(starship.starship_id))
    starship_id = relationship(starship)
    vehicle_id = Column(Integer, ForeignKey(vehicle.vehicle_id))
    V = relationship(vehicle)

class film(Base):
    __tablename__ = 'film'
    film_id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    film_data_id = Column(Integer, ForeignKey(film_data.film_data_id))
    film_data_id = relationship(film_data)

class Favorite(Base):
    __tablename__ = 'Favorite'
    FavoriteID = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey(character.character_id))
    character_id = relationship(character)
    planet_id = Column(Integer, ForeignKey(planet.planet_id))
    planet_id = relationship(planet)
    starship_id = Column(Integer, ForeignKey(starship.starship_id))
    starship_id = relationship(starship)
    vehicle_id = Column(Integer, ForeignKey(vehicle.vehicle_id))
    vehicle_id = relationship(vehicle)
    film_id = Column(Integer, ForeignKey(film.film_id))
    film_id = relationship(film)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
