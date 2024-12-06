import xlsxwriter
from pars import arr_url


def writer(parametr):

    book = xlsxwriter.Workbook(r"C:\GITHUB\Parsing_with_autorization\quotes.xlsx")
    sheet = book.add_worksheet("Цитати")

    row = 0
    column = 0

    sheet.set_column("A:A", 100)
    sheet.set_column("B:B", 20)
 

    for item in parametr():
        sheet.write(row, column, item[0])
        sheet.write(row, column + 1, item[1])
  
        row += 1

    book.close()


if __name__ == "__main__":
    if arr_url != None:
        writer(arr_url)
