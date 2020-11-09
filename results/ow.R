library(tidyverse)
library(hrbrthemes)
theme_set(theme_ipsum(base_size = 14))


# Fig 1 ----
q_E <- function(x, m, p_E) 1 - pmin(1, x * m) * (1 - p_E)

ggplot() +
  stat_function(fun = q_E, args = list(m = 1.5, p_E = .6)) +
  scale_y_continuous(breaks = seq(0, 1, .2), limits = c(0, 1)) +
  xlab(expression(italic(d))) + ylab(expression(italic("P'(E)"))) +
  theme(axis.title.x = element_text(size = 12), axis.title.y = element_text(size = 12))

ggsave("ow-1.png", width = 10, height = 7)


# Fig 2 ----
df <- read_csv("ow.csv") %>%
  mutate(agents = factor(agents, levels = c(20, 10, 6, 2))) %>%
  group_by(agents, mistrust) %>%
  summarise(p = mean(conclusion)) %>%
  ungroup()

ggplot(df) +
  geom_point(aes(x = mistrust, y = p, colour = agents)) +
  geom_path(aes(x = mistrust, y = p, colour = agents)) +
  scale_y_continuous(breaks = seq(0, 1, .2)) +
  scale_color_brewer(palette = "Set2") +
  xlab("Mistrust") + ylab("Probability of Polarization") +
  labs(colour = "Agents") +
  theme(axis.title.x = element_text(size = 12), axis.title.y = element_text(size = 12))

ggsave("ow-2.png", width = 10, height = 7)
