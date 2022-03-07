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


```

