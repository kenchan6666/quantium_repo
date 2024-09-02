import dash
from dash import html
import pandas as pd
from process_data import process_csv

# app = dash.Dash(__name__)

def merge_csv_files(file_paths, output_file):
    combined_df = pd.concat([process_csv(file) for file in file_paths], ignore_index=True)

    combined_df.to_csv(output_file, index=False)
    print(f"outputfile: {output_file}")

file_paths = [
    'data/daily_sales_data_0.csv',
    'data/daily_sales_data_1.csv',
    'data/daily_sales_data_2.csv'
]

output_file = 'formatted_output.csv'

merge_csv_files(file_paths, output_file)

# app.layout = html.Div(f"outputfile: {output_file}")

# if __name__ == '__main__':
#     app.run_server(debug=True)
