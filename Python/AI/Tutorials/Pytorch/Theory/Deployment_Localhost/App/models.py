from torchvision import models
from torch import nn


def create_resNet18(num_classes=10):

    # Creating EffNetB2 pretrained Weights, Transforms and Model
    weights = models.ResNet18_Weights.DEFAULT
    transforms = weights.transforms()
    resNet = models.resnet18(weights=weights)

    # Freezing all layers in Base Model
    for param in resNet.parameters():
        param.requires_grad = False

    # Changing the Classifier Head
    resNet.fc = nn.Linear(resNet.fc.in_features, num_classes)
    
    return resNet, transforms
