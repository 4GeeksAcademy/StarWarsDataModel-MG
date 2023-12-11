import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'planet'
    planet_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True ,nullable=False)
    population = Column(Integer)
    terrain = Column(String(50))
    climate = Column(String(50))

class Character(Base):
    __tablename__ = 'character'
    character_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True,nullable=False)
    height = Column(Float)
    mass = Column(Float)
    birth_year = Column(String(10))
    homeworld_id = Column(Integer, ForeignKey('planet.planet_id'))
    homeworld = relationship('Planet')

class Starship(Base):
    __tablename__ = 'starship'
    starship_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    model = Column(String(50), nullable=False)
    starship_type = Column(String(250))
    pilot_id = Column(Integer, ForeignKey('character.character_id'))
    pilot = relationship('Character')

class Vehicle(Base):
    __tablename__ = 'vehicle'
    vehicle_id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    model = Column(String(50), nullable=False)
    vehicle_type = Column(String(50))
    pilot_id = Column(Integer, ForeignKey('character.character_id'))
    pilot = relationship('Character')

class FilmData(Base):
    __tablename__ = 'film_data'
    film_data_id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.character_id'))
    character = relationship('Character')
    planet_id = Column(Integer, ForeignKey('planet.planet_id'))
    planet = relationship('Planet')
    starship_id = Column(Integer, ForeignKey('starship.starship_id'))
    starship = relationship('Starship')
    vehicle_id = Column(Integer, ForeignKey('vehicle.vehicle_id'))
    vehicle = relationship('Vehicle')

class Film(Base):
    __tablename__ = 'film'
    film_id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    film_data_id = Column(Integer, ForeignKey('film_data.film_data_id'))
    film_data = relationship('FilmData')

class Favorite(Base):
    __tablename__ = 'favorite'
    favorite_id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.character_id'))
    character = relationship('Character')
    planet_id = Column(Integer, ForeignKey('planet.planet_id'))
    planet = relationship('Planet')
    starship_id = Column(Integer, ForeignKey('starship.starship_id'))
    starship = relationship('Starship')
    vehicle_id = Column(Integer, ForeignKey('vehicle.vehicle_id'))
    vehicle = relationship('Vehicle')
    film_id = Column(Integer, ForeignKey('film.film_id'))
    film = relationship('Film')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
