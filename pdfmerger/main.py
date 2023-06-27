import PyPDF2

pdfiles = ["AJIT CV LATTER.pdf", "AJIT KU PATEL.pdf", "Ajit Kumar Patel.pdf"]
merger = PyPDF2.PdfMerger()
for  filename in pdfiles:
	pdfFiles = open(filename, 'rb')
	pdfReader = PyPDF2.PdfReader(pdfFiles)
	merger.append(pdfReader)
pdfFiles.close()
merger.write('merged.pdf')