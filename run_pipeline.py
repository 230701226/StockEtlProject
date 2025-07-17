from src.etl import run_etl

if __name__ == "__main__":
    run_etl("data", "output/processed_data.csv")
    print("ETL pipeline completed and data saved to output/processed_data.csv")
