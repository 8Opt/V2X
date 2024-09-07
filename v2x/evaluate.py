"""Evaluate methods
"""
import numpy as np
import nltk
from nltk.translate import meteor_score, chrf_score

import evaluate

nltk.download('wordnet')

def get_meteor_score(hyp, ref):
    try: 
        result = meteor_score.single_meteor_score(hyp, ref)
        return result
    except: 
        raise ImportError("`meteor` is not found locally. Please try `pip install meteor`")
def get_chrf_score(hyp, ref):
    result = chrf_score.sentence_chrf(hyp, ref)
    return result

def get_sacrebleu_score(hyp, ref):
    def postprocess_text(preds, labels):
        preds = [pred.strip() for pred in preds]
        labels = [[label.strip()] for label in labels]

        return preds, labels
    try: 
        sacrebleu = evaluate.load("sacrebleu")
        hyp, ref = postprocess_text(hyp, ref)
        result = sacrebleu.compute(predictions=hyp, references=ref)["score"]
        return result
    except: 
        raise ImportError("`sacrebleu` is not found locally. Please try `pip install sacrebleu`")

def get_rouge_score(hyp, ref):
    try: 
        rouge = evaluate.load('rouge')
        result = rouge.compute(predictions=hyp, references=ref)
        return result
    except: 
        raise ImportError("`rouge-score` is not found locally. Please try `pip install rouge-score`")