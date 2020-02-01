# SNLI-VE: Visual Entailment Dataset  
<p align="left">  
  <b>Ning Xie, Farley Lai, Derek Doran, Asim Kadav</b></span>  
</p>  

This is the <b>SNLI-VE</b> dataset we propose for <b>Visual Entailment (VE)</b> task in [Visual Entailment Task for Visually-Grounded Language Learning](https://arxiv.org/abs/1811.10582) (accpeted by <b>[NeurIPS 2018 ViGIL workshop](https://nips2018vigil.github.io/)</b>). Please also refer to our [full paper](https://arxiv.org/abs/1901.06706) for detailed analysis and models.
  
<div align="center">  
  <img   
  src="https://drive.google.com/uc?export=view&id=1Bo83CcaPKJqrNg0F_crbeAfCRiTDWlqz" style="float:left" width="1000px">  
</div>  
  



  
## Overview  

SNLI-VE is a dataset for VE task, which is generated based on [SNLI](https://nlp.stanford.edu/projects/snli/) and [Flickr30k](http://shannon.cs.illinois.edu/DenotationGraph/). The problem that VE trying to solve is to reason the relationship between an `image premise` <i>**P<sub>image</sub>**</i> and a `text hypothesis` <i>**H<sub>text</sub>**</i>.

Specifically, given an image as `premise`, and a natural language sentence as `hypothesis`, three labels (`entailment`, `neutral` and `contradiction`) are assigned based on the relationship conveyed by the (<i>**P<sub>image</sub>**</i>, <i>**H<sub>text</sub>**</i>)

- `entailment` holds if there is enough evidence in <i>**P<sub>image</sub>**</i> to conclude that <i>**H<sub>text</sub>**</i> is true.
- `contradiction` holds if there is enough evidence in <i>**P<sub>image</sub>**</i> to conclude that <i>**H<sub>text</sub>**</i> is false.
- Otherwise, the relationship is `neutral`, implying the evidence in <i>**P<sub>image</sub>**</i> is insufficient to draw a conclusion about <i>**H<sub>text</sub>**</i>.
 
<b>This repository contains the followings</b>,
 
- SNLI-VE generated dataset, which can be directly <b>downloaded</b> without running [`snli_ve_generator.py`](snli_ve_generator.py)  in this repository: 
	- [<b>SNLI-VE train split</b>](https://drive.google.com/file/d/1jQElLXUA5ps3OuiSMlJdKTRIMwZ_cJ2e/view?usp=sharing)
	- [<b>SNLI-VE dev split</b>](https://drive.google.com/file/d/1M6uSoJ4rXXsygReioHSJg2Xgip2NLpJW/view?usp=sharing)
	- [<b>SNLI-VE test split</b>](https://drive.google.com/file/d/1_n4g8sbw_P6KBayvJ9B8KklZDFr0uPsQ/view?usp=sharing)  
- Scritps to <b>generate SNLI-VE dataset</b>
	- In case you might prefer to generate SNLI-VE by yourself, we provide the generation script [`snli_ve_generator.py`](snli_ve_generator.py).
- Scripts to <b>parse SNLI-VE dataset</b>
	- [`snli_ve_parser.py`](snli_ve_parser.py) is a sample script to parse SNLI-VE dataset, please feel free to revise as you like! 
  
## Examples from SNLI-VE  
  
<div align="center">  
  <img   
  src="https://drive.google.com/uc?export=view&id=1FUL2PkSQB6EaTbyMvNz1yj_fMCxU3g_W" style="float:left" width="1000px">  
</div>  
  
  
## SNLI-VE Generator  
The script to generate SNLI-VE dataset is [`snli_ve_generator.py`](snli_ve_generator.py), which will automatically add `Flickr30kID` to each data item and split the dataset into `train`, `dev` and `test` split with no image overlappings.

In order to generate SNLI-VE dataset, the followings are required,

- SNLI dataset (**[download](https://nlp.stanford.edu/projects/snli/snli_1.0.zip)**)
- Flickr30k split list ([`flickr30k_train_val.lst`](flickr30k_train_val.lst) and [`flickr30k_test.lst`](flickr30k_test.lst))

	- We adopt other's split,  which can be found [here](https://github.com/kanchen-usc/KAC-Net). 
		- <b>`test`</b> split contains all Flickr30k images from [`flickr30k_test.lst`](flickr30k_test.lst)  
		- <b>`dev`</b> split contains the <i>last 1000</i> Flickr30k images from [`flickr30k_train_val.lst`](flickr30k_train_val.lst)  
		- <b>`train`</b> split contains all Flickr30k images <i>except for the last 1000</i> from [`flickr30k_train_val.lst`](flickr30k_train_val.lst)  
	- However, you could use your **self-defined split** if you want.
- *Flickr30k images (**[download](https://drive.google.com/file/d/0B_PL6p-5reUAZEM4MmRQQ2VVSlk/view?usp=sharing)**)

	- **Note**: the images are not required to run [`snli_ve_generator.py`](snli_ve_generator.py). 
	- However, it is required if you want to run experiments on SNLI-VE dataset.

After **downloaded** [SNLI dataset](https://nlp.stanford.edu/projects/snli/snli_1.0.zip) and Flickr30k split files ([`flickr30k_train_val.lst`](flickr30k_train_val.lst) and [`flickr30k_test.lst`](flickr30k_test.lst)), and **revised the paths** properly in `snli_ve_generator.py` to your settings, the generation can be conducted by running below command
```
python snli_ve_generator.py
```
  
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
The *question* here for SNLI-VE dataset is the `hypothesis`. As shown in the figure, the question length of SNLI-VE dataset is quite heavy-tailed distributed.

<div align="center">  
  <img   
  src="https://drive.google.com/uc?export=view&id=1d3iwptpIzQZjZdwn_d1GlXl8N1kBoCcH" style="float:left" width="500px">  
</div>  
  
## SNLI-VE Usage  
  
We also provide a sample script to parse SNLI-VE dataset, see [`snli_ve_parser.py`](snli_ve_parser.py). Please feel free to revise it to your own settings.
  
## SNLI-VE Extensions  
  
**[Flickr30k Entities](http://web.engr.illinois.edu/~bplumme2/Flickr30kEntities/)** dataset is an extension to Flickr30k, which contains detailed annotations. 

It is easy to extend our SNLI-VE dataset with **[Flickr30k Entities](http://web.engr.illinois.edu/~bplumme2/Flickr30kEntities/)** if fine-grained annotations are required to your experiment settings.


## SNLI-VE Quality Analysis

To check the quality of SNLI-VE dataset, we randomly sampled 217 (image, hypothesis) pairs from all three split (train+val+test, totally 565286 pairs).
Among all sampled examples, 20 (about 9.2\%) examples are incorrectly labeled, among which the majority are `neutral` examples. 
This is consistent to the analysis reported by [GTE](https://www.aclweb.org/anthology/C18-1199) in Table 2. 

It is worth noting that the original SNLI dataset is not perfectly labeled, 
and 8.8\% of the sampled data is not assigned a `gold label`, 
implying the disagreement within human labelers. 
We admit the noisiness of SNLI-VE, which we believe is a common scenario in other large scale datasets, 

However, if the dataset quality is a major concern to you, 
we suggest dropping neutral examples and conduct experiments on **SNLI-VE-binary** task
(i.e. only use `entailment` and `contradiction` examples).
  

## Bibtex  
```  
@article{xie2019visual,
  title={Visual entailment: A novel task for fine-grained image understanding},
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
  
Thank you for your interest in our dataset! Please contact me at xie.25@wright.edu for any questions, comments, or suggestions! :-)  
  
<div align="center">  
    <img src="https://drive.google.com/uc?export=view&id=1c5vFLq4yrj1wcHDds5WEVoTjM-K039La" style="float:left" width="200px"> 
</div>
