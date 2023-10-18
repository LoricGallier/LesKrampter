from transformers import pipeline


def get_emotion(text):
    classifier = pipeline('sentiment-analysis')
    result = classifier(text)
    return result[0]['label']


