# %%
from bg.agent import Agent

a = Agent()
b = Agent()
c = Agent()

b.credence, b.k, b.n = .6, 1, 10
c.credence, c.k, c.n = .6, 9, 10

# %%
a.credence = .4
a.jeffrey_update(b, .1, 2)
a.jeffrey_update(c, .1, 2)
a.credence

# %%
a.credence = .4
a.jeffrey_update(c, .1, 2)
a.jeffrey_update(b, .1, 2)
a.credence
