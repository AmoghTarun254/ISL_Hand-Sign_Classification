import pandas as pd

def swap_columns(input_file, output_file):
    # Load the Excel file
    df = pd.read_excel(input_file)
    
    # Separate the classification column and the rest of the data
    classification_col = df.iloc[:, 0]  # First column
    data_columns = df.iloc[:, 1:]      # All other columns
    
    # Identify the first 42 and last 42 columns
    first_42 = data_columns.iloc[:, :42]
    last_42 = data_columns.iloc[:, -42:]
    middle_columns = data_columns.iloc[:, 42:-42]  # Any middle columns (if any)
    
    # Swap first 42 and last 42 columns while keeping classification in place
    swapped_data = pd.concat([classification_col, last_42, middle_columns, first_42], axis=1)
    
    # Save the reordered DataFrame to a new CSV file
    swapped_data.to_excel(output_file, index=False)
    
# Example usage
input_file = "extracted landmarks\rotated_left-handed_landmarks 22nd Jan condensed.csv"  # Replace with the actual file path
output_file = "reordered_left_handed_landmarks.xlsx"  # Output CSV file
swap_columns(input_file, output_file)
