from ortools.algorithms import pywrapknapsack_solver
import time
from test_loader import *

def main():
    with open("results/" + "results.csv","a") as f:
        f.write("type, size, range, name, total_value, total_weight, duration, isOptimal\n")
    f.close()
    file_path = "test_case"
    test = test_loader(file_path)
    # Create the solver.
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.
        KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER, 'KnapsackExample')

    time_limit = 60
    solver.set_time_limit(time_limit)
    
    for t in test.load_types():
        test.set_type(t)
        for s in test.load_sizes():
            test.set_size(s)
            for r in test.load_ranges():
                test.set_range(r)
                for i in test.load_tests():
                    test.set_test(i)
                    n,c,values,weights = test.read_kp_file()
                    capacities = [c]
                    print(test.get_type()," ",test.get_size()," ",test.get_range()," ",test.get_test())
                    solver.Init(values, weights, capacities)
                    start_time = time.time()
                    computed_value = solver.Solve()
                    duration = abs((time.time() - start_time))
                    if time_limit > duration + 1:
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
                    print('Duration:',duration)
                    print('Is Optimal:',isOptimal)
                    info = test.get_all_info()
                    with open("results/" + "results.csv","a") as f:
                        f.write(str(test.get_type()) + ", " + str(test.get_size()) + ", " + str(test.get_range()) + ", " + str(test.get_test()) + ", " + str(computed_value) + ", " + str(total_weight) + ", " + str(duration) + ", " + str(isOptimal) + "\n" )
                    f.close()

                    txt_path = "results/items/" + str(info['type']) + ".txt"
                    with open(txt_path,"a") as f:
                        f.write(str(info['size']) + "/" + str(info['range']) + "/" + str(info['test']) + "\n")
                        f.write("Number of items:" + str(len(packed_items)) + "\n")

                        f.write("Packed_itmes:" + "\n")
                        for v in packed_items:
                            f.write(str(v) + " ")
                        f.write("\n")

                        f.write("Packed_weights:" + "\n")
                        for w in packed_weights:
                            f.write(str(w) + " ")
                        f.write("\n")

                    f.close()

                    
                    


if __name__ == '__main__':
    main()