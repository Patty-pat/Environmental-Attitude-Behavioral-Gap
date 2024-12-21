"""Tasks for managing the data."""

import pytask
from pytask import task
from eaibgap.config import SRC, BLD
from eaibgap.data_management.facilities_data_json_to_xls import (
    facilities_data_json_to_xls,
)

files = [
    ("central_java.json", "central_java.xlsx"),
    ("west_java.json", "west_java.xlsx"),
    ("east_java.json", "east_java.xlsx"),
    ("DKI_jakarta.json", "DKI_jakarta.xlsx"),
    ("DI_yogyakarta.json", "DI_yogyakarta.xlsx"),
    ("banten.json", "banten.xlsx"),
]

for json_file, excel_file in files:

    @task(
        name=f"extract_json_to_xls_{json_file.split('.')[0]}"  # Unique task name
    )
    def dynamic_task(json_input=SRC / "data" / json_file, produces=BLD / "data" / excel_file):
        """
        Dynamically generated task to extract data from JSON to Excel.
        """
        # Ensure output directory exists
        produces.parent.mkdir(parents=True, exist_ok=True)
        facilities_data_json_to_xls(json_input, produces)