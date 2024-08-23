from abc import ABC, abstractmethod


class BaseTranslator(ABC): 

    def __init__(self, 
                 src:str, 
                 dst:str,
                 auto_clean:bool=False): 
        
        self.src = src
        self.dst = dst
        self.auto_clean = auto_clean

    
    @abstractmethod
    def translate(self, text) -> str: 
        raise NotImplementedError