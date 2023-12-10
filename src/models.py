import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__ = 'Planet'
    PlanetID = Column(Integer, primary_key=True)
    Name = Column(String(50), unique=True ,nullable=False)
    Population = Column(Integer)
    Terrain = Column(String(50))
    Climate = Column(String(50))

class Character(Base):
    __tablename__ = 'Character'
    CharacterID = Column(Integer, primary_key=True)
    Name = Column(String(50), unique=True,nullable=False)
    Height = Column(Float)
    Mass = Column(Float)
    BirthYear = Column(String(10))
    Homeworld = Column(Integer, ForeignKey(Planet.PlanetID))
    Planet = relationship(Planet)

class Starship(Base):
    __tablename__ = 'Starship'
    StarshipID = Column(Integer, primary_key=True)
    Name = Column(String(50), unique=True, nullable=False)
    Model = Column(String(50), nullable=False)
    Type = Column(String(250))
    Pilotid = Column(Integer, ForeignKey(Character.CharacterID))
    C = relationship(Character)

class Vehicle(Base):
    __tablename__ = 'Vehicle'
    VehicleID = Column(Integer, primary_key=True)
    Name = Column(String(50), unique=True, nullable=False)
    Model = Column(String(50), nullable=False)
    Type = Column(String(50))
    PilotID = Column(Integer, ForeignKey(Character.CharacterID))
    C = relationship(Character)

class FilmData(Base):
    __tablename__ = 'FilmData'
    FilmDataID = Column(Integer, primary_key=True)
    CharacterID = Column(Integer, ForeignKey(Character.CharacterID))
    C = relationship(Character)
    PlanetID = Column(Integer, ForeignKey(Planet.PlanetID))
    P = relationship(Planet)
    StarshipID = Column(Integer, ForeignKey(Starship.StarshipID))
    S = relationship(Starship)
    VehicleID = Column(Integer, ForeignKey(Vehicle.VehicleID))
    V = relationship(Vehicle)

class Film(Base):
    __tablename__ = 'Film'
    FilmID = Column(Integer, primary_key=True)
    Title = Column(String(50), unique=True, nullable=False)
    FilmDataID = Column(Integer, ForeignKey(FilmData.FilmDataID))
    FD = relationship(FilmData)

class Favorite(Base):
    __tablename__ = 'Favorite'
    FavoriteID = Column(Integer, primary_key=True)
    CharacterID = Column(Integer, ForeignKey(Character.CharacterID))
    C = relationship(Character)
    PlanetID = Column(Integer, ForeignKey(Planet.PlanetID))
    P = relationship(Planet)
    StarshipID = Column(Integer, ForeignKey(Starship.StarshipID))
    S = relationship(Starship)
    VehicleID = Column(Integer, ForeignKey(Vehicle.VehicleID))
    V = relationship(Vehicle)
    FilmID = Column(Integer, ForeignKey(Film.FilmID))
    F = relationship(Film)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
