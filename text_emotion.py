from transformers import pipeline
from transformers import FlaubertForSequenceClassification
from transformers import AutoTokenizer


def get_emotion(text):
    model_name = 'flaubert/flaubert_small_cased'
    classifier = pipeline('sentiment-analysis', model=model_name, tokenizer=model_name)
    result = classifier(text)
    return result[0]['label']


# Les prédictions possibles sont : "colère", "joie", "peur", "s tristesse", "surprise"
#   0 : colère
#   1 : joie
#   2 : peur
#   3 : tristesse
#   4 : surprise

def get_emotionV2(text):
    model = FlaubertForSequenceClassification.from_pretrained("flaubert/flaubert_small_cased")
    tokenizer = AutoTokenizer.from_pretrained("flaubert/flaubert_small_cased")
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    outputs = model(input_ids)
    print (outputs)
    predictions = outputs.logits.argmax(dim=1)
    print (predictions)

    émotion_dominante = predictions.item()
    print(f"L'émotion dominante dans votre texte est : {émotion_dominante}")
    return émotion_dominante

    


