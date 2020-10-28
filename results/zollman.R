library(tidyverse)
library(hrbrthemes)
theme_set(theme_ipsum(base_size = 14))


df <- read_csv("zollman.csv") %>%
  mutate(graph = factor(graph, levels = c("cycle", "wheel", "complete"))) %>%
  group_by(graph, agents) %>%
  summarise(p = mean(conclusion)) %>%
  ungroup()

ggplot(df) +
  geom_point(aes(x = agents, y = p, colour = graph)) +
  geom_path(aes(x = agents, y = p, colour = graph)) +
  scale_color_brewer(palette = "Set2") +
  labs(colour = "Shape") +
  xlab("Number of Agents") + ylab("Probability of True Consensus") +
  theme(axis.title.x = element_text(size = 12), axis.title.y = element_text(size = 12))

ggsave("zollman.png", width = 10, height = 7)
