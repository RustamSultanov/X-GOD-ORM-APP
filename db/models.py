from peewee import *

db = SqliteDatabase('tourism.db')


class BaseModel(Model):
    class Meta:
        database = db


class Tour(BaseModel):
    name = CharField()
    date = DateField()
    duration = IntegerField()


class Tourist(BaseModel):
    name = CharField()
    age = SmallIntegerField()
    tour = ForeignKeyField(Tour, backref='tourists')


class Vehicle(BaseModel):
    type = CharField()
    capacity = IntegerField()
    resort = DeferredForeignKey('Resort', backref='vehicles')


class Resort(BaseModel):
    name = CharField()
    coordinate = CharField()
    tour = ForeignKeyField(Tour, backref='resorts')
    vehicles = ForeignKeyField(Vehicle, backref='resorts')


class Sight(BaseModel):
    name = CharField()
    resort = ForeignKeyField(Resort, backref='sights')


class Residence(BaseModel):
    type = CharField()
    price = IntegerField()
    resort = ForeignKeyField(Resort, backref='residences')
