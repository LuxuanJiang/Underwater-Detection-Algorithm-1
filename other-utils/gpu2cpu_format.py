# import torch
# from models import *
# from utils.utils import *
# from utils.datasets import *
# from utils.parse_config import *
# from torchvision import models
# pth_file = r'weights/yolov3_ckpt.pth'
# epochs = range(18)
#
# # for i in epochs:
# #     pth_file = r'model/yolov3_ckpt_%s.pth'% i
# #     net = torch.load(pth_file,map_location=torch.device('cuda'))
#
# # net = torch.load(pth_file,map_location=torch.device('cuda'))
# # net = torch.load(pth_file)
#
# # print(net['module_list.105.conv_105.weight'])
#
# # for key,value in net["model"].items():
# #     print(key,value.size(),sep="    ")
#
# weight = torch.load('weights/yolov3_ckpt.pth',map_location='cpu') # weights/yolov3_ckpt.pth 是我在Darknet上面训练好的模型
# Darknet = Darknet('config/yolov3-custom.cfg')
# Darknet.load_state_dict(weight)  # load_state_dict()函数表示导入当前权值，因为这个权值都是以字典的形式保存的
#

import torch

original = torch.load('weights/yolov3_ckpt.pth')
# print(original)
new = {"model": original['module_list.105.conv_105.weight']}
torch.save(new, 'weights/yolov3-custom.weights')
