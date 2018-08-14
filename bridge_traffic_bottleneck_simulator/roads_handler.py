import sys
from road import Road
from random import randrange
from car import Car


def beautify_print(arr, car_delimiter='car', empty_delimiter='---', is_end_line=False):
    sys.stdout.write('[')
    for i, cell in enumerate(arr):
        if cell is not None:
            sys.stdout.write(car_delimiter)
        else:
            sys.stdout.write(empty_delimiter)
        if i != len(arr) - 1:
            sys.stdout.write(',')

    sys.stdout.write(']')
    if is_end_line:
        sys.stdout.write('\n')

    sys.stdout.flush()


class RoadsHandler:
    roads = []
    bridge = None
    state = []
    num_of_roads = 0

    def __init__(self, _num_of_roads, size_of_road, size_of_bridge):
        if _num_of_roads < 4:
            self.num_of_roads = 4
        if _num_of_roads % 2 == 1:
            self.num_of_roads += 1
        else:
            self.num_of_roads = _num_of_roads
        self.roads = [None] * self.num_of_roads
        # self.roads = [Road(size_of_road)] * self.num_of_roads
        for i in range(self.num_of_roads):
            self.roads[i] = Road(size_of_road)
        self.bridge = Road(size_of_bridge)
        self.state = []

    def save_end_state(self):
        self.state = []
        for i, road in enumerate(self.roads):
            road_state = road.get_road_cell(road.road_size - 1)
            if road_state is not None:
                self.state.append(i)

    def move_from_road(self, road_number):
        self.roads[road_number].road[self.roads[road_number].road_size - 1] = None
        self.bridge.road[0] = Car()
        self.bridge.road[0].is_new = False
        self.bridge.road[0].is_moved = True

    def get_road_to_move(self):
        return self.state[randrange(0, len(self.state))]

    def move_to_bridge(self):
        if self.bridge.get_road_cell(0) is None and len(self.state) > 0:
            self.move_from_road(self.get_road_to_move())

    def save_start_roads_state(self):
        self.state = []
        if self.bridge.road[len(self.bridge.road) - 1] is not None:
            for i, road in enumerate(self.roads):
                if i <= (self.num_of_roads / 2 - 1):
                    continue
                if road.road[0] is None:
                    self.state.append(i)

    def move_from_bridge(self):
        if self.state is not None and len(self.state) > 0:
            if self.bridge.get_road_cell(self.bridge.road_size - 1) is not None:
                if not self.bridge.get_road_cell(self.bridge.road_size - 1).is_moved:
                    self.bridge.road[self.bridge.road_size - 1] = None
                    road_to_move = self.get_road_to_move()
                    self.roads[road_to_move].road[0] = Car()
                    self.roads[road_to_move].road[0].is_new = False
                    self.roads[road_to_move].road[0].is_moved = True
                else:
                    self.bridge.road[self.bridge.road_size - 1].is_moved = False

    round = 1

    def manage_simulation(self, T, t0):
        local_T = T
        while local_T > 0:
            self.round += 1
            local_T -= 1

            for i, road in enumerate(self.roads):
                if i > (self.num_of_roads / 2 - 1):
                    break
                road.try_add_car()

            self.save_end_state()

            for i, road in enumerate(self.roads):
                if i > (self.num_of_roads / 2 - 1):
                    break
                road.move_cars()

            self.move_to_bridge()
            self.bridge.move_cars()
            self.save_start_roads_state()

            for i, road in enumerate(self.roads):
                if i <= (self.num_of_roads / 2 - 1):
                    continue

                road.move_cars()
                if road.road[road.road_size - 1] is not None and not road.road[road.road_size - 1].is_moved:
                    if self.roads[i % (self.num_of_roads / 2)].road[0] is None:
                        if (self.roads[i % (self.num_of_roads / 2)].road[1] is None) or (
                                        self.roads[i % (self.num_of_roads / 2)].road[1] is not None
                                and not self.roads[i % (self.num_of_roads / 2)].road[1].is_moved):
                            road.road[road.road_size - 1] = None
                            self.roads[i % (self.num_of_roads / 2)].road[0] = Car()
                            self.roads[i % (self.num_of_roads / 2)].road[0].is_moved = True
                    else:
                        #self.roads[i % (self.num_of_roads / 2)].generate = False
                        road.road[road.road_size - 1].is_moved = False
            # self.print_roads()
            self.move_from_bridge()

            if self.round > t0:
                for road in self.roads:
                    road.collect_statistical_data()
                self.bridge.collect_statistical_data()

            for road in self.roads:
                for car in road.road:
                    if car is not None:
                        car.is_moved = False

            for car in self.bridge.road:
                if car is not None:
                    car.is_moved = False
            #self.print_roads()

    def print_roads(self):
        sys.stdout.write('\n----------------------------------------------------------------------------\n')
        beautify_print(self.roads[0].road)
        beautify_print(self.bridge.road, 'XXX', 'XXX')
        beautify_print(self.roads[2].road, is_end_line=True)

        beautify_print(self.roads[0].road, 'XXX', 'XXX')
        beautify_print(self.bridge.road)
        beautify_print(self.roads[0].road, 'XXX', 'XXX', True)

        beautify_print(self.roads[1].road)
        beautify_print(self.bridge.road, 'XXX', 'XXX')
        beautify_print(self.roads[3].road, is_end_line=True)
        sys.stdout.write('----------------------------------------------------------------------------\n')
        sys.stdout.flush()
