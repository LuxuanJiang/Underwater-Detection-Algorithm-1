
# Underwater-Detection-Algorithm

[![Alt](https://img.shields.io/github/repo-size/Team-Coding-Like-Immortal/Underwater-Detection-Algorithm?color=blue&label=repo%20size&style=for-the-badge)](https://github.com/Team-Coding-Like-Immortal/Underwater-Detection-Algorithm/)

## 这是大创及各种比赛所使用的yolov3-水下目标检测算法

**里面包含了修改后的代码，视频检测，数据集处理代码等。**


# 文件目录内容解释
<details><summary><b>CLICK ME</b> - 文件目录内容解释</summary>
  

* `assets`:一些样本预测图，基本不用动
* `config`:yolov3神经网络的配置文件以及.data文件
* `data`:存放数据集的地方，里面是custom是存放自定义数据集的，里面有test.py和voc_label.py文件用来生成标签文件和数据集中的图片路径
* `other-utils`:存放各种杂七杂八的代码，都是yolo有关的，包含之前试着写的视频检测和摄像头检测
* `pyqt_ui`:未来打算用qt写一个界面方便使用，存放相关的.py和.ui文件
* `requirement`:存放了运行训练、检测、测试的指令，所需依赖，权重下载文件
* `utils`:存放关于yolo神经网络相关的方法和函数
* `detect.py`:检测图片
* `train.py`:训练模型
* `test.py`:测试模型
* `video_detect.py`:视频或者摄像头检测
* `models.py`:神经网络架构
</details>

## 运行代码
<details><summary><b>CLICK ME</b> - 运行代码</summary>
```bash
python train.py --model_def config/yolov3-custom.cfg --data_config config/custom.data --pretrained_weights weights/darknet53.conv.74
python test.py --weights_path weights/yolov3_ckpt_125.pth --data_config config/custom.data --class_path data/custom/classes.names --model_def config/yolov3-custom.cfg
python train.py --model_def config/yolov3-custom.cfg --data_config config/custom.data --pretrained_weights weights/yolov3_ckpt.pth --batch_size 693 --epochs 50 --checkpoint_interval 5
python detect.py --image_folder data/test --model_def config/yolov3-custom.cfg --weights_path weights/yolov3_ckpt.pth --class_path data/custom/classes.names
```
</details>
## 更新日志

- 2020.4.29 加入了摄像头检测
```diff
+ video_detect.py
```



