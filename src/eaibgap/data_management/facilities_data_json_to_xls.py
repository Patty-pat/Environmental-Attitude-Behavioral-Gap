import json
from openpyxl import Workbook

def facilities_data_json_to_xls(json_input_path, output_xlsx_path):
    """
    Extract data by marker from a JSON file and save it into an Excel file.

    Parameters:
    - json_input_path: str, path to the JSON input file.
    - output_xlsx_path: str, path to save the output Excel file.
    """
    with open(json_input_path, 'r') as json_file:
        data = json.load(json_file)

    markers = data.get("markers", [])
    wb = Workbook()
    ws = wb.active
    headers = ["Name", "Unit Number", "Latitude", "Longitude", "Type"]
    ws.append(headers)

    for marker in markers:
        row = [
            marker[0] if len(marker) > 0 else '',
            marker[5] if len(marker) > 5 else '',
            marker[1] if len(marker) > 1 else '',
            marker[2] if len(marker) > 2 else '',
            marker[4] if len(marker) > 4 else ''
        ]
        ws.append(row)

    wb.save(output_xlsx_path)
    print(f"Excel file '{output_xlsx_path}' created successfully.")
