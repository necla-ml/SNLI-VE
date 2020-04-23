# SNLI-VE: Visual Entailment Dataset  
**Ning Xie, Farley Lai, Derek Doran, Asim Kadav**
  
![NEC Laboratories America, Inc.](http://www.nec-labs.com/static/images/layout/nec-laboratories-site-logo.jpg)

**SNLI-VE** is the dataset proposed for the **Visual Entailment (VE)** task investigated in [Visual Entailment Task for Visually-Grounded Language Learning](https://arxiv.org/abs/1811.10582) accpeted to [NeurIPS 2018 ViGIL workshop](https://nips2018vigil.github.io/)).
Refer to our [full paper](https://arxiv.org/abs/1901.06706) for detailed analysis and evaluations.

![Example](https://drive.google.com/uc?export=view&id=1Bo83CcaPKJqrNg0F_crbeAfCRiTDWlqz)

## Leaderboard

| Rank     | Test Accuracy          | Source                                             |  Date      |  
|:--------:|:----------------------:| ---------------------------------------------------|:----------:|
|  1       | 78.98%                 | [UNITER](https://arxiv.org/abs/1909.11740)         | 09/25/2019 |  
|  2       | 73.02%, 73.18%, 72.52% | [e-SNLI-VE-2.0](https://arxiv.org/abs/2004.03744)  | 04/07/2020 |  
| Baseline | 71.16%                 | [EVE-Image](https://arxiv.org/abs/1901.06706)      | 11/26/2018 |  

**NOTE**

`e-SNLI-VE-2.0` relabels the `dev` as well as `test` splits of the neutral class and evalutes the resulting performance in order of the original, val-correction and val/test correction configurations.

## Overview  

SNLI-VE is built on top of [SNLI](https://nlp.stanford.edu/projects/snli) and [Flickr30K](http://shannon.cs.illinois.edu/DenotationGraph).
The problem that VE is trying to solve is to reason about the relationship between an `image premise` **_P<sub>image</sub>_** and a `text hypothesis` **_H<sub>text</sub>_**.

Specifically, given an image as `premise`, and a natural language sentence as `hypothesis`, three labels (`entailment`, `neutral` and `contradiction`) are assigned based on the relationship conveyed by the (**_P<sub>image</sub>_**, **_H<sub>text</sub>_**)

- `entailment` holds if there is enough evidence in **_P<sub>image</sub>_** to conclude that **_H<sub>text</sub>_** is true.
- `contradiction` holds if there is enough evidence in **_P<sub>image</sub>_** to conclude that **_H<sub>text</sub>_** is false.
- Otherwise, the relationship is `neutral`, implying the evidence in **_P<sub>image</sub>_** is insufficient to draw a conclusion about **_H<sub>text</sub>_**.
 
### Examples from SNLI-VE  
  
![Examples](https://drive.google.com/uc?export=view&id=1FUL2PkSQB6EaTbyMvNz1yj_fMCxU3g_W)
    
## SNLI-VE Statistics  

Below is some highlighted dataset statistic, details can be found in our [paper](https://arxiv.org/abs/1811.10582).
  
### Distribution by Split

The data details of `train`, `dev` and `test` split is shown below. The instances of three labels (`entailment`, `neutral` and `contradiction`) are evenly distributed for each split.

|                      | **Train** | **Dev** | **Test** |  
|  ------------------- | --------- | ------- | -------- |  
|  **#Image**          |  29783    | 1000    | 1000     |  
|  **#Entailment**     | 176932    | 5959    | 5973     |  
|  **#Neutral**        | 176045    | 5960    | 5964     |  
|  **#Contradiction**  | 176550    | 5939    | 5964     |  
|  **Vocabulary Size** |  29550    | 6576    | 6592     |  
 
### Dataset Comparision
  
Below is a dataset comparison among [SNLI-VE](https://bit.ly/2VgSfbI), [VQA-v2.0](https://bit.ly/2Vhe9vn) and [CLEVR](https://bit.ly/2VkpoD8).  
  
|  | [SNLI-VE](https://bit.ly/2VgSfbI) | [VQA-v2.0](https://bit.ly/2Vhe9vn) | [CLEVR](https://bit.ly/2VkpoD8) |  
|  ------------------- | --------- | ------ | ------ |  
| **Partition Size:**  |           |        |        |  
|  Training            | 529527    | 443757 | 699989 |  
|  Validation          |  17858    | 214354 | 149991 |  
|  Test                |  17901    | 555187 | 149988 |  
| **Question Length:** |           |        |        |  
|  Mean                |    7.4    |    6.1 |   18.4 |  
|  Median              |      7    |      6 |     17 |  
|  Mode                |      6    |      5 |     14 |  
|  Max                 |    **56** |     23 |     43 |  
| **Vocabulary Size**  | **32191** |  19174 |     87 |  
  
### Question Length Distribution

The *question* here for SNLI-VE dataset is the `hypothesis`.
As shown in the figure, the question length of SNLI-VE dataset is distributed with a quite long tail.

![Question length distribution](https://drive.google.com/uc?export=view&id=1d3iwptpIzQZjZdwn_d1GlXl8N1kBoCcH)
  
## Caveats

To check the quality of SNLI-VE dataset, we randomly sampled 217 pairs from all three splits (565286 pairs in total).
Among all sampled pairs, 20 (about 9.2%) examples are incorrectly labeled, among which the majority is in the `neutral` class. 
This is consistent to the analysis reported by [GTE](https://www.aclweb.org/anthology/C18-1199) in its Table 2.

It is worth noting that the original SNLI dataset is not perfectly labeled, 
with 8.8% of the sampled data not assigned a `gold label`, 
implying the disagreement within human labelers. 
SNLI-VE is no exception but we believe it is a common scenario in other large scale datasets.
However, if the dataset quality is a major concern to you, 
we suggest dropping the `neutral` classs and only use `entailment` and `contradiction` examples.

## SNLI-VE Creation

[snli_ve_generator.py](vet/tools/snli_ve_generator.py) generates the SNLI-VE dataset in `train`, `dev` and `test` splits with disjoint image sets. 
Each entry contains a `Flickr30kID` field to associate with the original Flickr30K image id. 

[snli_ve_parser.py](vet/tools/snli_ve_parser.py) parses entires in SNLI-VE for applications and is free to revise.

Follow the instructions below to set up the environment and generate SNLI-VE:

1. Set the conda environment and dependencies

    ```sh
    conda create -n vet37 python=3.7
    conda activate vet37
    conda install jsonlines
    # conda install -c NECLA-ML ml
    ```

2. Clone the repo

    ```sh
    git clone https://github.com/necla-ml/SNLI-VE.git
    ```

2. Generate SNLI-VE in `data/`

    ```sh
    cd SNLI-VE
    python -m vet.tools.snli_ve_generator.py
    ```

3. Download dependent datasets: Flickr30K, Entities, SNLI, and RoI features 

    ```sh
    cd data
    ./download # y to all if necessary
    ```

<!--
4. Extract RoI features from pre-extracted

  ```sh
  python -m vet.tools.ROI_related
  ```

5. Train models

  ```sh
  ```

6. Evaluation

  ```sh
  ```
-->

### SNLI-VE Extensions  
  
[Flickr30k Entities](http://web.engr.illinois.edu/~bplumme2/Flickr30kEntities) dataset is an extension to Flickr30k, which contains grounded RoI and entity annotations. 

It is easy to extend our SNLI-VE dataset with **[Flickr30k Entities](http://web.engr.illinois.edu/~bplumme2/Flickr30kEntities/)** if fine-grained annotations are required in your experiments.

## Bibtex  

The first is our full paper while the second is the ViGiL workshop version.

```  
@article{xie2019visual,
  title={Visual Entailment: A Novel Task for Fine-grained Image Understanding},
  author={Xie, Ning and Lai, Farley and Doran, Derek and Kadav, Asim},
  journal={arXiv preprint arXiv:1901.06706},
  year={2019}
}

@article{xie2018visual,
  title={Visual Entailment Task for Visually-Grounded Language Learning},
  author={Xie, Ning and Lai, Farley and Doran, Derek and Kadav, Asim},
  journal={arXiv preprint arXiv:1811.10582},
  year={2018}
}  
```  
  
Thank you for your interest in our dataset!  
Please contact [us](farleylai@nec-labs.com) for any questions, comments, or suggestions!
