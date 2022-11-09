from PyPDF2 import PdfMerger

pdfs = [r"C:\Users\varun\Desktop\Vanhack\Final\6. Employee Reference Letters\334458_Srilekha Anumulapelli.pdf", r"C:\Users\varun\Desktop\Vanhack\Final\6. Employee Reference Letters\SL-DNB.pdf", r"C:\Users\varun\Desktop\Vanhack\Final\6. Employee Reference Letters\Srilekha Optum Reference letter.pdf"]

merger = PdfMerger()


merger.append(pdfs[0])
merger.append(pdfs[2])
merger.append(pdfs[1])

merger.write(r"C:\Users\varun\Desktop\Vanhack\Final\6. Employee Reference Letters\Srilekha Reference Letters Asc.pdf")
merger.close()