# -*- coding: utf-8 -*-
import datetime

from db.models import db, Tour, Tourist, Vehicle, Resort, Sight, Residence, ResortVehicle


def fill():

    with db:
        db.create_tables([Tour, Tourist, Vehicle, Resort, Sight, Residence, ResortVehicle])

    vehicle1 = Vehicle.create(
        type='Sedan',
        capacity=4,
    )

    vehicle2 = Vehicle.create(
        type='Minivan',
        capacity=6,
    )

    vehicle3 = Vehicle.create(
        type='Coupe',
        capacity=2,
    )
    vehicles = [vehicle1, vehicle2, vehicle3]

    tour1 = Tour.create(
        name='Ларнака',
        date=datetime.date(2020, 7, 18),
        duration=21,
    )

    tourist1_1 = Tourist.create(
        name='Иванов Василий Петрович',
        age=21,
        tour=tour1,
    )

    tourist1_2 = Tourist.create(
        name='Сидорова Ольга Владиславовна',
        age=35,
        tour=tour1,
    )

    resort1_1 = Resort.create(
        name='Айя-Напа',
        coordinate='34°59′ с.ш. 34°00′ в.д.',
        tour=tour1,
    )

    sight1_1_1 = Sight.create(
        name='Ayia Napa Square',
        resort=resort1_1,
    )

    sight1_1_2 = Sight.create(
        name='Love Bridge',
        resort=resort1_1,
    )

    residence1_1_1 = Residence.create(
        type='Бунгало',
        price=80000,
        resort=resort1_1,
    )

    residence1_1_2 = Residence.create(
        type='Номер в отеле',
        price=8000,
        resort=resort1_1,
    )

    resort1_2 = Resort.create(
        name='Протарас',
        coordinate='35°01′ с.ш. 34°03′ в.д.',
        tour=tour1,
    )

    sight1_2_1 = Sight.create(
        name='Церковь Пророка Ильи',
        resort=resort1_2,
    )

    sight1_2_2 = Sight.create(
        name='Залив Фигового дерева',
        resort=resort1_2,
    )

    residence1_2_1 = Residence.create(
        type='Вилла',
        price=200000,
        resort=resort1_2,
    )

    residence1_2_2 = Residence.create(
        type='Номер в отеле',
        price=12000,
        resort=resort1_2,
    )

    resort1_3 = Resort.create(
        name='Никосия',
        coordinate='35°10′ с.ш. 33°22′ в.д.',
        tour=tour1,
    )

    sight1_3_1 = Sight.create(
        name='Buyuk Han',
        resort=resort1_3,
    )

    sight1_3_2 = Sight.create(
        name='Paphos Gate',
        resort=resort1_3,
    )

    residence1_3_1 = Residence.create(
        type='Бунгало',
        price=100000,
        resort=resort1_3,
    )

    residence1_3_2 = Residence.create(
        type='Номер в отеле',
        price=10000,
        resort=resort1_3,
    )

    tour2 = Tour.create(
        name='Таиланд',
        date=datetime.date(2020, 8, 19),
        duration=8,
    )

    tourist2_1 = Tourist.create(
        name='Орлова Елизавета Андреевна',
        age=25,
        tour=tour2,
    )

    tourist2_2 = Tourist.create(
        name='Дощечкин Виталий Дмитриевич',
        age=45,
        tour=tour2,
    )

    tourist2_3 = Tourist.create(
        name='Бессмертный Игорь Степанович',
        age=18,
        tour=tour2,
    )

    resort2_1 = Resort.create(
        name='Остров Пхукет',
        coordinate='7°53′ с.ш. 98°23′ в.д.',
        tour=tour2,
    )

    sight2_1_1 = Sight.create(
        name='Old Phuket Town',
        resort=resort2_1,
    )

    sight2_1_2 = Sight.create(
        name='Banana beach',
        resort=resort2_1,
    )

    residence2_1_1 = Residence.create(
        type='Номер в отеле',
        price=9000,
        resort=resort2_1,
    )

    resort2_2 = Resort.create(
        name='Паттайя',
        coordinate='12°55′ с.ш. 100°52′ в.д.',
        tour=tour2,
    )

    sight2_2_1 = Sight.create(
        name='Храм Истины',
        resort=resort2_2,
    )

    sight2_2_2 = Sight.create(
        name='Pattaya Hill Top',
        resort=resort2_2,
    )

    residence2_1_2 = Residence.create(
        type='Номер в отеле',
        price=9500,
        resort=resort2_2,
    )

    residence2_1_2 = Residence.create(
        type='Вилла',
        price=29500,
        resort=resort2_2,
    )

    resorts = [resort1_1, resort1_2, resort1_3, resort2_1, resort2_2]

    for vehicle in vehicles:
        for resort in resorts:
            ResortVehicle.create(
                resort=resort,
                vehicle=vehicle,
            )
