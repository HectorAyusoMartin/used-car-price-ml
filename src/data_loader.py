import pandas as pd
from src.config import RAW_DATA_FILE

def load_raw_data() -> pd.DataFrame:
    """
    Carga el dataset bruto desde data/raw/cars.csv.
    """

    if not RAW_DATA_FILE.exists():
        raise FileNotFoundError(f"No se encontró el archivo de datos en: {RAW_DATA_FILE}")
    
    df = pd.read_csv(RAW_DATA_FILE)
    return df


def load_processed_data():
    pass