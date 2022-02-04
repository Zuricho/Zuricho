# Graph Theory

主要参考2021组合数学课程

参考教材：

- Introduction to Graph Theory, Douglas West [^West]
- Combinatorics and Graph Theory, By Harris, Hirst and Mossinghoff [^Harris]
- Graph Theory, Reinhard Diestel [^Diestel]
- Graph Theory, by Bondy and Murty [^Bondy]

- A course in Combinatorics, J. H. Van Lint [^Lint]



## Basics

Graph $G (V,E)$

Simple Graph: 简单图，无loop，无多重边

homomorphism - 同态（从A到B保持关联性）

isomorphic - 图同构（A到B和B到A）

导出(induced)子图、支撑(spanning)子图

k-regular：k-正则，每个顶点的度(degree)相同

二部图(Bipartite graph)

Walk(游走，通道)，Path(路)

$\delta (G)$, $\Delta (G)$, $\text{d} (G)$



[1.2.2 D] 每个至少有一条边的图包含一个子图H满足$\delta (G) > \frac{1}{2}d(H) > \frac{1}{2}d(G)$

- 删除degree最小的顶点证明



distance, diameter（直径）, central（中心点），radius（半径）



girth(围长)，$g(G)$

A graph with large girth has small chromatic number? no

Theorem (Erdős, 1959) For all 𝑘, 𝑙, there exists a graph 𝐺 with $g(G)>l$ and $\chi(G)>k$ （证明略）



[1.3.23 W] 在n-顶点的 triangle-free简单图中，最大边数是$\left\lfloor n^{2} / 4\right\rfloor$

- $e(G)$被具有n个顶点的完全二部图限制



连通，连通分量(component)，桥/割边(bridge)，割点(cut vertex)，cut set, 连通分量$\kappa(G)$就是最小cut set的数量，edge connectivity($\lambda (G)$)

[1.4.2 D] 若G非平凡，则$\kappa(G) \leq \lambda(G) \leq \delta(G)$

- 具体讨论即可



[1.2.23 W] 完全图$K_n$可以被表示为k个二部图的并当且仅当$n \leq 2^k $

- 对k归纳



[1.3.19 W] 每个无环图都有一个二部子图至少包含$e(G)/2$的边

- 划分成两边，然后移点



## References

[^West]: Introduction to Graph Theory, Douglas West
[^Harris]: Combinatorics and Graph Theory, By Harris, Hirst and Mossinghoff
[^Diestel]: Graph Theory, Reinhard Diestel
[^Bondy]: Graph Theory, by Bondy and Murty
[^Lint]: A course in Combinatorics, J. H. Van Lint