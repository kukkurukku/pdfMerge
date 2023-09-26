from PyPDF2 import PdfWriter

merger = PdfWriter()

cv = open("SajihBinSuja/SajihBinSuja.pdf", "rb")
transcripts = open("SajihBinSuja/Transcript_Sajih_Bin_Suja.pdf", "rb")

for pdf in [cv, transcripts]:
    merger.append(pdf)

# Write to an output PDF document
merger.write("SajihBinSuja/Sajih_Bin_Suja.pdf")

# Close File Descriptors
merger.close()