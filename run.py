import argparse
import torch
from PIL import Image
from strhub.data.module import SceneTextDataModule
from strhub.models.utils import load_from_checkpoint

def load(img, model_path):
    print(model_path)
    model = torch.load(model_path, map_location=torch.device('cpu'))

    parseq = load_from_checkpoint(model_path).eval()

    img_transform = SceneTextDataModule.get_transform(parseq.hparams.img_size)

    img = img_transform(img).unsqueeze(0)

    logits = parseq(img)
    logits.shape

    # Greedy decoding
    pred = logits.softmax(-1)
    label, confidence = parseq.tokenizer.decode(pred)
    print('Decoded label = {}'.format(label[0]))

    return label[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process image using the desired model")
    parser.add_argument("--model_path", required=True, help="Path to the Parseq model checkpoint")
    parser.add_argument("--image_path", required=True, help="Path to the input image")
    args = parser.parse_args()

    img_path = args.image_path
    model_path = args.model_path

    img = Image.open(img_path).convert('RGB')

    text = load(img, model_path)
    print(text)
