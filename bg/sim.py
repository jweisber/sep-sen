import csv
import os.path
from multiprocessing import Pool
from bg.graph import Graph

def process(grid, path):
    for params in grid:
        print(params)
        n_simulations, graph, a, n, e, m = params
        pool = Pool()
        results = pool.starmap(run_simulation, ((graph, a, n, e, m),) * n_simulations)
        pool.close()
        pool.join()
        record(results, path)

def run_simulation(graph, a, n, e, m):
    g = Graph(a, graph)
    g.run_simulation(n, e, m)
    return [graph, a, g.epoch, g.conclusion, n, e, m]

def record(results, path):
    file_exists = os.path.isfile(path)
    with open(path, mode = 'a') as csv_file:
        writer = csv.writer(csv_file)
        if not file_exists:
            writer.writerow(['graph', 'agents', 'epochs', 'conclusion', 'trials', 'epsilon', 'mistrust'])
        writer.writerows(results)