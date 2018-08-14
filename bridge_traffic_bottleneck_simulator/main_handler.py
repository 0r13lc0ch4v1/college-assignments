import matplotlib.pyplot as plt
from roads_handler import RoadsHandler

def analyse_data(roadsHandler):
    roads_pvj = []
    bridge_pvj = []

    for k in range(len(roadsHandler.roads) + 1):
        if k != len(roadsHandler.roads):
            _round = roadsHandler.roads[k]
        else:
            _round = roadsHandler.bridge

        p = []
        v = []
        j = []

        avg_p = 0
        avg_v = 0
        avg_j = 0

        for i in range(len(_round.num_of_cars)):
            p_temp = float(_round.num_of_cars[i]) / _round.road_size
            p.append(p_temp)
            v_temp = 0
            if _round.num_of_cars[i] != 0:
                v_temp = float(_round.num_of_moved_cars[i]) / _round.num_of_cars[i]
                v.append(v_temp)
            else:
                v.append(0)
            j_temp = p_temp * v_temp
            j.append(j_temp)

        for tik in p:
            avg_p += tik
        avg_p /= len(_round.num_of_cars)

        for tik in v:
            avg_v += tik
        avg_v /= len(_round.num_of_cars)

        avg_j = avg_p * avg_v

        # plt.plot(range(len(p)), p)
        s = []
        for i in range(len(p)):
            s.append(float(i) / float((len(p))))

        plt.plot(s, p, 'r', s, v, 'b', s, j, 'g')
        if k != len(roadsHandler.roads):
            plt.title("Road " + str(k + 1))
            roads_pvj.append([p, v, j])
        else:
            plt.title("Bridge")
            bridge_pvj = [p, v, j]

        plt.show()

    s = []
    for i in range(len(p)):
        s.append(float(i) / float((len(p))))
    plt.plot(s, roads_pvj[0][2], 'r', s, bridge_pvj[2], 'b', s, roads_pvj[3][2], 'g')
    plt.title("flow in Road1, Bridge, Road 4")
    plt.show()

    plt.plot(s, roads_pvj[0][1], 'r')
    plt.title("Road 1 Velocity")
    plt.show()

    plt.plot(s, roads_pvj[0][0], 'r')
    plt.title("Road 1 Density")
    plt.show()

def run_simulation(num_of_roads, size_of_road, size_of_bridge, T, t0):
    roadsHandler = RoadsHandler(num_of_roads, size_of_road, size_of_bridge)
    roadsHandler.manage_simulation(T, t0)
    analyse_data(roadsHandler)


