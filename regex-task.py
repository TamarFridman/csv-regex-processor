import argparse
import pandas as pd
import re

def filter_knit_products(infile, outfile):
    # Load the CSV file
    try:
        df = pd.read_csv(infile)
    except Exception as e:
        raise ValueError(f"Error reading input file: {e}")
    
    # Ensure there's a relevant column
    column_name = 'custom_5'
    if column_name not in df.columns:
        raise ValueError(f"The input CSV must contain a '{column_name}' column.")
    
    # Regex pattern to match 'Knitwear' but exclude 'Jumper'
    pattern = r'\bKnitwear\b(?!.*\bJumper\b)'
    
    # Filter the dataframe: Keep rows where 'custom_5' does not match the pattern
    try:
        filtered_df = df[~df[column_name].str.contains(pattern, flags=re.IGNORECASE, na=False)]
    except Exception as e:
        raise ValueError(f"Error during filtering with regex: {e}")
    
    # Save the result
    try:
        filtered_df.to_csv(outfile, index=False)
        print(f"Filtered data saved to {outfile}")
    except Exception as e:
        raise ValueError(f"Error saving the output file: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--infile", required=True, help="Input CSV file")
    parser.add_argument("--out", required=True, help="Output CSV file")
    args = parser.parse_args()
    
    try:
        filter_knit_products(args.infile, args.out)
    except Exception as e:
        print(f"Error: {e}")
