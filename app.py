import streamlit as st
from translate_ar_to_en import translate_arabic_to_english

st.set_page_config(page_title="Arabic to English Translator", layout="centered")
st.title("🇸🇦 Arabic ➝ English Translator")
st.markdown("Translate Arabic to English using Helsinki-NLP model.")

input_text = st.text_area("✍️ Enter Arabic text", height=150)

if st.button("🔁 Translate"):
    with st.spinner("Translating..."):
        output = translate_arabic_to_english(input_text)
        st.success("✅ Translation Complete")
        st.text_area("📝 English Translation", value=output, height=150)
