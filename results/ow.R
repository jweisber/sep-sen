library(tidyverse)
library(hrbrthemes)
theme_set(theme_ipsum())


df <- read_csv("ow.csv") %>%
  mutate(agents = factor(agents, levels = c(20, 10, 6, 2))) %>%
  group_by(agents, mistrust) %>%
  summarise(p = mean(conclusion)) %>%
  ungroup()

ggplot(df) +
  geom_point(aes(x = mistrust, y = p, colour = agents)) +
  geom_path(aes(x = mistrust, y = p, colour = agents)) +
  scale_y_continuous(breaks = seq(0, 1, .2)) +
  scale_color_brewer(palette = "Set2")

ggsave("ow.png", width = 10, height = 7)
