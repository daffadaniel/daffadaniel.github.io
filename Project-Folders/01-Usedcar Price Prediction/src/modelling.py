from pathlib import Path
from src.utils import *
from src.preprocessing import *
from lightgbm import LGBMRegressor

# Paths to the model, scaler, imputer, and encoder
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH   = BASE_DIR / "models" / "lgb_rand.pkl"
SCALER_PATH  = BASE_DIR / "models" / "scaler.pkl"
IMPUTER_PATH = BASE_DIR / "models" / "imputer.pkl"
ENCODER_PATH = BASE_DIR / "models" / "OHencoder.pkl"

def load_models():
    model = deserialize_data(str(MODEL_PATH))
    scaler = deserialize_data(str(SCALER_PATH))
    imputer = deserialize_data(str(IMPUTER_PATH))
    encoder = deserialize_data(str(ENCODER_PATH))
    return model, scaler, imputer, encoder

def predict(data: pd.DataFrame):
    """
    data: DataFrame with the same columns as during training
    return: prediction array
    """
    # Step 1: Load model & scaler
    model, scaler, imputer, encoder = load_models()
    
    # Step 2: preprocessing
    data_clean = preprocessing_pipeline(data, imputer, scaler, encoder)
    
    # Step 3: Prediction
    preds = model.predict(data_clean)
    return preds