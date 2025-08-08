from transformers import MarianMTModel, MarianTokenizer
import torch

DetectorFactory.seed = 0 

import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
import torch
import langdetect
import sentencepiece
from langdetect import detect, DetectorFactory
import gradio as gr


@st.cache_resource
def load_models():
    models = {
     "en-ar": {
     "name": "Helsinki-NLP/opus-mt-en-ar",
 "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-tc-big-en-ar"),
 "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-tc-big-en-ar")
 },
 "ar-en": {
 "name": "Helsinki-NLP/opus-mt-ar-en",
 "tokenizer": MarianTokenizer.from_pretrained("Helsinki-NLP/opus-mt-tc-big-ar-en"),
 "model": MarianMTModel.from_pretrained("Helsinki-NLP/opus-mt-tc-big-ar-en")
}
 }
    return models
    
    


def translate(text, tokenizer, model):
    tokens = tokenizer([text], return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)
