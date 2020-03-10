# -*- coding: utf-8 -*-
#             *     ,MMM8&&&.            *
#                  MMMM88&&&&&    .
#                 MMMM88&&&&&&&
#     *           MMM88&&&&&&&&
#                 MMM88&&&&&&&&
#                 'MMM88&&&&&&'
#                   'MMM8&&&'      *
#          |\___/|
#          )     (             .              '
#         =\     /=
#           )===(       *
#          /     \
#          |     |
#         /       \
#         \       /
#  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
#  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
#  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
#  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
#  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
#  |  |   Magic cat pls save from bugs!   |  |
#  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
import datetime

from db.filler import fill
from db.models import Resort, Residence, Vehicle, Tour, ResortVehicle, Sight, Tourist


def query1(residence_name):
    return (Resort.
            select(Resort.name).
            join(Residence).
            where(Residence.type == residence_name))


def query2(date):
    return (Vehicle.
            select(Vehicle.type, Vehicle.capacity).
            join(ResortVehicle).
            join(Resort).
            join(Tour).
            where(Tour.date > date).
            distinct().
            order_by(Vehicle.capacity.desc()))


def query3(age, duration):
    return (Sight.
            select(Sight.name, Resort.coordinate).
            join(Resort).
            join(Tour).
            join(Tourist).
            where((Tourist.age > age) & (Tour.duration < duration)).
            distinct())


# fill()


query = query1('Вилла')
for resort in query:
    print(resort.name)

# query = query2(datetime.date(2020, 5, 19))
# for vehicle in query:
#     print(vehicle.type, vehicle.capacity)

# query = query3(21, 15)
# for result in query.namedtuples():
#     print(result.name, result.coordinate)
