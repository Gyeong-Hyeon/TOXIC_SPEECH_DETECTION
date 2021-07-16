import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from toxic_classifier import ToxicspeechClassifier

tokenizer = AutoTokenizer.from_pretrained("mrm8488/distilroberta-finetuned-tweets-hate-speech")
model = AutoModelForSequenceClassification.from_pretrained("mrm8488/distilroberta-finetuned-tweets-hate-speech")
model.load_state_dict(torch.load('./pretrainedmodel/ds2_vl_0.3701.pth', map_location=torch.device('cpu')))

svc = ToxicspeechClassifier()
svc.pack('tokenizer', tokenizer)
svc.pack('model', model)

saved_path = svc.save()
#ToxicspeechClassifier:20210708203157_95C61B