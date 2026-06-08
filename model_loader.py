import torch
from torchvision import models

def load_model():
    model = models.mobilenet_v3_small(weights="DEFAULT")

    model.eval()

    return model
