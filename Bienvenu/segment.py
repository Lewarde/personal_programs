import torch
from torchvision.models.segmentation import deeplabv3_resnet101, DeepLabV3_ResNet101_Weights
from PIL import Image

weights = DeepLabV3_ResNet101_Weights.DEFAULT
model = deeplabv3_resnet101(weights=weights).eval()
preprocess = weights.transforms()

def segment_image(image_path, resize_to=(320, 240)):
    image = Image.open(image_path).convert("RGB")
    if resize_to:
        image = image.resize(resize_to)

    input_tensor = preprocess(image).unsqueeze(0)

    with torch.no_grad():
        output = model(input_tensor)['out'][0]

    output_predictions = output.argmax(0).byte().cpu().numpy()
    return output_predictions != 0 
