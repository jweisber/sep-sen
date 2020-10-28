from bg.sim import process
import timeit


s = 10000
grid  = [(s, 'complete', a, 1000, .001, None) for a in range(3, 11)]
grid += [(s, 'cycle',    a, 1000, .001, None) for a in range(4, 11)]
grid += [(s, 'wheel',    a, 1000, .001, None) for a in range(5, 11)]

tic = timeit.default_timer()
process(grid, 'results/zollman.csv')
toc = timeit.default_timer()

print("Time: " + str(round(toc - tic, 1)))