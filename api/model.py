import spacy




def load_model(model_path: str):
    model = spacy.load(model_path)
    return model


