from v2x.pre_processing import clean
from v2x.tools.base import BaseTranslator

class PyTranslator(BaseTranslator):

    def __init__(self, from_lang='vi', to_lang='en', auto_clean=False):
        super().__init__(from_lang=from_lang, to_lang=to_lang, auto_clean=auto_clean)
        try: 
            from translate import Translator

            if from_lang is None: 
                from_lang = 'autodetect'
            self.from_lang = from_lang

            self.translator = Translator(from_lang=self.from_lang, to_lang=self.to_lang)
        except ValueError: 
            raise ValueError('`translate` is not installed. Please try `pip install translate`')
        
    def translate(self, text: str) -> str:
        result = self.__call__(text)
        return result
    
    def __call__(self, text):
        if self.auto_clean: 
            text = clean(text)
        result = self.translator.translate(text)
        assert type(result) == str
        return result