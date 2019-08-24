# coding=utf-8
import os
from xlrd import open_workbook


def _get(xlsx_path, sheet, colums):
    if xlsx_path is None:
        return None

    if sheet is None:
        return None

    if colums is None:
        return None

    # open xls file
    file = open_workbook(xlsx_path)
    # get sheet by name
    sheet = file.sheet_by_name(sheet)

    row0 = sheet.row_values(0);
    search = []
    for i in range(len(row0)):
        name = row0[i]
        try:
            colums.index(name)
            search.append(i)
        except Exception:
            continue
    # get one sheet's rows
    rows = []
    nrows = sheet.nrows
    for i in range(1, nrows):
        row = []
        for j in search:
            row.append(sheet.row_values(i)[j])
        rows.append(row)
    return rows


class Xlsx:
    _instance = None

    def __init__(self):
        pass

    @classmethod
    def _get_instance(cls):
        if cls._instance is None:
            cls._instance = Xlsx()
        return cls._instance

    @staticmethod
    def get_rows(xlsx_path, sheet, colums):
        return _get(xlsx_path, sheet, colums)


if __name__ == "__main__":
    print(Xlsx.get_rows(os.path.join(os.getcwd(), "config", "testcase.xlsx"),
                        "login",
                        ("case_name", "method", "token", "email", "password")))
