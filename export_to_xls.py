import openpyxl
from buffer import Buffer
from const import ColType, type_titles

def export(in_file):
    with open(in_file, "rb") as file:
        data = file.read()

    wb = openpyxl.Workbook()
    sheet = wb.active

    buff = Buffer(data)
    col_size = buff.read(ColType.UINT32)

    cols, headers = [], []
    for _ in range(col_size):
        col = buff.read(ColType.UINT32)
        headers.append(type_titles[ColType(col)])
        cols.append(col)

    sheet.append(headers)

    row_size = buff.read(ColType.UINT32)
    for _ in range(row_size):
        row = []
        for col in cols:
            col_type = ColType(col)
            if col_type == ColType.STRING:
                text_size = buff.read(ColType.UINT32)
                text = buff.read_n(text_size)
                row.append(bytes_to_string(text))
            else:
                row.append(buff.read(col_type))

        sheet.append(row)

    wb.save(str(file.name).removesuffix(".tbl") + ".xlsx")
    return "done"


def bytes_to_string(data):
    s = ""
    for d in data:
        if d < 128:
            s += chr(d)
        else:
            s += "?"
    return s

