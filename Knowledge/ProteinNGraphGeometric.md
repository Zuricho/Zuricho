# Deep Learning Models in Protein Structure

[TOC]

## Protein Structure Prediction Task

**AlphaFold**[^AlphaFold]

两个主要部分，Evoformer (Attention) 和 Structure Module (3D Equivariant)

Structure Module 中没有用到 Graph 的部分，更多还是Attention的操作为主 (IPA, Invariant Point Attention)



**RoseTTAFold** [^RoseTTAFold]

直接利用了SE(3)-Transformer [^SE3Transformer]，应该会用到其中的图结构



**EBM-Fold** [^EBMFold] 和 **SE(3)-Equivariant Energy-based Models** [^SE3EBM] 都是腾讯后续模仿AlphaFold的工作，用到了很多SE(3)的概念



Ron Dror 在这方面的工作：

- 算法为主的[^RonDrorArxiv]
- 应用为主的[^RonDrorProtein]





## SE(3) Models

**Tensor field networks** [^TensorField]

概念的产生：3D 点云的学习



**SE(3)-Transformer**[^SE3Transformer]

Author: Max Welling

在Transformer中用到了符合SE(3)等变的架构



**Iterative SE(3)-Transformers** [^IterativeSE3]

Author: Fabian B. Fuchs

类似的文章





## Protein Function Classification Task

**GCN方法**[^DeepFRI]

发在 Nature Communications，算是一个比较Benchmark的方法





## RNA Structure Task

**Geometric deep learning of RNA structure**[^RNA]

Rhiju Das 和 Ron Dror 联手的工作，Das 负责 RNA 的部分，Dror负责 Geometric learning 的部分

宣称能够实现从18个样本里面学习一个用于评估RNA结构的打分函数





## Protein Design Task

**Generative Model, Graph-Based Protein Design** [^Jaakkola]

**Deep Graph Neural Networks** [^PhillipKim]



## Normalize Flow

这个领域主要都是 Frank Noe 的工作

**Boltzmann Generator** [^BoltzmannGenerator]

方法学能上Science的文章并不多



Temperature Steerable Flows [^TemperatureFlow]

一篇用Flow的新文章



## References

[^AlphaFold]: https://www.nature.com/articles/s41586-021-03819-2

[^RoseTTAFold]: https://www.science.org/doi/full/10.1126/science.abj8754
[^SE3Transformer]: https://arxiv.org/abs/2006.10503
[^TensorField]: https://arxiv.org/abs/1802.08219
[^IterativeSE3]: https://arxiv.org/abs/2102.13419
[^EBMFold]: https://arxiv.org/abs/2105.04771
[^SE3EBM]: https://doi.org/10.1101/2021.06.06.447297
[^Jaakkola]: https://proceedings.neurips.cc/paper/2019/hash/f3a4ff4839c56a5f460c88cce3666a2b-Abstract.html
[^PhillipKim]: https://linkinghub.elsevier.com/retrieve/pii/S2405471220303276
[^RonDrorArxiv]: https://arxiv.org/abs/2106.03843
[^RonDrorProtein]: https://onlinelibrary.wiley.com/doi/full/10.1002/prot.26033
[^DeepFRI]: https://www.nature.com/articles/s41467-021-23303-9
[^BoltzmannGenerator]: https://science.sciencemag.org/content/365/6457/eaaw1147.abstract
[^TemperatureFlow]: https://arxiv.org/abs/2108.01590

