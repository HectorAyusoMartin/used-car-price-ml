import pandas as pd
from datetime import datetime

def extract_brand(df: pd.DataFrame)-> pd.DataFrame:

    """
    Extrae la marca del modelo desde la columna 'name'.

    Usa la primera palabra del nombre, con la excepcion de 
    'Land Rover', que usa las dos.
    
    """

    df_copy = df.copy()
    
    df_copy["brand"] = df_copy["name"].apply(
        lambda x : "Land Rover" if x.startswith("Land Rover") else x.split()[0]
    )

    return df_copy

def create_car_age(df: pd.DataFrame) -> pd.DataFrame:
    
    """Crea la columna {car_age} a partir de {year}"""

    df_copy = df.copy()
    current_year = datetime.now().year
    df_copy["car_age"] = current_year - df_copy["year"]
    return df_copy

def create_km_per_year(df: pd.DataFrame)->pd.DataFrame:

    """ 
    Crea la columna {km_per_year} a razón de dividir {km_driven} / {car_age}.
    La lógica de + 1 a {car_age} es que no pueda tener valor 0 ningun coche, y 
    asi evitar el error matemático div/Zero
    
    """

    df_copy = df.copy()
    df_copy["km_per_year"] = (df_copy["km_driven"] / (df_copy["car_age"] + 1)).astype(int)
    return df_copy

