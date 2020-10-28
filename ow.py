from bg.sim import process, record
import timeit


s = 10000
grid = [(s, 'complete', a, 50, .2, m) for a in [2, 6, 10, 20]
                                      for m in [1, 1.1, 1.5, 2, 2.5]]

tic = timeit.default_timer()
process(grid, 'results/ow.csv')
toc = timeit.default_timer()

print("Time: " + str(round(toc - tic, 1)))