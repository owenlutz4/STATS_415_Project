import pandas as pd
import os

def load_train_data(data_path='Downloads/STATS 415 Final Project/train'):
    """
    Load training data from specified path.
    
    Parameters:
    data_path : str
        Path to the folder containing X_train.txt and subject_train.txt
        Default is 'Downloads/STATS 415 Final Project/train'
    """
    try:
        X_train = pd.read_csv(os.path.join(data_path, 'X_train.txt'), 
                          delim_whitespace=True, 
                          header=None)
        
        subject_train = pd.read_csv(os.path.join(data_path, 'subject_train.txt'), 
                               header=None,
                               names=['subject_id'])
        
        train = pd.concat([subject_train, X_train], axis=1)
        print(f"Number of features (columns): {len(train.columns) - 1}")
        print(f"Number of samples (rows): {len(train)}")
        return train
        
    except FileNotFoundError:
        print(f"Could not find data files in {data_path}")
        print("Please specify the correct path to your data folder when calling the function")
        print("Example: train = load_train_data('path/to/your/data/folder')")
