from fpdf import FPDF
import csv
import project
from datetime import datetime

def getdate():
    nowtime = datetime.now()
    return nowtime.strftime("%Y-%m-%d ")

def gettime():
    nowtime = datetime.now()
    return nowtime.strftime("%H:%M:%S")



def makepdf():
    class PDF(FPDF):
        def header(self):
            self.image("logo/Store logo.png", 8, 6, 33)
            self.set_font("helvetica", size = 18)
            self.cell(75)
            self.cell(40, 20, txt="CS50 Convenient Store", align="C")
            self.ln(10)
            self.set_font("helvetica", size = 10)
            self.cell(150)
            self.cell(20, 10, txt=f"Date:{getdate()}")
            self.ln(5)
            self.cell(150)
            self.cell(20, 10, txt=f"Time:{gettime()}")
            self.ln(15)

        def footer(self):
            self.set_y(-15)
            self.set_font("helvetica", size = 10)
            self.cell(20, 10, txt=f"Cashier:{project.get_admin()}")
            self.cell(120)
            self.cell(20, 10, txt=f"Telephone: 852+ 2123-456X")
            pass

    with open('tempreceipt.csv', 'r') as file:
        data = list(csv.reader(file, delimiter=","))

    pdf = PDF()
    pdf.set_font("helvetica", size = 12)
    pdf.add_page()



    with pdf.table(borders_layout="SINGLE_TOP_LINE") as table:
        for data_row in data:
            row = table.row()
            for datum in data_row:
                row.cell(datum, align="c")

    ########################################
    ######### total + pay + change #########
    ########################################

    pdf.ln(20)
    pdf.cell(150)
    pdf.cell(20,10,txt=f"Total: {project.retuTotal()}")
    pdf.ln(10)
    pdf.cell(150)
    pdf.cell(20,10,txt=f"Pay: ${project.retuPay()}")
    pdf.ln(10)
    pdf.cell(150)
    pdf.cell(20,10,txt=f"Change: {project.retuChange()}")

    temp_date = getdate().replace(" ", "_")
    temp_time = gettime().replace(":", "_")
    date_time = temp_date + "_" + temp_time
    pdf_name = f"{date_time}.pdf"

    file_path = "receiptrecord/" + pdf_name

    pdf.output(file_path,"f")