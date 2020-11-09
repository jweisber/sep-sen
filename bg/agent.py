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
        
        p_E_H  = (0.5 + epsilon)**k * (0.5 - epsilon)**(n - k)         # P(E|H)  = p^k (1-p)^(n-k)
        p_E_nH = (0.5 - epsilon)**k * (0.5 + epsilon)**(n - k)         # P(E|~H) = (1-p)^k p^(n-k)
        p_E    = self.credence * p_E_H + (1 - self.credence) * p_E_nH  # P(E) = P(E|H) P(E) + P(E|~H) P(~H)
        
        p_H_E  = self.credence * p_E_H / p_E                           # P(H|E)  = P(H) P(E|H)  / P(E)
        p_H_nE = self.credence * (1 - p_E_H) / (1 - p_E)               # P(H|~E) = P(H) P(~E|H) / P(~E)
        
        # q_E = max(1 - abs(self.credence - neighbor.credence) * m * (1 - p_E), 0)  # O&W's Eq. 1 (anti-updating)
        q_E = 1 - min(1, abs(self.credence - neighbor.credence) * m) * (1 - p_E)    # O&W's Eq. 2

        self.credence = p_H_E * q_E + p_H_nE * (1 - q_E)               # Jeffrey's Rule
                                                                       # P'(H) = P(H|E) P'(E) + P(H|~E) P'(~E)