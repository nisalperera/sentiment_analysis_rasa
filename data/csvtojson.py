import json
import re

import pandas as pd


def load_csv():
    data = pd.read_csv("DataSetForWorkersEmotions.txt", delimiter='\t')
    # print(data)
    convert_json(data)


def convert_json(data):
    common_examples = []
    for emotion, text in zip(data['emotion'], data['text']):
        json_obj = {}
        json_obj['text'] = clean_text(text)
        json_obj['intent'] = emotion
        json_obj['entities'] = []
        common_examples.append(json_obj)

    # print(common_examples)

    json_format = pd.read_json("data.json")
    # print(json_format['rasa_nlu_data']['common_examples'])

    json_format = {
                    "rasa_nlu_data": {
                    "regex_features": [],
                    "entity_synonyms": [],
                    "common_examples": common_examples
                    }
                  }

    with open("./data.json", 'w') as outfile:
        json.dump(json_format, fp=outfile, indent=4)


def clean_text(text):
    text = re.sub(r"<br />", " ", text)
    text = re.sub(r"[^a-z]", " ", text)
    text = re.sub(r" {3}", " ", text)
    text = re.sub(r" {2}", " ", text)

    return text


load_csv()
