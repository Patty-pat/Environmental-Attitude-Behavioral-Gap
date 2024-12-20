"""Tasks for managing the data."""

import pytask
from eaibgap.config import SRC, BLD
from eaibgap.data_management.facilities_data_json_to_xls import (
    facilities_data_json_to_xls,
)

@pytask.mark.task
def task_extract_json_to_xls_central_java(
    json_input=SRC / "data" / "central_java.json",
    produces=BLD / "data" / "central_java.xlsx",
):
    """
    Pytask task to extract data from JSON to Excel.
    """
    facilities_data_json_to_xls(json_input, produces)
