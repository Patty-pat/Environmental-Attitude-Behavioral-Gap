"""Tasks for managing the data."""

import pytask
from pytask import task
from eaibgap.config import SRC, BLD
from eaibgap.data_management.facilities_data_json_to_xls import (
    facilities_data_json_to_xls,
)

@task
def task_extract_json_to_xls_central_java(
    json_input=SRC / "data" / "central_java.json",
    produces=BLD / "data" / "central_java.xlsx",
):
    """
    Pytask task to extract data from JSON to Excel.
    """
    facilities_data_json_to_xls(json_input, produces)

@task
def task_extract_json_to_xls_west_java(
    json_input=SRC / "data" / "west_java.json",
    produces=BLD / "data" / "west_java.xlsx",
):
    """
    Pytask task to extract data from JSON to Excel.
    """
    facilities_data_json_to_xls(json_input, produces)
