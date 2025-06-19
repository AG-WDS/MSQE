# MSQE

Maize Seedling Quality Evaluation with Oriented YOLO11-Mamba and UAV-RGB Images

![image-20250619144055795](https://typora119.oss-cn-shenzhen.aliyuncs.com/image-20250619144055795.png)

# Dataset

The MSQE dataset is available at

 `https://drive.google.com/file/d/1nPxlaaaNF4921lwNrGjBLbmk-mnYYoRL/view?usp=drive_link`


# Setup

Preparing the Code

    git clone https://github.com/AG-WDS/MSQE.git
    cd MSQE/YOLO-Mamba

Install the mamba dependencies

    pip install ultralytics
    pip install causal-conv1d>=1.1.2
    pip install mamba-ssm>=1.1.2

Requirement

```
python>=3.8.0 
pytorch-cuda==11.3
torch==1.12.1
```

## Acknowledgement

This repo is modified from open source real-time object detection codebase [Ultralytics](https://github.com/ultralytics/ultralytics)
