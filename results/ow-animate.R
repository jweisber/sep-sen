library(tidyverse)
library(hrbrthemes)
library(gganimate)
theme_set(theme_ipsum())


df <- read_csv("ow-animate.csv") %>%
  group_by(epoch) %>%
  mutate(d      = abs(credence - min(credence[credence > .5])),
         status = case_when(credence > .5 ~ "active",
                            2 * d < 1     ~ "open",
                            TRUE          ~ "closed"),
         status = factor(status, levels = c("closed", "active", "open"))) %>%  # red, blue, green
  ungroup()

a <- max(df$agent) + 1
df$agent <- rep(rank(df$credence[1:a]), max(df$epoch) + 1)  # order agents by initial credence

p <- ggplot(df) +
  geom_point(aes(x = credence, y = agent, colour = status, group = agent), size = 4) +
  scale_color_brewer(palette = "Set1") +
  labs(subtitle = 'Epoch: {closest_state}', x = "Credence") +
  scale_y_continuous(breaks = 0:max(df$agent)) +
  scale_x_continuous(breaks = c(0, 0.5, 1.0)) +
  theme(axis.title.y = element_blank(), axis.text.y = element_blank(), axis.ticks.y = element_blank(),
        panel.grid.minor.x = element_blank(), panel.grid.minor.y = element_blank(), 
        legend.position = "none") +
  coord_cartesian(expand = FALSE, clip = "off") +
  transition_states(epoch, wrap = FALSE, state_length = .25, transition_length = 2)

animate(p, renderer = av_renderer("ow-animate.mp4"), height = 5, width = 8, units = "in", 
        res = 300, fps = 30, duration = 8)
