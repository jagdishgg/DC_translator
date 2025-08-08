from transformers import MarianMTModel, MarianTokenizer
import torch

model_name = "Helsinki-NLP/opus-big-mt-ar-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate_arabic_to_english(text):
    if not text.strip():
        return "Please enter Arabic text."
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    translated = model.generate(**inputs)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
