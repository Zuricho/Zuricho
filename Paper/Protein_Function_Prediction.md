# Protein Function Prediction

We now have various method to predict protein function, these methods can be divided to 2 major categories:

- from sequence to function
- from structure to function



## Training set

SIFTS database ([Dana et al., 2018](https://doi.org/10.1093/nar/gky1114)). This database contains EC annotations for entries on the Protein Data Bank (PDB)





## Models



Hou et al. (2018) [Deepsf](https://academic.oup.com/bioinformatics/article-abstract/34/8/1295/4708302)

Rao et al. (2019) [TAPE](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7774645/) 

Bepler & Berger (2019) [Learning protein sequence embeddings using information from structure](https://arxiv.org/abs/1902.08661)

Alley et al. (2019) [UniRep](https://www.nature.com/articles/s41592-019-0598-1)

Strodthoff et al. (2020) [UDSMProt](https://academic.oup.com/bioinformatics/article-abstract/36/8/2401/5698270)

Elnaggar et al. (2020) [ProtTrans (ProtBERT)](https://arxiv.org/abs/2007.06225)

Kipf & Welling (2017) [GNN](https://arxiv.org/abs/1609.02907)

Diehl (2019) [GNN](https://arxiv.org/abs/1905.10990)

Derevyanko et al. [3D CNN](https://academic.oup.com/bioinformatics/article/34/23/4046/5040325?login=true)

Gligorijevic et al. (2021)  [DeepFRI (LSTM+GCN)](https://www.nature.com/articles/s41467-021-23303-9)

Baldassarre et al. (2020) [GraphQA](https://doi.org/10.1093/bioinformatics/btaa714)

Hermosilla et al. (2021) [IEconv](https://arxiv.org/abs/2007.06252)

[Random Embeddings and Linear Regression can Predict Protein Function](https://arxiv.org/abs/2104.14661)

[BERTology Meets Biology](https://arxiv.org/abs/2006.15222): BERT, ALBERT, XLNet

Kulmanov et al. (2020) [DeepGOPlus](https://doi.org/10.1093/bioinformatics/btz595)

Nicolas et al. (2020) [PersGNN](https://arxiv.org/abs/2010.16027)

### BERTology Meets Biology: Interpreting Attention in Protein Language Models

[Paper](https://arxiv.org/abs/2006.15222)

[Github](https://github.com/salesforce/provis)

评估了各种用于预测序列性质的，基于Transformer的方法（这些方法一般解决的是从序列预测功能的任务），用一种可视化方法表示这些Attention模块能够学到蛋白质中结构层面的信息



### DeepFRI: Structure-based protein function prediction using graph convolutional networks

[Paper](https://www.nature.com/articles/s41467-021-23303-9#Sec1)

[Github](https://github.com/flatironinstitute/DeepFRI)

DeepFRI: a Graph Convolutional Network for predicting protein functions by leveraging sequence features extracted from a protein language model and protein structures. 

Class activation mapping allows function predictions at an unprecedented resolution, allowing site-specific annotations at the residue-level in an automated manner. ==This is interesting==

Core pipeline:

![img](https://github.com/flatironinstitute/DeepFRI/raw/master/figs/pipeline.png)

这个方法将蛋白质结构转化为 contact map 作为输入，可能损失很多的信息？不过使用了图网络倒是可以避免，但是很可能难以learn到global的性质

还是把这个作为Benchmark吧





### IEConv: Intrinsic-Extrinsic Convolution and Pooling for Learning on 3D Protein Structures

[Paper](https://arxiv.org/abs/2007.06252)

[Github](https://github.com/phermosilla/IEConv_proteins)

其实整体工作是不错的，就是代码写的太糟糕了，部署比较困难

通病：卷积网络可能学不到全局特征

Core concept: intrinsic distance & extrinsic distance

![image-20210813191023098](.\Protein_Function_Prediction.assets\image-20210813191023098.png)

#### Major components and architecture

Convolution kernel: Intrinsic-extrinsic convolution on our multi-graph for atom A

![image-20210813191145345](.\Protein_Function_Prediction.assets\image-20210813191145345.png)

Hierarchical protein pooling

![image-20210813191912467](.\Protein_Function_Prediction.assets\image-20210813191912467.png)

Model architecture

![image-20210813192100656](.\Protein_Function_Prediction.assets\image-20210813192100656.png)



