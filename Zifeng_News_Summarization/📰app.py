import streamlit as st
import transformers
from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer

access_token = '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'

st.title('📰News Summarization!')
st.subheader("Got no time to read those lengthy news articals?🧐")
st.write("Copy and paste your news article here and I will tell you what happened.😎")
model_name = st.selectbox("Pick a summarization model📊", ["T5 (Fast and small)", "PEGASUS(Large but slow)", "BART(Somwhere in between)"])
txt = st.text_area("📃News to summarize:", height=200)
submitted = st.button("🤖Generate summarization!")

def generate_response(txt, model_name):
    # Instantiate the LLM model and tokenizer
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name, token=access_token)
    tokenizer = AutoTokenizer.from_pretrained(model_name, token=access_token)
    # Text preprocessing
    news = 'summarize: '+ txt
    # Text summarization
    summarizer = pipeline("summarization", model = model, tokenizer = tokenizer, max_length = 100)
    summary = summarizer(news)
    return summary[0]['summary_text']

if submitted:
    if txt:
        if model_name == "T5 (Fast and small)":
            summary = generate_response(txt, 'A-C-E/t5-news')
        if model_name == "PEGASUS(Large but slow)":
            summary = generate_response(txt, 'A-C-E/pegasus-news')
        if model_name == "BART(Somwhere in between)":
            summary = generate_response(txt, 'A-C-E/bart-news')
        if len(summary):
            st.info(summary)
            st.write("Disclaimer:")
            st.write("This app uses the AI Large Language Models to generate news summarization, the summarization is just for reference.")
            st.write("The app may generate misleading or inaccurate information, be careful!")
            st.write("The final right of interpretation belongs to the app owner.")
    else:
        st.warning("Please input some news!")  # must have text input