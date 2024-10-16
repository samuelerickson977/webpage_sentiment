# webpage_sentiment
An LLM application to classify the sentiment of a webpage.

## Instructions
1. Install Anaconda:
```
wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh
bash Anaconda3-2024.06-1-Linux-x86_64.sh
```

2. Create and activate the environment. Replace <env> with the name
of your choosing:
```
conda create --name <env> --file spec-file.txt
conda activate <env>
```
3. Install and run ollama:
```
curl -fsSL https://ollama.com/install.sh | sh
pip install -U langchain-ollama
ollama pull llama3.2
ollama run llama3.2:1b
```

4. Try an example to see if it looks similar to this output:

```
python3 analyze_sentiment.py http://example.com
The webpage text is:
 
 
 Example Domain 
 This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission. 
 More information... 
 


The sentiment of the webpage is: I would analyze the sentiment of this text as neutral. 
The language used is straightforward and informative, with a tone that is neither 
encouraging nor discouraging. There are no emotional appeals, phrases that express 
strong opinions, or language that conveys irony or sarcasm. Overall, the text 
presents a factual statement about using the example domain without expressing 
any emotional tone.
```

