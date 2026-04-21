

def basic_data_check(df: pd.DataFrame)-> None:
    """
    Muestra una revisión básica del dataset.
    
    """

    print("\nPrimeras 5 filas:")
    print(df.head())

    print("\nForma del dataset:")
    print(df.shape)

    print("\nColumnas:")
    print(df.columns.tolist())

    print("\nTipo de datos:")
    print(df.dtypes)

    print("\nValores nulos por columna:")
    print(df.isnull().sum())