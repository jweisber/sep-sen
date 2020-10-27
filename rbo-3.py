from bg.sim import process, record
import timeit


s = 50000
grid  = [(s, g, 10,  10, .01, None) for g in ['complete', 'cycle']]
grid  = [(s, g, 10, 100, .01, None) for g in ['complete', 'cycle']]
grid += [(s, g, 10,   n, .01, None) for g in ['complete', 'cycle']
                                    for n in range(500, 2001, 500)]
grid += [(s, g, 10,   n, .01, None) for g in ['complete', 'cycle']
                                    for n in range(2500, 10001, 500)]

tic = timeit.default_timer()
process(grid, 'analysis/rbo-fig-3.csv')
toc = timeit.default_timer()

print("Time: " + str(round(toc - tic, 1)))