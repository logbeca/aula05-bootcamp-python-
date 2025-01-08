import pandas as pd

def write_parquet( filename , output_file):
    df = pd.read_csv(filename)
    df.to_parquet(output_file)

def read_parquet(output_file):
 
    return pd.read_parquet(output_file)

if __name__ == "__main__":
  
    filename = "data/measurements.txt"  
    output_file = 'data/measurements.parquet'
    write_parquet( filename , output_file)
    read_parquet(output_file)
    print((read_parquet(output_file)).head())