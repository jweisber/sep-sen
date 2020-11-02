library(tidyverse)
library(hrbrthemes)
theme_set(theme_ipsum(base_size = 14))

# Fig 2 ----
df2 <- read_csv("rbo-fig-2.csv") %>%
  mutate(graph = factor(graph, levels = c("cycle", "complete"))) %>%
  group_by(graph, epsilon) %>%
  summarise(p = mean(conclusion)) %>%
  ungroup()

ggplot(df2) +
  geom_path(aes(x = epsilon, y = p, colour = graph)) +
  scale_color_brewer(palette = "Set1") +
  xlab("Epsilon") + ylab("Probability of True Consensus") +
  labs(colour = "Shape") +
  theme(axis.title.x = element_text(size = 12), axis.title.y = element_text(size = 12))

ggsave("rbo-2.png", width = 10, height = 7)

# Fig 3 ----
df3 <- read_csv("rbo-fig-3.csv") %>%
  mutate(graph = factor(graph, levels = c("cycle", "complete"))) %>%
  group_by(graph, trials) %>%
  summarise(p = mean(conclusion)) %>%
  ungroup()

ggplot(df3) +
  geom_path(aes(x = trials, y = p, colour = graph)) +
  scale_color_brewer(palette = "Set1") +
  xlab("Trials") + ylab("Probability of True Consensus") +
  labs(colour = "Shape") +
  theme(axis.title.x = element_text(size = 12), axis.title.y = element_text(size = 12))

ggsave("rbo-3.png", width = 10, height = 7)

# Fig 4 ----
df4 <- read_csv("rbo-fig-4.csv") %>%
  mutate(graph = factor(graph, levels = c("cycle", "complete"))) %>%  
  group_by(graph, agents) %>%
  summarise(p = mean(conclusion)) %>%
  ungroup()

ggplot(df4) +
  geom_path(aes(x = agents, y = p, colour = graph)) +
  scale_color_brewer(palette = "Set1") +
  xlab("Number of Agents") + ylab("Probability of True Consensus") +
  labs(colour = "Shape") +
  theme(axis.title.x = element_text(size = 12), axis.title.y = element_text(size = 12))

ggsave("rbo-4.png", width = 10, height = 7)
