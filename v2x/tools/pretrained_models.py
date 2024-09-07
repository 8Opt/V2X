from typing import Tuple, Any
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from v2x.tools.base import BaseTranslator

TRANSLATION_CONFIG = {
    'max_new_tokens': 40, 
    'do_sample': True, 
    'top_k': 30, 
    'top_p': 0.95
}

class HFTranslator(BaseTranslator):
    """
    Translator class for Pre-Trained Models (PTMs).
    """

    def __init__(self, 
                 model_id: str='t5/small', 
                 llm_config: dict = None):
        """
        Initializes the PTMTranslator instance.

        Args:
            model_id (str): The ID of the pre-trained model.
            llm_config (dict, optional): The configuration for the Large Language Model (LLM). Defaults to None.
        """
        super().__init__()

        self.llm_config = llm_config or TRANSLATION_CONFIG  # Use the default config if not provided
        self.model_id = model_id

        try:
            self.tokenizer, self.model = self._load_pretrained_model(model_id)
        except ValueError as e:
            raise ValueError(f"`model_id` is in wrong format: {e}")

    def run(self, text: str) -> str:
        """
        Translates the input text using the pre-trained model.

        Args:
            text (str): The input text to be translated.

        Returns:
            str: The translated text.
        """
        input_ids = self.tokenizer(text, return_tensors="pt")["input_ids"]
        outputs = self.model.generate(input_ids, **self.llm_config)
        result = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return result

    def _load_pretrained_model(self, model_id: str) -> Tuple[AutoTokenizer, AutoModelForSeq2SeqLM]:
        """
        Loads the pre-trained model and tokenizer.

        Args:
            model_id (str): The ID of the pre-trained model.

        Returns:
            Tuple[AutoTokenizer, AutoModelForSeq2SeqLM]: The loaded tokenizer and model.
        """
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_id).eval()
        return tokenizer, model

    def __call__(self, input_ids) -> Any:
        """
        Calls the pre-trained model to generate the output.

        Args:
            input_ids: The input IDs for the model.

        Returns:
            Any: The output of the model.
        """
        outputs = self.model.generate(input_ids, **self.llm_config)
        return outputs