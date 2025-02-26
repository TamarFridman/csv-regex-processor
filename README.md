# CSV and Regex Processing Scripts

## Overview

This project includes two Python scripts to process CSV and TSV files:

### 1.CSV Processing (csv-task.py)

  - Converts a TSV (Tab-Separated Values) file to a CSV (Comma-Separated Values) file.

  - Adds a new column, price_edited, extracted as a float from the existing search_price column.

### 2.Regex Filtering (regex-task.py)

  - Filters out rows from a CSV file that contain Knitwear in the custom_5 column but do not include Jumper.

   - Uses a regular expression to perform the filtering operation.

### Prerequisites

Ensure you have Python installed (version 3.6 or later) and install the required dependencies using:
```
pip install pandas
```
### Usage

### 1. Convert TSV to CSV & Add a Column (csv-task.py)

This script processes a TSV file, converts it to CSV format, and adds a price_edited column.

```
python csv-task.py --infile python_home_task_file.csv --out python_home_task_file_with_price.csv
```

### Functionality:

- If python_home_task_file.csv does not exist, the script will attempt to convert python_home_task_file.tsv to CSV.

- Adds a price_edited column with float values extracted from search_price.

- Saves the processed file as python_home_task_file_with_price.csv.

### 2. Regex Filtering (regex-task.py)

This script filters out rows based on regex conditions applied to the custom_5 column.

```
python regex-task.py --infile python_home_task_file.csv --out python_home_task_file_regex.csv
```
### Functionality:

- Removes rows where custom_5 contains Knitwear but does not contain Jumper.

- Saves the filtered dataset to python_home_task_file_regex.csv.

### Error Handling

- If the input file is missing, an error message is displayed.

- If the input file is empty, the script exits with an appropriate message.

- If required columns are missing, the script warns the user and continues execution where possible.

### Example Execution

1.Convert TSV to CSV and add the price_edited column:
```
python csv-task.py --infile python_home_task_file.csv --out python_home_task_file_with_price.csv
```


2.Filter out Knitwear without Jumpers:
```
python regex-task.py --infile python_home_task_file.csv --out python_home_task_file_regex.csv
```

### Notes

The regex filtering script assumes the existence of a custom_5 column.

The price_edited column is created only if search_price exists in the dataset.

### Author

Developed by Tamar Friedman

