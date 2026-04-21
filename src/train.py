#--------------------------------------------------------------------------------------------

#Imports

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, OrdinalEncoder
from xgboost import XGBRegressor

from src.config import TARGET_COLUMN, RANDOM_STATE, TEST_SIZE, MODEL_FILE, PREPROCESSOR_FILE, MODELS_DIR
from src.data_loader import load_raw_data
from src.features import extract_brand, create_car_age, create_km_per_year
from src.preprocessing import group_rare_fuel_types, select_model_columns,split_features_target
from src.evaluate import evaluate_regression
from src.utils import ensure_directory, save_pickle

#---------------------------------------------------------------------------------------------


def main():

    print("Training started...")
    df = load_raw_data()

    df = extract_brand(df)
    df = create_car_age(df)
    df = create_km_per_year(df)

    df = group_rare_fuel_types(df)
    df = select_model_columns(df)

    X,y = split_features_target(df, TARGET_COLUMN) 

    
    #Split para obtener datos de validación añadidos para hacer funcionar el early stoping del modelo XGBoost:

    X_train_full, X_test, y_train_full, y_test = train_test_split(

        X,
        y,
        test_size = TEST_SIZE,
        random_state = RANDOM_STATE
    )
    
    #sacamos los datos de validación early stop desde el bloque de entrenamiento(train)

    X_train, X_val, y_train, y_val = train_test_split(

        X_train_full,
        y_train_full,
        test_size = 0.25,
        random_state=RANDOM_STATE
    )

    numerical_features = ["car_age","km_driven","km_per_year"]
    nominal_features = ["brand","fuel","seller_type","transmission"]
    ordinal_features = ["owner"]
    owner_order = [["Test Drive Car","First Owner","Second Owner","Third Owner","Fourth & Above Owner"]]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num","passthrough",numerical_features),
            ("nom", OneHotEncoder(handle_unknown="ignore"),nominal_features),
            ("ord",OrdinalEncoder(categories=owner_order),ordinal_features)
        ]
    )

    X_train_prepared = preprocessor.fit_transform(X_train)
    X_val_prepared = preprocessor.transform(X_val)
    X_test_prepared = preprocessor.transform(X_test)



    model = XGBRegressor(
        n_estimators = 1000,
        learning_rate=0.05,
        max_depth = 6,
        random_state = RANDOM_STATE,
        objective="reg:squarederror",
        early_stopping_rounds=50
    )

    model.fit(
        X_train_prepared,
        y_train,
        eval_set=[(X_val_prepared,y_val)],
        verbose = False
    )

    preds = model.predict(X_test_prepared)
     
    metrics = evaluate_regression(y_test, preds)
    print('Training completed.')
    print(metrics)

    ensure_directory(MODELS_DIR)
    save_pickle(model,MODEL_FILE)
    save_pickle(preprocessor, PREPROCESSOR_FILE)
    print("Artifacts saved successfully.")
    
if __name__ == "__main__":
    main()