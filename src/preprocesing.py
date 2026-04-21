import pandas as pd

def group_rare_fuel_types(df: pd.DataFrame)-> pd.DataFrame:

    """
    Agrupa categorías minoritarias de la columna 'fuel' en 'Other
    
    """
    df_copy = df.copy()

    rare_fuels = ["CNG", "LPG", "Electric"]
    df_copy["fuel"] = df_copy["fuel"].replace(rare_fuels, "Other")

    return df_copy

def select_model_columns(df: pd.DataFrame)-> pd.DataFrame:
    """
    Selecciona las columnas que se utilizarán en el modelo
    """
    df_copy = df.copy()

    selected_columns = [
        "brand",
        "car_age",
        "km_driven",
        "km_per_year",
        "fuel",
        "seller_type",
        "transmission",
        "owner",
        "selling_price"
    ]

    return df_copy[select_model_columns]

def split_features_target(df: pd.DataFrame, target_col:str) -> tuple[pd.DataFrame,pd.Series]:
    """
    Separa el dataframe en variables predictoras (X) y variable objetivo (y).
    """
    df_copy = df.copy()

    X = df_copy.drop(columns=[target_col])
    y = df_copy[target_col]

    return X, y

def get_columns_types(X: pd.DataFrame):
    """
    Detecta columnas numéricas y categóricas dentro de X.
    """
    numerical_cols = X.select_dtypes(include=["int64","float64","number"]).columns.tolist()
    categorical_cols = X.select_dtypes(include=["object","category"]).columns.to_list()

    return numerical_cols, categorical_cols

