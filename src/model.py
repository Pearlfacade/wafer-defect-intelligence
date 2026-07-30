from torchvision.models import resnet18
import torch.nn as nn

def get_model(num_classes=9, pretrained=True):
    model = resnet18(pretrained=pretrained)
    model.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)
    model.fc = nn.Linear(512, num_classes)
    return model