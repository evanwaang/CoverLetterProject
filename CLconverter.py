from docxtpl import DocxTemplate
import datetime

company = input("Enter Company Name: ")
region = input("Enter provide and city: ")
address = input("Enter company address: ")
position = input("Enter position applied for: ")
date = datetime.datetime.today().strftime('%B, %d, %Y')

context = {
    'company': company,
    'region': region,
    'address': address,
    'position': position,
    'date': date
}

#Open document

doc = DocxTemplate("Cover_Letter_Template.docx")

#Load document

doc.render(context)

doc.save('Cover_Letter_for_'+company+'_'+position+'.docx')