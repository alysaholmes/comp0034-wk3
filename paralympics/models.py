# Adapted from https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/quickstart/#define-models
from typing import List
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from paralympics import db


# This uses the latest syntax for SQLAlchemy, older tutorials will show different syntax
# SQLAlchemy provide an __init__ method for each model, so you do not need to declare this in your code
class Region(db.Model):
    __tablename__ = "region"
    NOC: Mapped[str] = mapped_column(db.Text, primary_key=True)
    region: Mapped[str] = mapped_column(db.Text, nullable=False)
    notes: Mapped[str] = mapped_column(db.Text, nullable=True)
    # one-to-many relationship with Event, the relationship in Event is called 'region'
    # https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-many
    events: Mapped[List["Event"]] = relationship(back_populates="region")


class Event(db.Model):
    __tablename__ = "event"
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    type: Mapped[str] = mapped_column(db.Text, nullable=False)
    year: Mapped[int] = mapped_column(db.Integer, nullable=False)
    country: Mapped[str] = mapped_column(db.Text, nullable=False)
    host: Mapped[str] = mapped_column(db.Text, nullable=False)
    # add ForeignKey to mapped_column(String, primary_key=True)
    NOC: Mapped[str] = mapped_column(ForeignKey("region.NOC"))
    # add relationship to the parent table, Region, which has a relationship called 'events'
    region: Mapped["Region"] = relationship(back_populates="events")
    start: Mapped[str] = mapped_column(db.Text, nullable=True)
    end: Mapped[str] = mapped_column(db.Text, nullable=True)
    duration: Mapped[int] = mapped_column(db.Integer, nullable=True)
    disabilities_included: Mapped[str] = mapped_column(db.Text, nullable=True)
    countries: Mapped[str] = mapped_column(db.Text, nullable=True)
    events: Mapped[int] = mapped_column(db.Integer, nullable=True)
    athletes: Mapped[int] = mapped_column(db.Integer, nullable=True)
    sports: Mapped[int] = mapped_column(db.Integer, nullable=True)
    participants_m: Mapped[int] = mapped_column(db.Integer, nullable=True)
    participants_f: Mapped[int] = mapped_column(db.Integer, nullable=True)
    participants: Mapped[int] = mapped_column(db.Integer, nullable=True)
    highlights: Mapped[str] = mapped_column(db.String, nullable=True)


class User(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    email: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)

def to_json(self):
        return json.dumps(self.__dict__)


# To use, create a User object by querying the database for the user with the id 1, serialise using to_json and then print the result
user = db.session.execute(db.select(User).order_by(User.username)).scalars()
user_json = user.to_json()
print(user_json)

class Region(db.Model):
    __tablename__ = "region"
    # Primary key attribute
    NOC: Mapped[str] = mapped_column(db.Text, primary_key=True)
    # Add a relationship to Event. The Region then has a record of the Events associated with it. 
    # This references the relationship 'region' in the Event table.
    events: Mapped[List["Event"]] = relationship(back_populates="region")


class Event(db.Model):
    __tablename__ = "event"
    # add ForeignKey that maps to the primary key of the Region table
    NOC: Mapped[str] = mapped_column(ForeignKey("region.NOC"))
    # add relationship to Region, this references the relationship 'events' that is in the Region table
    region: Mapped["Region"] = relationship(back_populates="events")

    