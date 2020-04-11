import PyPDF2
import json

malelst=[]
femalelst=[]

pdfFileObj = open('N:\Python\Islamic-Names-Boys-Girls.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.numPages
# Loop for reading all the Pages
for i in range(pages):
        # Creating a page object
        pageObj = pdfReader.getPage(i)
        # Printing Page Number
        #print("Page No: ",i)
       
        text = pageObj.extractText().split("  ")
       
        for i in range(len(text)):
               
            lines=text[i].split("\n")
            
            for l in range(len(lines)):
                line=lines[l]
                
                if(line.__contains__("(male)Š")):
                    dct={}
                    slst=line.split("(male)Š")
                    dct["name"]=slst[0]
                    dct["meaning"]=slst[1]
                    malelst.append(dct)

                elif(line.__contains__("(female)Š")):
                    dct={}
                    slst=line.split("(female)Š")
                    dct["name"]=slst[0]
                    dct["meaning"]=slst[1]
                    femalelst.append(dct)

pdfFileObj.close()

# print(malelst)
# print(femalelst)

with open('N:\Python\male.json', 'w') as fp:
    json.dump(malelst, fp)
    print("Saved male.json")

with open('N:\Python\\female.json', 'w') as fp:
    json.dump(femalelst, fp)
    print("Saved female.json")