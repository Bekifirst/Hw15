from docx import Document
from docx.shared import Pt

document = Document()

paragraph = document.add_paragraph("Hello World")

run = paragraph.runs[0]
run.font.name = "Arial"
run.font.size = Pt(12)

document.save("File.docx")





