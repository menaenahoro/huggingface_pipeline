from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from typing import Dict, List
import torch


tokenizer = AutoTokenizer.from_pretrained("./tokenizer/")

model = AutoModelForSequenceClassification.from_pretrained(
    "./models/")  # "finiteautomata/bertweet-base-sentiment-analysis"

pipe = pipeline(task="sentiment-analysis", model=model, tokenizer=tokenizer)

def data(data_set):
    for i in data_set:
        yield i


def get_results(data_set: List[str]):
    sentiment = []
    for out in pipe(data(data_set), truncation=True):
        sentiment.append(out)
    return sentiment

