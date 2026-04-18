from src.data_loader import load_raw_data, basic_data_check

def main():
    df = load_raw_data()
    basic_data_check(df)


if __name__ == "__main__":
    main()
