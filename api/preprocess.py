from collections import defaultdict
import re


def clean_text(text):
    text = re.sub(r"[^\w\s]", "", text)  # Remove special characters
    if(len(text)>1 and text[1]>='a' and text[1]<'z'):
        text = text.title()
    return text.strip() 

def preprocess(model, text:str):
    doc = model(text)
    categorized_skills = defaultdict(set)
    for ent in doc.ents:
        # print(ent.text, '--->', ent.label_)
        key = clean_text(ent.label_)
        value = clean_text(ent.text)
        categorized_skills[key].add(value)
    categorized_skills = dict(categorized_skills)
    return categorized_skills

