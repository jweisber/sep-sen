from bg.agent import Agent
import numpy as np

class Graph:
    def __init__(self, a, shape):
        np.random.seed()
        self.agents = [Agent() for i in range(a)]
        self.graph = dict()
        self.epoch = 0

        if shape == "cycle":
            for i in range(a):
                self.graph[self.agents[i]] = [ self.agents[i - 1], self.agents[i], self.agents[(i + 1) % a] ]
        elif shape == "wheel":
            self.graph[self.agents[0]] = self.agents
            for i in range(1, a):
                self.graph[self.agents[i]] = [ self.agents[0], self.agents[i - 1], self.agents[i], self.agents[(i + 1) % a] ]
        elif shape == "complete":
            for i in range(a):
                self.graph[self.agents[i]] = self.agents
    
    def __str__(self):
        return "\n" + "\n".join([str(a) for a in self.agents])

    def run_simulation(self, n, epsilon, m):
        while(self.undecided() and not (m and self.polarized(m))):
            self.epoch += 1
            self.run_experiments(n, epsilon)
            if m:
                self.jeffrey_update_agents(epsilon, m)
            else:
                self.bayes_update_agents(epsilon)
        
        if m:
            self.conclusion = self.polarized(m)
        else:
            credences = np.array([a.credence for a in self.agents])
            self.conclusion = all(credences > .99)

    def run_experiments(self, n, epsilon):
        for a in self.agents:
            a.experiment(n, epsilon)

    def bayes_update_agents(self, epsilon):
        for a in self.agents:
            total_k, total_n = 0, 0
            for neighbor in self.graph[a]:
                total_k += neighbor.k
                total_n += neighbor.n
            if total_n > 0:
                a.bayes_update(total_k, total_n, epsilon)

    def jeffrey_update_agents(self, epsilon, m):
        for a in self.agents:
            for neighbor in self.graph[a]:
                if neighbor == a and a.n > 0:
                    a.bayes_update(a.k, a.n, epsilon)
                elif neighbor.n > 0:
                    a.jeffrey_update(neighbor, epsilon, m)

    def undecided(self):
        credences = np.array([a.credence for a in self.agents])
        return not (all(credences <= .5) or all(credences > .99))

    def polarized(self, m):
        credences = np.array([a.credence for a in self.agents])
        if all((credences < .5) | (credences > .99)) & any(credences < .5) & any(credences > .99):
            min_believer = min(credences[credences > .99])
            max_disbeliever = max(credences[credences < .5])
            d = min_believer - max_disbeliever
            return m * d >= 1
        else:
            return False