# pip install torch torchvision pillow
import torch
from torchvision import models, transforms
from PIL import Image
import requests
model = models.resnet50(pretrained=True)
model.eval()
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])
labels_url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
labels = requests.get(labels_url).text.split("\n")
def predict_image(image_path):

    image = Image.open(image_path).convert("RGB")
    img = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(img)

    _, predicted = torch.max(outputs,1)

    print("Prediction:", labels[predicted.item()])

predict_image("test1.jpg")