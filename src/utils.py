from pathlib import Path
import joblib


def ensure_directory(path: Path) -> None:
    """
    Crea el folder, si no existe antes.
    """
    path.mkdir(parents=True,exist_ok=True)
    return None

def save_pickle(obj, filepath: Path) ->None:

    """
    Guarda un objeto en disco duro usando joblib
    
    """
    joblib.dump(obj,filepath)
    return None

def load_pickle(filepath: Path):
    """
    Carga un objeto del disco con joblib
    """
    return joblib.load(filepath)