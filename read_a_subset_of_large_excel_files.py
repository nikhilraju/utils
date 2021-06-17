# https://stackoverflow.com/questions/54012750/loading-first-100-rows-of-excel
import openpyxl
import pandas as pd


def read_excel_custom(filename, nrows):
    """Read out a subset of rows from the first worksheet of an excel workbook.

    This function will not load more excel rows than necessary into memory, and is 
    therefore well suited for very large excel files.

    Parameters
    ----------
    filename : str or file-like object
        Path to excel file.
    nrows : int
        Number of rows to parse (starting at the top).

    Returns
    -------
    pd.DataFrame
        Column labels are constructed from the first row of the excel worksheet.

    """
    # Parameter `read_only=True` leads to excel rows only being loaded as-needed
    book = openpyxl.load_workbook(filename=filename, read_only=True, data_only=True)
    first_sheet = book.worksheets[0]
    rows_generator = first_sheet.values

    header_row = next(rows_generator)
    data_rows = [row for (_, row) in zip(range(nrows - 1), rows_generator)]
    return pd.DataFrame(data_rows, columns=header_row)