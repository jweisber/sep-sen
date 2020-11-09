from bg.sim import process
from bg.graph import Graph
import csv


a, n, epsilon, m = 20, 5, .05, 2
g = Graph(a, "complete")

credences = [[0, i, g.agents[i].credence] for i, a in enumerate(g.agents)]
while(g.undecided() and not g.polarized(m)):
    g.epoch += 1
    g.run_experiments(n, epsilon)
    g.jeffrey_update_agents(epsilon, m)
    credences += [[g.epoch, i, g.agents[i].credence] for i, a in enumerate(g.agents)]

with open('results/ow-animate.csv', mode = 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['epoch', 'agent', 'credence'])
    writer.writerows(credences)

print(g.epoch, g.polarized(m))