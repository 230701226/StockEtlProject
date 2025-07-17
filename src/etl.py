import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

def load_and_concatenate_csvs(data_dir):
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data folder not found: {data_dir}")

    all_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.csv')]
    df_list = []

    for f in all_files:
        try:
            df = pd.read_csv(f)
            if all(col in df.columns for col in ["Date", "Close", "Volume"]):
                df["Stock Symbol"] = os.path.splitext(os.path.basename(f))[0]
                df_list.append(df)
            else:
                print(f"Skipped: {f} - Missing required columns.")
        except Exception as e:
            print(f"Error reading {f}: {e}")

    if not df_list:
        raise ValueError("No valid CSV files found in data directory.")

    return pd.concat(df_list, ignore_index=True)


def preprocess_data(df):
    df = df.dropna(subset=["Close", "Volume"])
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df = df.dropna(subset=["Date"])
    df["Year"] = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month
    df["Day"] = df["Date"].dt.day
    df["Return"] = df["Close"].pct_change()
    df["RollingMean"] = df["Close"].rolling(window=7).mean()
    df["Volatility"] = df["Close"].rolling(window=7).std()
    df = df.dropna(subset=["RollingMean", "Volatility"])  # Drop early rows with NaN
    return df

def scale_features(df):
    scale_cols = ["Close", "Volume", "RollingMean", "Volatility"]
    scaler = StandardScaler()
    df[scale_cols] = scaler.fit_transform(df[scale_cols])
    return df

def run_etl(data_dir, output_path):
    df = load_and_concatenate_csvs(data_dir)
    df = preprocess_data(df)
    df = scale_features(df)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Processed data saved to {output_path}")
    return df
