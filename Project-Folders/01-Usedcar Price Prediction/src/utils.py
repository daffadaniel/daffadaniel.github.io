import joblib
import pandas as pd

def load_data(fname: str) -> pd.DataFrame:
  """
  Read a CSV file and return a DataFrame

  Args: 
      fname (str): path to the CSV file to be read.

  Returns:
      data (pd.DataFrame)
  """
  data = pd.read_csv(fname, index_col='id')
  print("Data Shape: ", data.shape)
  return data

def split_input_output(data: pd.DataFrame, target_col: str):
    """
    Split predictor variables with target variables 
    
    Args: 
        data (pd.DataFrame): Data to be split
        target_col (str): target variable in the data
    
    Returns:
        X (pd.DataFrame): predictor variables
        y (pd.Series): target variables
    """
    X = data.drop(columns = target_col)
    y = data[target_col]
    print(f"Original data shape: {data.shape}") 
    print(f"X data shape: {X.shape}")
    print(f"y datashape: {y.shape}")
    return X,y 


def serialize_data(data: pd.DataFrame, path: str):
    """
    Saves data to a file in pickle format (.pkl) using joblib.

    Args:
        data (e.g. pd.DataFrame): Data to be saved. 
        path (str): Full path to the file storage location, including the file name and extension (.pkl).

    Returns:
        None
    """
    joblib.dump(data, path)

def deserialize_data(path: str):
    """
    Deserialize (load) data from a file stored in pickle format using joblib.

    Args:
        path (str): Address or path of the file where the data is stored.

    Returns:
        data (pd.DataFrame): Deserialized data.
    """
    data =  joblib.load(path)
    return data
