import xlsxwriter

xl_file = xlsxwriter.Workbook(r'/Users/rimanagi/PycharmProjects/Parsing_orscraping_sites/parsing.xlsx')
page = xl_file.add_worksheet('Товары')

def writer(name: str | None = None,
           price: str | None = None,
           product_link: str | None = None,
           description: str | None = None,
           row: int = 0):


    column = 0

    page.set_column('A:A', 50)
    page.set_column('D:D', 50)

    page.write(row, column, name)
    page.write(row, column + 1, price)
    page.write(row, column + 2, product_link)
    page.write(row, column + 3, description)
    row += 1


