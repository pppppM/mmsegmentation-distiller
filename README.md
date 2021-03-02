# mmsegmentation-distiller

This project is based on mmsegmentation(v-0.11.0), all the usage is the same as [mmsegmentation](https://mmsegmentation.readthedocs.io/en/latest/) including training , test and so on.

# Distiller Zoo



- [x] [Channel-wise Distillation for Semantic Segmentation](https://github.com/pppppM/mmsegmentation-distiller/tree/master/configs/distiller/cwd)
- [ ] [Structured Knowledge Distillation for Semantic Segmentation](https://arxiv.org/abs/1903.04197)



# Installation

* Set up a new conda environment: `conda create -n distiller python=3.7`

* Install pytorch

* [Install mmcv ( 1.2.4 <= mmcv-full < 1.3 )](https://github.com/open-mmlab/mmcv#installation)

* Install mmdetection-distiller

  ```bash
  git clone https://github.com/pppppM/mmsegmentation-distiller.git
  cd mmsegmentation-distiller
  pip install -r requirements/build.txt
  pip install -v -e .
  ```

# Train

```
#single GPU
python tools/train.py configs/distiller/cwd/cwd_psp_r101-d8_distill_psp_r18_d8_512_1024_80k_cityscapes.py

#multi GPU
bash tools/dist_train.sh configs/distillers/cwd/cwd_psp_r101-d8_distill_psp_r18_d8_512_1024_80k_cityscapes.py 8
```

# Test

```
#single GPU
python tools/test.py configs/distillers/cwd/cwd_psp_r101-d8_distill_psp_r18_d8_512_1024_80k_cityscapes.py $CHECKPOINT --eval mIoU

#multi GPU
bash tools/dist_test.sh configs/distillers/cwd/cwd_psp_r101-d8_distill_psp_r18_d8_512_1024_80k_cityscapes.py $CHECKPOINT 8 --eval mIoU
```

# Lisence

This project is released under the [Apache 2.0 license](LICENSE).
