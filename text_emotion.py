from transformers import pipeline
from transformers import FlaubertForSequenceClassification
from transformers import AutoTokenizer


def get_emotion(text):
    model_name = 'flaubert/flaubert_small_cased'
    classifier = pipeline('sentiment-analysis', model=model_name, tokenizer=model_name)
    result = classifier(text)
    return result[0]['label']

def get_emotionV2(text):
    model = FlaubertForSequenceClassification.from_pretrained("flaubert/flaubert_small_cased")
    tokenizer = AutoTokenizer.from_pretrained("flaubert/flaubert_small_cased")
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    outputs = model(input_ids)
    predictions = outputs.logits.argmax(dim=1)

    # Les prédictions possibles sont : "colère", "joie", "peur", "s tristesse", "surprise"
    émotion_dominante = predictions.item()
    print(f"L'émotion dominante dans votre texte est : {émotion_dominante}")
    return émotion_dominante

    


