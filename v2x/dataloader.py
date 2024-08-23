import pandas as pd

from dataset.synthetic import synthetic_dataset


class DataLoader: 
    
    def __init__(self): 
        self.dataset = pd.DataFrame(synthetic_dataset)

    def __len__(self): 
        return len(self.dataset)
    
    def __getitem__(self, idx): 
        sample = self.dataset.iloc[idx, :]
        return sample.to_dict()