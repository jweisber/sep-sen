library(igraph)

g1 <- make_full_graph(6, directed = FALSE)
g3 <- make_ring(6, directed = FALSE)

wheel <- union(make_ring(5), make_star(6, center = 6, mode = "undirected"))
V(wheel)$name <- letters[seq_len(vcount(wheel))]
sstar <- make_star(6, center = 6, mode = "undirected")
V(sstar)$name <- letters[c(1, 3, 5, 7, 9, 11)]
g2 <- wheel %m% sstar

par(mfrow = c(1, 3), cex.lab = 2)
plot(g1, layout = layout_in_circle(g1), vertex.label = NA, xlab = "complete")
plot(g2, layout = layout_nicely(g2),    vertex.label = NA, xlab = "wheel")
plot(g3, layout = layout_in_circle(g3), vertex.label = NA, xlab = "cycle")
