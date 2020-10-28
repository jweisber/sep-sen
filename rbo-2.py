from bg.sim import process
import timeit


s = 50000
grid  = [(s, g, 10, 1000, .001, None)     for g in ['complete', 'cycle']]
grid += [(s, g, 10, 1000, i / 1000, None) for g in ['complete', 'cycle']
                                          for i in range(2, 11, 2)]
grid += [(s, g, 10, 1000, i / 1000, None) for g in ['complete', 'cycle']
                                          for i in range(15, 101, 5)]

tic = timeit.default_timer()
process(grid, 'results/rbo-fig-2.csv')
toc = timeit.default_timer()

print("Time: " + str(round(toc - tic, 1)))