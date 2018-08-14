from car import Car
from random import randrange


def yes_or_no():
    if randrange(0, 2):
        return True
    else:
        return False


class Road:

    def __init__(self, _road_size):
        self.road = [None] * _road_size
        self.road_size = _road_size
        self.num_of_cars = []
        self.num_of_moved_cars = []
        self.generate = True
        self.generated_cars = 0

    def is_road_available(self):
        if self.road[0] is None:
            return True
        else:
            return False

    def try_add_car(self):
        if self.generate is True and self.generated_cars < float('inf'):
            if self.generate is True:
                if yes_or_no() is True:
                    if self.road[0] is None:
                        self.road[0] = Car()
                        self.generated_cars += 1
                        return True
                    else:
                        return False
                else:
                    return True
            return False

    def move_cars(self):
        iterable = enumerate(self.road)
        for i, car in iterable:
            if car is not None:
                if i == 0 and car.is_new is True:
                    car.is_new = False
                    continue

                if i < self.road_size - 1 and self.road[i + 1] is None and self.road[i].is_moved is False:
                    self.road[i] = None
                    self.road[i + 1] = Car()
                    self.road[i + 1].is_moved = True
                    iterable.next()

    def get_road_cell(self, cell_num):
        return self.road[cell_num]

    def collect_statistical_data(self):
        _num_of_cars = 0
        _num_of_moved_cars = 0
        for car in self.road:
            if car is not None:
                _num_of_cars += 1
                if car.is_moved is True:
                    _num_of_moved_cars += 1
                    car.is_moved = False
        self.num_of_cars.append(_num_of_cars)
        self.num_of_moved_cars.append(_num_of_moved_cars)
