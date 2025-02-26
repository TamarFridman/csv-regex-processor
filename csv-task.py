import pandas as pd
import argparse
import os
def tsv_to_csv(tsv_file, csv_file):
    """Convert TSV file to CSV."""
    if not os.path.isfile(tsv_file):
        raise FileNotFoundError(f"The input TSV file '{tsv_file}' does not exist.")
    
    # Check if file is empty
    if os.stat(tsv_file).st_size == 0:
        raise ValueError(f"The input TSV file '{tsv_file}' is empty.")
    
    df = pd.read_csv(tsv_file, delimiter='\t')
    df.to_csv(csv_file, index=False)
    print(f"TSV file '{tsv_file}' has been converted to CSV and saved as '{csv_file}'.")

def csv_to_df(infile):
    """Read CSV file into DataFrame."""
    if not os.path.isfile(infile):
        raise FileNotFoundError(f"The input file '{infile}' does not exist.")
    
    # Check if file is empty
    if os.stat(infile).st_size == 0:
        raise ValueError(f"The input file '{infile}' is empty.")
    
    return pd.read_csv(infile)

def add_price_column(df):
    """Add price_edited column with float values from search_price column."""
    if 'search_price' in df.columns:
        df['price_edited'] = pd.to_numeric(df['search_price'], errors='coerce')
    else:
        print("Warning: 'search_price' column not found, skipping 'price_edited' creation.")
    return df

def main():
    parser = argparse.ArgumentParser(description='Add price_edited column to a CSV file or convert TSV to CSV')
    parser.add_argument('--infile', required=True, help='Input CSV file (if not exists, create from TSV)')
    parser.add_argument('--out', required=True, help='Output CSV file with price')
    args = parser.parse_args()

    try:
        infile = args.infile

        # Check if the input file is CSV and exists, if not, convert it from TSV
        if not os.path.isfile(infile):
            # If the .csv file doesn't exist, try to convert it from a .tsv file
            tsv_file = infile.replace('.csv', '.tsv')
            if os.path.isfile(tsv_file):
                print(f"Input CSV '{infile}' does not exist. Converting from TSV file '{tsv_file}'...")
                tsv_to_csv(tsv_file, infile)
            else:
                raise FileNotFoundError(f"Neither the input CSV file '{infile}' nor the corresponding TSV file '{tsv_file}' exist.")

        # Read the input CSV file into DataFrame
        df = csv_to_df(infile)
        
        # Modify the DataFrame with price_edited column
        df_with_price = add_price_column(df)
        
        # Save the modified CSV with the price_edited column
        df_with_price.to_csv(args.out, index=False)

        print(f"Processing completed successfully. Output saved to '{args.out}'.")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    main()
