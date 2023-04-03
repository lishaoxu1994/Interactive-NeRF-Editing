# Interactive Geometry Editing of Neural Radiance Fields
Code for our paper:
> **Interactive Geometry Editing of Neural Radiance Fields**
> <br>Shaoxu Li, Ye Pan<br>


<div align=center><img src="demo_mic.gif"/></div>

<div align=center><img src="demo_pinecone.gif"/></div>

## Installation
  ## Dependencies
  - PyTorch 1.4
  - matplotlib
  - numpy
  - imageio
  - imageio-ffmpeg
  - configargparse

## How To Run?
Download data for two example datasets: `lego` and `fern`
```
bash download_example_data.sh
```
To train a low-res `lego` NeRF:
```
python run_nerf.py --config configs/lego.txt
```
To render a edited `lego` NeRF:
```
python run_nerf_edit.py --config configs/lego.txt
```
Sorry for not finishing the interface design. You can define the cages in "run_nerf_edit.py" line 29-40. You can choose to use boxs or directly indicate some control points by setting "box_cage" and other parameters.

## Comments

- Our codebase is based on the [nerf](https://github.com/bmild/nerf) implemented by [nerf-pytorch](https://github.com/yenchenlin/nerf-pytorch).
## BibTeX

```
@misc{li2023interactive,
      title={Interactive Geometry Editing of Neural Radiance Fields}, 
      author={Shaoxu Li and Ye Pan},
      year={2023},
      eprint={2303.11537},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
## Related Work

```
@inproceedings{mildenhall2020nerf,
  title={NeRF: Representing Scenes as Neural Radiance Fields for View Synthesis},
  author={Ben Mildenhall and Pratul P. Srinivasan and Matthew Tancik and Jonathan T. Barron and Ravi Ramamoorthi and Ren Ng},
  year={2020},
  booktitle={ECCV},
}
@misc{lin2020nerfpytorch,
  title={NeRF-pytorch},
  author={Yen-Chen, Lin},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished={\url{https://github.com/yenchenlin/nerf-pytorch/}},
  year={2020}
}
```
