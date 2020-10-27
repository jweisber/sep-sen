from numpy import random


class Agent:
    def __init__(self):
        self.credence = random.uniform(0, 1)
        self.k, self.n = 0, 0
    
    def __str__(self):
        return f"credence = {round(self.credence, 2)}, k = {self.k}, n = {self.n}"

    def experiment(self, n, epsilon):
        if self.credence > .5:
            self.k = random.binomial(n, .5 + epsilon)
            self.n = n
        else:
            self.k, self.n = 0, 0
    
    def bayes_update(self, k, n, epsilon):
        self.credence = 1 / (1 + (1 - self.credence) * (((0.5 - epsilon) / (0.5 + epsilon)) ** (2 * k - n)) / self.credence)
    
    def jeffrey_update(self, neighbor, epsilon, m):
        n = neighbor.n
        k = neighbor.k
        
        p_E_H  = (0.5 + epsilon)**k * (0.5)**(n - k)
        p_E_nH = (0.5)**k * (0.5 + epsilon)**(n - k)
        p_E    = self.credence * p_E_H + (1 - self.credence) * p_E_nH
        
        p_H_E  = self.credence * p_E_H / p_E
        p_H_nE = self.credence * (1 - p_E_H) / (1 - p_E)
        
        q_E = 1 - min(1, abs(self.credence - neighbor.credence) * m) * (1 - p_E)  # max(1 - abs(self.credence - neighbor.credence) * m * (1 - p_E), 0)

        self.credence = p_H_E * q_E + p_H_nE * (1 - q_E)