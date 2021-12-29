# CHOICE COIN AI/ML CHATBOT

Building a project that can be actualised by using practical machine learning algorithms to build an AI Powered Bot to educate and communicate the idea behind Choice Coin which involves promoting decentralised voting processes.

## TECHNOLOGIES USED IN THIS PROJECT
1. Language -----> Python

2. Pytorch
    Install PyTorch and dependencies

      For Installation of PyTorch see [official website](https://pytorch.org/).

    You also need nltk:

    pip install nltk

        If you get an error during the first run, you also need to install nltk.tokenize.punkt: Run this once in your terminal:

            $ python
              >>> import nltk
              >>> nltk.download('punkt')

3. NLTK (Natural Language Toolkit)

N/B: The patterns and responses used in the intents.json file was extracted from https://choice-coin.com/


### To run this code at your own convinence

clone the repo
cd into the project and activate a virtual environment
Mac / Linux:
```console
. venv/bin/activate
```
Windows:
```console
venv\Scripts\activate
``` 
Install dependencies
You can modify the intents.json or customize the patterns and responses 
Run
```console
python train.py
```
This will dump `data.pth` file. And then run
```console
python chat.py
```