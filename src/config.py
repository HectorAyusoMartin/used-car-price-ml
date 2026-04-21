from pathlib import Path

#Raiz del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

#Carpetas
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = BASE_DIR / "models"

PREPROCESSOR_FILE = MODELS_DIR / "preprocessor.pkl"

#Archivos
RAW_DATA_FILE = RAW_DATA_DIR / "cars.csv"
MODEL_FILE = MODELS_DIR / "model.pkl"

#Variable objetivo provisional:
TARGET_COLUMN = "selling_price"

#Hiper-parámetros
RANDOM_STATE = 7
TEST_SIZE = 0.2