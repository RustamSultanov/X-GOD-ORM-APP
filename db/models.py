from peewee import *

db = SqliteDatabase('tourism.db')


class Tour(Model):
    name = CharField()
    date = DateField()
    duration = IntegerField()

    class Meta:
        database = db


class Tourist(Model):
    name = CharField()
    age = SmallIntegerField()
    tour = ForeignKeyField(Tour, backref='tourists')

    class Meta:
        database = db


class Transport(Model):
    kind = CharField()
    capacity = IntegerField()

    class Meta:
        database = db


class Resort(Model):
    name = CharField()
    coordinate = CharField()
    tour = ForeignKeyField(Tour, backref='resorts')
    transport = ManyToManyField(Transport)

    class Meta:
        database = db


class Showplace(Model):
    name = CharField()
    resort = ForeignKeyField(Resort, backref='showplaces')

    class Meta:
        database = db


class Residence(Model):
    kind = CharField()
    price = IntegerField()
    resort = ForeignKeyField(Resort, backref='showplaces')

    class Meta:
        database = db
