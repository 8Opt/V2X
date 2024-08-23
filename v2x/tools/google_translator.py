from v2x.pre_processing import clean
from v2x.tools.base import BaseTranslator

class GoogleTranslator(BaseTranslator):

    def __init__(self, from_lang=None, to_lang='en', auto_clean=False):
        super().__init__(from_lang=from_lang, to_lang=to_lang, auto_clean=auto_clean)
        try: 
            from googletrans import Translator

            if from_lang is None: 
                from_lang = 'auto'
            self.from_lang = from_lang
            self.translator = Translator()
        except ValueError: 
            raise ValueError('`googletrans` is not installed. Please try `pip install googletrans`')
    
    def translate(self, text: str) -> str:
        result = self.__call__(text)
        return result
    
    def __call__(self, text):
        if self.auto_clean: 
            text = clean(text)
        result = self.translator.translate(text, dest=self.to_lang, src=self.from_lang).text
        assert type(result) == str
        return result