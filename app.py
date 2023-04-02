# Core Pkg
import streamlit as st


# Additional Pkgs /Summarization Pkgs
# TextRank Algorithm

# LexRank Algorithm
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
# EDA Pkgs
import pandas as pd

# Data visualization
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg') # TkAgg # Backend

# import seaborn as sns
import altair as alt


def main():
    st.title("Summarizer App")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu", menu)


    if choice =="Home":
        st.subheader("Summarization")
        raw_text = st.text_area("Enter your text here")
        if st.button("Summarize"):

            with st.expander("Original text"):
                st.write(raw_text)

        #Layout

        c1, c2 = st.columns(2)

        with c1:
            with st.expander("LexRank Summary"):
                pass

        with c2:
            with st.expander("TextRank Summary"):
                pass

    else:
        st.subheader("About")




if __name__ == "__main__":
    main()
