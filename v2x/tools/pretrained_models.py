from typing import Tuple, Any
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from v2x.tools.base import BaseTranslator

TRANSLATION_CONFIG = {
    'max_new_tokens': 40, 
    'do_sample': True, 
    'top_k': 30, 
    'top_p': 0.95
}

class PTMTranslator(BaseTranslator): 

    def __init__(self, model_id, llm_config):
        super().__init__()

        if llm_config: 
            self.llm_config = llm_config
        else: 
            self.llm_config = TRANSLATION_CONFIG

        try: 
            if model_id: 
                self.tokenizer, self.model = self.call_pretrained(model_id)
        except ValueError: 
            raise ValueError("`model_id` is in wrong format, which means that either it is not ")
        
    def translate(self, text: str) -> str:
        input_ids = self.tokenizer(text, return_tensors="pt")["input_ids"]
        outputs = self.__call__(input_ids)
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result
    

    def __call__(self, input_ids) -> Any:
        outputs = self.model.generate(input_ids, **self.llm_config)
        return outputs
    

    def call_pretrained(self, model_id) -> Tuple[AutoTokenizer, AutoModelForSeq2SeqLM]: 
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_id).eval()
        return (tokenizer, model)  
    