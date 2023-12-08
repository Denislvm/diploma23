from script import data
import xlsxwriter


def writer(array):

    book = xlsxwriter.Workbook(r"D:\PycharmProjects\diplom23\parse\odessa_house.xlsx")
    page = book.add_worksheet("data")

    column_names = ['District', 'Street', 'Rooms', 'Total Area', 'Floor', 'Total Floors in House',
                    'Living Space', 'Area Kitchen', 'House', 'Price']


    for i, name in enumerate(column_names):
        page.write(0, i, name)

    row = 1
    column = 0

    page.set_column("A:A", 50)
    page.set_column("B:B", 30)
    page.set_column("C:C", 30)
    page.set_column("D:D", 30)
    page.set_column("E:E", 30)
    page.set_column("F:F", 30)
    page.set_column("G:G", 30)
    page.set_column("I:I", 30)
    page.set_column("J:J", 30)
    page.set_column("K:K", 30)

    for item in array():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        page.write(row, column+6, item[6])
        page.write(row, column+7, item[7])
        page.write(row, column+8, item[8])
        page.write(row, column+9, item[9])
        row += 1

    book.close()


writer(data)
