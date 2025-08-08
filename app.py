import streamlit as st
from translate_ar_to_en import translate_arabic_to_english
from translate_ar_to_en import simple_lang_detect
from translate_ar_to_en load_models

st.title("DC Arabic to English and viceversa Translator")
st.markdown("Use Transliteration button for person or entity names")
text = st.text_area("Enter text (English or Arabic):", height=150)

if st.button("Translate"):
		 if text.strip():
		 		 try:
		 		 		 detected_lang = simple_lang_detect(text)
		 		 		 models = load_models()

		 		 		 if detected_lang == "en":
		 		 		 		 st.info("Detected language: English → Arabic")
		 		 		 		 tokenizer = models["en-ar"]["tokenizer"]
		 		 		 		 model = models["en-ar"]["model"]
		 		 		 elif detected_lang == "ar":
		 		 		 		 st.info("Detected language: Arabic → English")
		 		 		 		 tokenizer = models["ar-en"]["tokenizer"]
		 		 		 		 model = models["ar-en"]["model"]
		 		 		 else:
		 		 		 		 st.info("Detected language: English → Arabic")
		 		 		 		 tokenizer = models["en-ar"]["tokenizer"]

		 		 		 output = translate(text, tokenizer, model)
		 		 		 st.success("Translation:")
		 		 		 st.write(output)

		 		 except Exception as e:
		 		 		 st.error(f"Error: {str(e)}")
		 else:
		 		 st.warning("Please enter some text.")