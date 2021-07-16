import time
import torch
import numpy as np
from preprocessing import preprocessing

from bentoml import env, artifacts, api, BentoService
from bentoml.adapters import JsonInput, JsonOutput
from bentoml.frameworks.pytorch import PytorchModelArtifact
from bentoml.service.artifacts.common import PickleArtifact

class_name = ("Non-toxic","Toxic")

@env(infer_pip_packages=True)
@artifacts([PickleArtifact('tokenizer'), PytorchModelArtifact('model')])
class ToxicspeechClassifier(BentoService):
    @api(input=JsonInput()) # input:{"sent1": "sent1", "sent2": "sent2"}
    def predict(self, parsed_json):
        start_time = time.time() #inference time 측정 시작
        if parsed_json['sent2']: #If 2 setntents are input
            text = preprocessing([parsed_json['sent1'],parsed_json['sent2']])
        else:
            text = preprocessing(parsed_json['sent1'])

        encoded_texts = self.artifacts.tokenizer(text, max_length=512,
                                                pad_to_max_length=True,
                                                truncation=True,
                                                return_attention_mask=False,
                                                return_tensors='pt')
        
        input_id=encoded_texts['input_ids']
        # 어텐션 마스크를 패딩이 아니면 1, 패딩이면 0으로 설정
        # 패딩 부분은 BERT 모델에서 어텐션을 수행하지 않아 속도 향상
        masks = []
        
        for seq in input_id:
            seq_mask = [float(i>0) for i in seq]
            masks.append(seq_mask)
        masks = torch.tensor(masks)

        model = self.artifacts.model
        model.eval()
        outputs = model(input_ids=input_id, attention_mask=masks, token_type_ids=None)
        logits = outputs[0].detach().cpu().numpy()
    
        return {'predicted label':class_name[np.argmax(logits)], 'inference time': time.time()-start_time}