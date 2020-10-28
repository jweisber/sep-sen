library(tidyverse)
library(gganimate)
library(av)

df <- read_csv("animate.csv")
df <- bind_rows(df, df[rep(157:162, 562), ])
df$epoch[3697:7068] <- rep(seq(27, 588), each = 6)

x <- c(-1,      -1/2,       1/2, 1,        1/2,       -1/2)
y <- c( 0, sqrt(3)/2, sqrt(3)/2, 0, -sqrt(3)/2, -sqrt(3)/2)

df$x <- x[(df$id %% 6) + 1]
df$y <- y[(df$id %% 6) + 1]

cycle <- data.frame(x = c(x, x[1]), y = c(y, y[1]), graph = "cycle")
compl <- data.frame(x = c(x, x[1], x[4], x[2], x[6], x[4], x[3], x[1], x[5], x[3], x[6], x[5], x[2]), 
                    y = c(y, y[1], y[4], y[2], y[6], y[4], y[3], y[1], y[5], y[3], y[6], y[5], y[2]), 
                    graph = "complete")
path <- bind_rows(cycle, compl)

p <- ggplot(df) +
  theme_void(base_size = 14) +  
  facet_wrap( ~ graph) +
  theme(strip.text.x = element_blank()) +
  labs(title = 'Epoch: {closest_state}') +
  geom_path(aes(x = x, y = y), data = path) +  
  geom_point(aes(x = x, y = y, colour = credence), size = 20) +
  scale_color_viridis_c(option = "magma") +
  xlim(-1.25, 1.25) + ylim(-1.25, 1.25) +
  transition_states(epoch)

animate(p, nframes = 1176, fps = 80, height = 500, width = 1000, renderer = av_renderer("animate.mp4"))
