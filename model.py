from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    model.eval()
    return processor, model

def generate_caption(processor, model, image: Image.Image):
    inputs = processor(image, "a picture of", return_tensors="pt")
    with torch.no_grad():
        ids = model.generate(**inputs, output_scores=True, return_dict_in_generate=True, max_new_tokens=50)
    
    caption = processor.decode(ids.sequences[0], skip_special_tokens=True)
    
    # Estimate confidence from sequence scores
    if ids.scores:
        import math
        scores = [torch.softmax(s, dim=-1).max().item() for s in ids.scores]
        confidence = round(sum(scores) / len(scores), 2)
    else:
        confidence = 0.85

    return caption, confidence
