from main_handler import run_simulation
from random import randrange

# binomial distribution
def zero_or_one_distribution():
    # n - number of trials
    n = 1000
    # size - number of testes
    size = 10000
    arr = []
    tmp = []
    for _ in range(size):
        for _ in range(n):
            arr.append(randrange(0, 2))
        tmp.append(sum(arr))
        arr = []
    # return the binomial distribution
    return (sum(tmp)/float(len(tmp))/n)*100

def chi_square():
    arr = [0, 0]
    repeat = 10000
    for _ in range(repeat):
        if randrange(0, 2) == 1:
            arr[1] += 1
        else:
            arr[0] += 1

    arr[0] = (arr[0]/float(repeat))*100
    arr[1] = (arr[1] / float(repeat)) * 100

    x0 = pow(50 - arr[0],2)/arr[0]
    x1 = pow(50 - arr[1],2)/arr[1]
    x = x0+x1
    print x

# Run the simulation

num_of_roads = 6
size_of_road = 1000
size_of_bridge = 100
T = 10000
t0 = 0

run_simulation(num_of_roads, size_of_road, size_of_bridge, T, t0)
#chi_square()