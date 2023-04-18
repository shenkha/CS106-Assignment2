from ortools.algorithms import pywrapknapsack_solver
import timeit 
from test_loader import *
def main():
    # Create the solver.
    file_path = "kplib/00Uncorrelated/n00500/R01000/s000.kp"
    n, c,values,weights = read_kp_file(file_path)
    nhom,soluong,giatri,ten = extract_keyword(file_path)
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')
    time_limit = 180
    solver.set_time_limit(time_limit)
    #values = [
    #    360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147,
    #    78, 256, 63, 17, 120, 164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28,
    #    87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274, 43, 33, 10, 19, 389, 276,
    #    312
    #]
    #weights = [[
    #    7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0,
    #    42, 47, 52, 32, 26, 48, 55, 6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71,
    #    3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13
    #]]
    weights = [weights]
    capacities = [c]
    #print(values)
    solver.Init(values, weights, capacities)
    start_time = timeit.timeit()
    computed_value = solver.Solve()
    #print(time_end,start_time)
    duration = abs((timeit.timeit() - start_time))*1000
    if time_limit*1000 > duration:
        isOptimal = True
    else:
        isOptimal = False
    packed_items = []
    packed_weights = []
    total_weight = 0
    print('Total value =', computed_value)
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            packed_items.append(i)
            packed_weights.append(weights[0][i])
            total_weight += weights[0][i]
    print('Total weight:', total_weight)
    print('Packed items:', packed_items)
    print('Packed_weights:', packed_weights)
    print('Run time:',duration)
    #with open("results/" + nhom  + ".csv","a") as file:
    #    file.writelines( str(soluong +'/'+ giatri + '/' + ten) + ", " + str(total_weight) + ", " + str(computed_value) + ", "+ str(duration) + ", " + str(isOptimal) + "\n")
if __name__ == '__main__':
    main()