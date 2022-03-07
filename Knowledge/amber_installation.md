# AMBER Installation

```bash
# Unpack 
tar jxvf amber20.tar.bz2
tar jxvf ambertools.tar.bz2


# Prepare miniconda environments
module load miniconda3
conda create -n amber
conda install -c conda-forge AmberTools

# run on computing nodes
srun p ...

# cmake
cd amber20_src/build
./run_cmake
make install

export PATH="/dssg/home/acct-stu/stu/software/amber20_src/build/CMakeFiles/miniconda/install/bin:$PATH"

```

## Used module

```bash
module load miniconda3

conda create -n amber
conda install -c conda-forge AmberTools
conda install numpy scipy matplotlib

module load cuda/10.1
module load openmpi
module load cmake
# all gcc version corresbond the the highest version: 12
```



## References

https://ambermd.org/doc12/Amber20.pdf page 24

https://ambermd.org/InstCentOS.php

