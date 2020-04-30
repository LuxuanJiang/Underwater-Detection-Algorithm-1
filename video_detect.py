from __future__ import division

from models import *
from utils.utils import *
from utils.datasets import *

import os
import sys
import time
import datetime
import argparse
import cv2 as cv

from PIL import Image

import torch
from torch.utils.data import DataLoader
from torchvision import datasets
from torch.autograd import Variable

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.ticker import NullLocator

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # parser.add_argument("--image_folder", type=str, default="data/test", help="path to dataset")
    parser.add_argument("--video_file", type=str, default="data/video/video.avi", help="path to dataset")
    parser.add_argument("--model_def", type=str, default="config/yolov3-custom.cfg", help="path to model definition file")
    parser.add_argument("--weights_path", type=str, default="weights/yolov3_ckpt.pth", help="path to weights file")
    parser.add_argument("--class_path", type=str, default="data/custom/classes.names", help="path to class label file")
    parser.add_argument("--conf_thres", type=float, default=0.8, help="object confidence threshold")
    parser.add_argument("--nms_thres", type=float, default=0.4, help="iou thresshold for non-maximum suppression")
    parser.add_argument("--batch_size", type=int, default=1, help="size of the batches")
    parser.add_argument("--n_cpu", type=int, default=0, help="number of cpu threads to use during batch generation")
    parser.add_argument("--img_size", type=int, default=416, help="size of each image dimension")
    parser.add_argument("--checkpoint_model", type=str, help="path to checkpoint model")
    parser.add_argument("--mode", type=str, default="camera", help="choose mode between video or camera")
    opt = parser.parse_args()
    print(opt)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # 创建输出文件夹
    os.makedirs("output", exist_ok=True)
    os.makedirs("output/video_image", exist_ok=True)
    # Set up model
    # 导入模型配置文件
    model = Darknet(opt.model_def, img_size=opt.img_size).to(device)
    # 判断是否使用.weights还是其他权重文件
    if opt.weights_path.endswith(".weights"):
        # Load darknet weights
        model.load_darknet_weights(opt.weights_path)
    else:
        # Load checkpoint weights
        model.load_state_dict(torch.load(opt.weights_path))
    model.cuda()
    # 切换评估模式
    model.eval()  # Set in evaluation mode
    # 获取类别
    classes = load_classes(opt.class_path)  # Extracts class labels from file
    # 转化为Tensor float类型
    Tensor = torch.cuda.FloatTensor if torch.cuda.is_available() else torch.FloatTensor

    if opt.mode == 'video':
        cap = cv.VideoCapture(opt.video_file)
        colors = np.random.randint(0,255,size=(len(classes),3),dtype="uint8")
    else:
        cap = cv.VideoCapture(0)
        colors = np.random.randint(0,255,size=(len(classes),3),dtype="uint8")

    # Bounding-box colors
    # 检测框的颜色
    # cmap = plt.get_cmap("tab20b")
    # colors = [cmap(i) for i in np.linspace(0, 1, 20)]
    img_detections = []
    # 开始检测
    print("\nPerforming object detection:")
    start = time.time()
    current_frame = 0
    while cap.isOpened():
        ret, frame = cap.read()
        # 将将numpy的矩阵转化成PIL 再将opencv中获取的BGR颜色空间转换成RGB
        PILimg = np.array(Image.fromarray(cv.cvtColor(frame, cv.COLOR_BGR2RGB)))
        imgTensor = transforms.ToTensor()(PILimg)
        imgTensor, _ = pad_to_square(imgTensor, 0)
        # resize图像变成416×416
        imgTensor = resize(imgTensor, 416)
        # 添加一个维度
        imgTensor = imgTensor.unsqueeze(0)
        imgTensor = Variable(imgTensor.type(Tensor))

        # 检测
        with torch.no_grad():
            detections = model(imgTensor)
            detections = non_max_suppression(detections, opt.conf_thres, opt.nms_thres)
        current_frame += 1
        img_detections.clear()
        if detections is not None:
            img_detections.extend(detections)
        length = len(img_detections)
        if length:
            for detections in img_detections:
                if detections is not None:
                    detections = rescale_boxes(detections, opt.img_size, PILimg.shape[:2])
                    unique_labels = detections[:, -1].cpu().unique()
                    n_cls_preds = len(unique_labels)
                    end = time.time()
                    time_count = end - start
                    for x1, y1, x2, y2, conf, cls_conf, cls_pred in detections:
                        print("\t+ Label: %s, Conf: %.5f, time: %d" % (classes[int(cls_pred)], cls_conf.item(),time_count))
                        box_w = x2 - x1
                        box_h = y2 - y1
                        color = [int(clr) for clr in colors[int(cls_pred)]]
                        frame = cv.rectangle(frame, (x1, y1 + box_h), (x2, x1), color, 2)
                        cv.putText(frame, classes[int(cls_pred)], (x1, y1), cv.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
                        cv.putText(frame, str("%.2f" % float(conf)), (x2, y2 - box_h), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                                   color, 2)
        cv.imshow('frame', frame)

        if cv.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break

cv.destroyAllWindows()