from PyPDF2 import PdfFileWriter, PdfFileReader
import os

inputFolder = "C:\\Users\\developer\\Documents\\Handout"
outputFolder = "C:\\Users\\developer\\Documents\\Slide"

for subdir, dirs, files in os.walk(inputFolder):
    for file in files:
        if not file.endswith(".pdf"): 
            continue   
        sourcePdf =  os.path.join(subdir,file)        
        resultDir = os.path.join(outputFolder, os.path.relpath(subdir, inputFolder))
        resultPdf = os.path.join(resultDir, file)
        if not os.path.exists(resultDir):
            os.makedirs(resultDir)
        input1= PdfFileReader(sourcePdf)      
        output = PdfFileWriter()

        numPages = input1.getNumPages()
        print(f"{sourcePdf} has {numPages} pages.")

        for i in range(numPages):
            page = input1.getPage(i)         
            left = (30, 393)
            right = (512, 668)
            page.trimBox.lowerLeft = left
            page.trimBox.upperRight = right
            page.cropBox.lowerLeft = left
            page.cropBox.upperRight = right
            output.addPage(page)

        with open(resultPdf, "wb") as out_f:
            output.write(out_f)
