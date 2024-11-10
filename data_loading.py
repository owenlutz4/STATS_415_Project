import pandas as pd

def load_train_data():
    X_train = pd.read_csv('Downloads/STATS 415 Final Project/train/X_train.txt', 
                          delim_whitespace=True, 
                          header=None)
    
    subject_train = pd.read_csv('Downloads/STATS 415 Final Project/train/subject_train.txt', 
                               header=None,
                               names=['subject_id'])
    
    train = pd.concat([subject_train, X_train], axis=1)
    return train

if __name__ == "__main__":
    # This will run only if the script is run directly
    train = load_train_data()
    print(f"Number of features (columns): {len(train.columns) - 1}")
    print(f"Number of samples (rows): {len(train)}")
