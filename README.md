# MSQE

# Maize Seedling Quality Evaluation with Oriented YOLO11-Mamba and UAV-RGB Images

![Fig.1](https://typora119.oss-cn-shenzhen.aliyuncs.com/Fig.1.svg)

# Dataset

Diff
 - The dataset and code are restricted to validation and comparative analysis. Any use of this data for independent publications is prohibited in the absence of additional licensing or permissions

The MSQE dataset is available at

 `https://drive.google.com/file/d/1nPxlaaaNF4921lwNrGjBLbmk-mnYYoRL/view?usp=drive_link`


# Setup

Preparing the Code

    git clone https://github.com/AG-WDS/MSQE.git
    cd MSQE/YOLO11-Mamba

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
# Citations
    @article
    {Minghu Zhao,2025,
        tilte={Evaluating maize emergence quality with multi-task YOLO11-Mamba and UAV-RGB remote sensing},
        author={Minghu Zhao, Dashuai Wang*, Gan Zhang, Wujing Cao, Sheng Xu, Zhuolin Li, Xiaoguang Liu*},
        journal={Smart Agricultural Technology},
        doi={https://doi.org/10.1016/j.atech.2025.101351},
        volume={12},
        pages={101351},
        year={2025}
    } 
# Acknowledgement

This repo is modified from open source real-time object detection codebase [Ultralytics](https://github.com/ultralytics/ultralytics)
