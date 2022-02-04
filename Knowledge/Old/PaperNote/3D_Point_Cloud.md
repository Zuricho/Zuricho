[Tensor field networks: Rotation- and translation-equivariant neural networks for 3D point clouds](https://arxiv.org/abs/1802.08219)

为什么要关注3D点云：蛋白质也是3D点云的问题

> 标量场：空间中每一个点的坐标能够对应一个标量（温度场）
>
> 向量场：空间中每一个点的坐标能够对应一个向量（力场）
>
> 张量场：空间中每一个点的坐标能够对应一个张量。最常见的张量场有广义相对论的应力能张量场（Stress-energy tensor field）。



We introduce **tensor field neural networks**（张量场神经网络）, which are locally equivariant to 3D rotations, translations, and permutations of points at every layer. 3D rotation equivariance removes the need for data augmentation to identify features in arbitrary orientations. Our network uses filters built from spherical harmonics（球谐函数）; due to the mathematical consequences of this filter choice, each layer accepts as input (and guarantees as output) scalars, vectors, and higher-order tensors, in the geometric sense of these terms. We demonstrate the capabilities of tensor field networks with tasks in geometry, physics, and chemistry.

