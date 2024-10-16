import requests
from bs4 import BeautifulSoup
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import argparse


def get_webpage_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 503:
            print("Service Unavailable. Try again later or use a different website.")
        else:
            print(f"An error occurred: {e}")
        return
    soup = BeautifulSoup(response.content, 'html.parser')
    tag = soup.body
    text = ' '.join([string for string in tag.strings])
    return text

def analyze_sentiment(url):
    prompt_template = """
    Analyze the sentiment of the following text as postive, negative, or neutral.
    
    Webpage Text: {webpage_text}
    """
    prompt = ChatPromptTemplate.from_template(template = prompt_template)
    
    llama_llm = OllamaLLM(model="llama3.2:1b")
    
    # Fetch web page content
    webpage_text = get_webpage_content(url)
    if not webpage_text:
        return
    
    chain = prompt | llama_llm
    
    # Run the sentiment chain and get the result
    sentiment = chain.invoke({"webpage_text": webpage_text})
    
    return sentiment.strip(), webpage_text

# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="url to analyze sentiment of.")
    args = parser.parse_args()
    sentiment, text = analyze_sentiment(args.url)
    if sentiment:
        print(f"The webpage text is:\n {text}\n")
        print(f"The sentiment of the webpage is: {sentiment}") 
