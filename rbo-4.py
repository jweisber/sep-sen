from bg.sim import process
import timeit


s = 20000
grid  = [(s, g, a, 1000, .001, None) for g in ['complete', 'cycle']
                                     for a in range(4, 20, 2)]
grid += [(s, g, a, 1000, .001, None) for g in ['complete', 'cycle']
                                     for a in range(20, 101, 5)]

tic = timeit.default_timer()
process(grid, 'results/rbo-fig-4.csv')
toc = timeit.default_timer()

print("Time: " + str(round(toc - tic, 1)))