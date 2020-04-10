# SNLI-VE: Visual Entailment Dataset  
**Ning Xie, Farley Lai, Derek Doran, Asim Kadav**

<b>SNLI-VE</b> is the dataset proposed for the **Visual Entailment (VE)** task investigated in [Visual Entailment Task for Visually-Grounded Language Learning](https://arxiv.org/abs/1811.10582) accpeted to [NeurIPS 2018 ViGIL workshop](https://nips2018vigil.github.io/)).
Refer to our [full paper](https://arxiv.org/abs/1901.06706) for detailed analysis and evaluations.

![Example](https://drive.google.com/uc?export=view&id=1Bo83CcaPKJqrNg0F_crbeAfCRiTDWlqz)

## Overview  

SNLI-VE is built on top of [SNLI](https://nlp.stanford.edu/projects/snli) and [Flickr30k](http://shannon.cs.illinois.edu/DenotationGraph).
The problem that VE is trying to solve is to reason about the relationship between an `image premise` **_P<sub>image</sub>_** and a `text hypothesis` **_H<sub>text</sub>_**.

Specifically, given an image as `premise`, and a natural language sentence as `hypothesis`, three labels (`entailment`, `neutral` and `contradiction`) are assigned based on the relationship conveyed by the (**_P<sub>image</sub>_**, **_H<sub>text</sub>_**)

- `entailment` holds if there is enough evidence in **_P<sub>image</sub>_** to conclude that **_H<sub>text</sub>_** is true.
- `contradiction` holds if there is enough evidence in **_P<sub>image</sub>_** to conclude that **_H<sub>text</sub>_** is false.
- Otherwise, the relationship is `neutral`, implying the evidence in **_P<sub>image</sub>_** is insufficient to draw a conclusion about **_H<sub>text</sub>_**.
 
This repository contains the following:
- SNLI-VE generated dataset, which can be directly <b>downloaded</b> without running [`snli_ve_generator.py`](snli_ve_generator.py)  in this repository: 
	- [SNLI-VE train split](https://drive.google.com/file/d/1jQElLXUA5ps3OuiSMlJdKTRIMwZ_cJ2e/view?usp=sharing)
	- [SNLI-VE dev split](https://drive.google.com/file/d/1M6uSoJ4rXXsygReioHSJg2Xgip2NLpJW/view?usp=sharing)
	- [SNLI-VE test split](https://drive.google.com/file/d/1_n4g8sbw_P6KBayvJ9B8KklZDFr0uPsQ/view?usp=sharing)  
- Scritps to <b>generate SNLI-VE dataset</b>
	- In case you might prefer to generate SNLI-VE by yourself, we provide the generation script [`snli_ve_generator.py`](snli_ve_generator.py).
- Scripts to <b>parse SNLI-VE dataset</b>
	- [`snli_ve_parser.py`](snli_ve_parser.py) is a sample script to parse SNLI-VE dataset, please feel free to revise as you like! 
  
## Examples from SNLI-VE  
  
![Examples](https://drive.google.com/uc?export=view&id=1FUL2PkSQB6EaTbyMvNz1yj_fMCxU3g_W)
    
## SNLI-VE Generator

The script to generate SNLI-VE dataset is [`snli_ve_generator.py`](snli_ve_generator.py), which will automatically add `Flickr30kID` to each data item and split the dataset into `train`, `dev` and `test` split with no image overlappings.

In order to generate SNLI-VE dataset, the followings are required,

- SNLI dataset (**[download](https://nlp.stanford.edu/projects/snli/snli_1.0.zip)**)
- Flickr30K splits based on previous work on [grounding](https://github.com/kanchen-usc/KAC-Net) using disjoint image sets:
		- `train` split contains all Flickr30k images *except for the last 1000* from [`flickr30k_train_val.lst`](data/flickr30k_train_val.lst)  
		- `dev` split contains the *last 1000* Flickr30k images from [flickr30k_train_val.lst](data/flickr30k_train_val.lst)  
		- `test` split contains all Flickr30k images from [flickr30k_test.lst](data/flickr30k_test.lst)  
	- However, you could use your **self-defined split** if you want.

After downloaded [SNLI dataset](https://nlp.stanford.edu/projects/snli/snli_1.0.zip) and Flickr30k splits ([flickr30k_train_val.lst](data/flickr30k_train_val.lst) and [flickr30k_test.lst](data/flickr30k_test.lst)), and revised the paths properly in `snli_ve_generator.py` to your settings, the generation can be conducted by running below command:

```
python snli_ve_generator.py
```

**Note**

Flickr30K images are not required to run [`snli_ve_generator.py`](snli_ve_generator.py). 
However, it is required if you want to run experiments on SNLI-VE dataset.
Flickr30k images can be download [here](https://drive.google.com/file/d/0B_PL6p-5reUAZEM4MmRQQ2VVSlk/view?usp=sharing).

## SNLI-VE Statistics  

Below is some highlighted dataset statistic, details can be found in our [paper](https://arxiv.org/abs/1811.10582).
  
###  Data Split Distribution

The data details of `train`, `dev` and `test` split is shown below. The instances of three labels (`entailment`, `neutral` and `contradiction`) are evenly distributed for each split.

|   | **Train** | **Dev** | **Test** |  
|  ------ | ------ | ------ | ------ |  
|  **#Image** | 29783 | 1000 | 1000 |  
|  **#Entailment** | 176932 | 5959 | 5973 |  
|  **#Neutral** | 176045 | 5960 | 5964 |  
|  **#Contradiction** | 176550 | 5939 | 5964 |  
|  **Vocabulary Size** | 29550 | 6576 | 6592 |  
 
### Dataset Comparision
  
Below is a dataset comparison summary among **[SNLI-VE](https://arxiv.org/abs/1811.10582)**,  **[VQA-v2.0](https://arxiv.org/abs/1612.00837)** and **[CLEVR](https://arxiv.org/abs/1612.06890)** datasets.  
  
|    | **[SNLI-VE](https://arxiv.org/abs/1811.10582)** | **[VQA-v2.0](https://arxiv.org/abs/1612.00837)** | **[CLEVR](https://arxiv.org/abs/1612.06890)** |  
|  ------ | ------ | ------ | ------ |  
| **Partition Size:** |  |  |  |  
|  Training  | 529527 | 443757 | 699989 |  
|  Validation  | 17858 | 214354 | 149991 |  
|  Testing  | 17901 | 555187 | 149988 |  
| **Question Length:** |  |  |  |  
|  Mean  | 7.4 | 6.1 | 18.4 |  
|  Median  | 7 | 6 | 17 |  
|  Mode   | 6 | 5 | 14 |  
|  Max    | **56** | 23 | 43 |  
| **Vocabulary Size** | **32191** | 19174 | 87 |  
  
### Question Length Distribution

The *question* here for SNLI-VE dataset is the `hypothesis`.
As shown in the figure, the question length of SNLI-VE dataset is quite heavy-tailed distributed.

![Question length distribution](https://drive.google.com/uc?export=view&id=1d3iwptpIzQZjZdwn_d1GlXl8N1kBoCcH)

## SNLI-VE Usage  
  
We also provide a sample script to parse SNLI-VE dataset, see [`snli_ve_parser.py`](snli_ve_parser.py). Please feel free to revise it to your own settings.
  
## SNLI-VE Extensions  
  
[Flickr30k Entities](http://web.engr.illinois.edu/~bplumme2/Flickr30kEntities) dataset is an extension to Flickr30k, which contains detailed annotations. 

It is easy to extend our SNLI-VE dataset with **[Flickr30k Entities](http://web.engr.illinois.edu/~bplumme2/Flickr30kEntities/)** if fine-grained annotations are required to your experiment settings.

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

## 

1. Set the conda environment and dependencies

    ```sh
    conda create -n vet37 python=3.7
    conda activate vet37
    conda install jsonlines
    # conda install -c NECLA-ML ml
    ```

2. Clone the repo

    ``sh
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
    ./download # y to all
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

## SNLI-VE Leaderboard

- **78.98%** by [UNITER](https://arxiv.org/abs/1909.11740)
- 73.02% by [e-SNLI-VE-2.0](https://arxiv.org/abs/2004.03744)
- 71,16% by [EVE-Image](https://arxiv.org/abs/1901.06706)

| Rank     | Test Accuracy          | Source                                            |  
|--------- | ---------------------- | ------------------------------------------------- |
|  1       | 78.98%                 | [UNITER](https://arxiv.org/abs/1909.11740) | 1000 |  
|  2       | 73.02%, 73.18%, 72.52% | [e-SNLI-VE-2.0](https://arxiv.org/abs/2004.03744) |  
| Baseline | 71.16%                 | [EVE-Image](https://arxiv.org/abs/1901.06706)     |  


**NOTE**

`e-SNLI-VE-2.0` relabels the the val and test splits of the neutral class and evalutes the resultings performance in order of the original, val-correction and val/test correction.

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
  
![NEC Laboratories America, Inc.](https://drive.google.com/uc?export=view&id=1c5vFLq4yrj1wcHDds5WEVoTjM-K039La)