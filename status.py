import torch
from nets.yolo3 import yoloBody
print(torch.__version__)
print(torch.cuda.is_available())