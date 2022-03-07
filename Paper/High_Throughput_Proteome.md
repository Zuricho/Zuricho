# LiP-MS

## Overview

How to produce high throughput data from *E. coli* proteome?

Professor Paola Picotti from ETH provide a series of possible solutions for discover protein properties of *E. coli* proteome.

- [Nonrefoldability in *E. coli*](https://pubs.acs.org/doi/10.1021/jacs.1c03270)  in JACS 2021 (Stephen D. Fried)
- [Conformation change in yeast](https://www.nature.com/articles/nbt.2999) in NBT 2014
- [Unfold in several species](https://science.sciencemag.org/content/355/6327/eaai7825.abstract) in Science 2017
- [Metabolite Interactions](https://www.sciencedirect.com/science/article/pii/S0092867417314484) in Cell 2018

Core strategy: LiP-MS



## Thermal Stability (Unfold)

Paper title: [Cell-wide analysis of protein thermal unfolding reveals determinants of thermostability](https://science.sciencemag.org/content/355/6327/eaai7825.full)

Comment: Their results suggest that temperature-induced cell death is caused by the **loss of a subset of proteins** with key functions.

Method: **LiP-MS** (limited proteolysis and mass spectrometry)

Overall results:

- Proteome-wide thermal denaturation profiles for *Escherichia coli*, *Saccharomyces cerevisiae*, *Thermus thermophilus*, and human cells
- Comparing of genomes of thermophilic and mesophilic bacteria, we observed enrichment for lysine residues and β-sheet structures in thermostable proteins
- Unstable proteins have a higher content of aspartic acid than that of stable proteins and observed an inverse correlation between protein length and thermal stability
- Thermostable proteins are substantially less prone to thermal aggregation than unstable proteins
- Relative domain thermostability was conserved both within species and across organisms. Thermal stability was not generally similar for proteins encoded by orthologous genes (等位基因). This suggests that the melting temperatures of proteins are affected by the reshuffling of protein domains, despite the conservation of domain stability.
- Our data show a clear direct relationship between protein thermal stability and intracellular abundance and an inverse relationship between protein stability and aggregation or local unfolding. Increasing the thermodynamic stabilities of the folds of abundant proteins will broaden the range of amino acid replacements that a protein can tolerate before misfolding. 
- Revealed that about half of these proteins showed two-state denaturation profiles in the cellular matrix, suggests that many IDPs are globally or locally structured in cells



Studies based on purified proteins and sequence analyses of thermophilic organisms and their mesophilic counterparts revealed that enrichment in specific amino acids or types of secondary structure enhance thermostability. [Ref1](https://link.springer.com/article/10.1007%2Fs101420000003), [Ref2](https://www.pnas.org/content/108/44/17876?ijkey=39b055c7e94acaf91faae34c0de544d19a6cedd4&keytype2=tf_ipsecsha), [Ref3](https://onlinelibrary.wiley.com/doi/full/10.1110/ps.062130306)

Cell death at high temperature may result from global loss of protein structure or may be caused by loss of specific proteins with key functional roles ([8](https://www.sciencedirect.com/science/article/pii/S000634951001324X?via%3Dihub), [15](https://science.sciencemag.org/content/340/6137/1220))

Large-scale stability analyses thus far have used data from purified proteins from different studies ([*8*](https://science.sciencemag.org/content/355/6327/eaai7825.full#ref-8), [*15*](https://science.sciencemag.org/content/355/6327/eaai7825.full#ref-15), [*16*](https://science.sciencemag.org/content/355/6327/eaai7825.full#ref-16)).These data sets are very heterogeneous and include measurements conducted under various experimental conditions.



Workflow of the LiP-MS–based analysis of protein stability:

<img src="High_Throughput_Proteome.assets\image-20210813022202292.png" alt="image-20210813022202292" style="zoom:80%;" />



