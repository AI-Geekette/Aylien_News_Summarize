import streamlit as st
import pandas as pd
from makeRequests import *

# Function to generate the news content and summaries
def generate_news_data(word):
    # Here, you would have your own logic to fetch and process news data based on the provided word
    first_response = make_custom_request(custom_keyword = word)
    print("API NEWS RESPONSE: \n", first_response, '\n\n')
    clean_data = data_to_summarize(first_response['results'])
    print("CLEAN NEWS RESPONSE: \n", clean_data, '\n\n')
    
    summaries = summarize(clean_data["news_list"][:1])
    print(summaries)
    # Creating a pandas DataFrame for the news content and summaries
    df = pd.DataFrame(summaries['results'])

    return df

# Streamlit App
def main():
    # Set page title
    st.set_page_config(page_title="News Summarizer")

    # Set app title
    st.title("News Summarizer")

    # User input for word
    word = st.text_input("Enter a word")

    if st.button("Summarize"):
        df = generate_news_data(word)

        # Display original news content
        st.subheader("Original News")
        st.table(df["original_news"])

        # Display news summaries
        st.subheader("News Summaries")
        st.table(df["summarized_news"])

# Running the app
if __name__ == "__main__":
    main()
