# Structure Alignment



## DALI

A common and popular structural alignment method is the DALI, or Distance-matrix ALIgnment method, which breaks the input structures into hexapeptide fragments and calculates a distance matrix by evaluating the contact patterns between successive fragments.[[21\]](https://en.wikipedia.org/wiki/Structural_alignment#cite_note-holm-21) 

本质上就是把蛋白拆分成六肽，然后计算每一块之间的distance map[^MappingProteinUniverse]，二级结构填充矩阵的对角线

[Secondary structure](https://en.wikipedia.org/wiki/Secondary_structure) features that involve residues that are contiguous in sequence appear on the matrix's [main diagonal](https://en.wikipedia.org/wiki/Main_diagonal); other diagonals in the matrix reflect spatial contacts between residues that are not near each other in the sequence. When these diagonals are parallel to the main diagonal, the features they represent are parallel; when they are perpendicular, their features are antiparallel. This representation is memory-intensive because the features in the square matrix are symmetrical (and thus redundant) about the main diagonal.

When two proteins' distance matrices share the same or similar features in approximately the same positions, they can be said to have similar folds with similar-length loops connecting their secondary structure elements. DALI's actual alignment process requires a similarity search after the two proteins' distance matrices are built; this is normally conducted via a series of overlapping submatrices of size 6x6. Submatrix matches are then reassembled into a final alignment via a standard score-maximization algorithm — the original version of DALI used a [Monte Carlo](https://en.wikipedia.org/wiki/Monte_Carlo_method) simulation to maximize a structural similarity score that is a function of the distances between putative corresponding atoms. In particular, more distant atoms within corresponding features are exponentially downweighted to reduce the effects of noise introduced by loop mobility, helix torsions, and other minor structural variations.[[20\]](https://en.wikipedia.org/wiki/Structural_alignment#cite_note-Mount-20) Because DALI relies on an all-to-all distance matrix, it can account for the possibility that structurally aligned features might appear in different orders within the two sequences being compared.

The DALI method has also been used to construct a database known as [FSSP](https://en.wikipedia.org/wiki/Families_of_structurally_similar_proteins) (Fold classification based on Structure-Structure alignment of Proteins, or Families of Structurally Similar Proteins) in which all known protein structures are aligned with each other to determine their structural neighbors and fold classification. There is an [searchable database](http://ekhidna.biocenter.helsinki.fi/dali) based on DALI as well as a [downloadable program](http://ekhidna.biocenter.helsinki.fi/dali/README.v5.html) and [web search](http://ekhidna.biocenter.helsinki.fi/dali) based on a standalone version known as DaliLite.

Ref: [Wikipedia](https://en.wikipedia.org/wiki/Structural_alignment)





[^MappingProteinUniverse]: https://www.science.org/doi/10.1126/science.273.5275.595