from email.message import EmailMessage
import os, PyPDF2, textract, glob, json, smtplib
from unicodedata import name
from inputs import *

def pdf_reader(keywordlst, email):
   pdf_dir = base_directory + 'Solicitation/tests/PDFs/'
   os.chdir(pdf_dir)
   complete_results = {}

   # loops thorugh each state in the PDFs folder
   for state in glob.iglob(f'{pdf_dir}/*'):
      state_name = state.split('\\')[-1]
      results = {}
      for file_name in glob.iglob(os.path.join(state, "*.pdf")):
         src = file_name.replace('\\', '/')
         name = src.split("/")[-1]
         #open method allows you to read the file.
         pdfFileObj = open(src,'rb')
         pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
         #Calculating number of pages in the PDF document.
         num_pages = pdfReader.numPages
         count = 0
         text = ""
         #The while loop will read each page.
         while count < num_pages:
            pageObj = pdfReader.getPage(count)
            count +=1
            text += pageObj.extractText()
         #This if statement exists because PyPDF2 cannot read scanned files.
         if text != "":
            text = text
         #If the above returns as False, we run the mighty OCR library textract to #convert scanned/image based PDF files into text.
         else:
            text = textract.process(file_name, method='tesseract', language='eng')
         
         # for loop throuhg text and match the search_keywords    
         lst = []
         for word in keywordlst:
            if word in text:
               lst.append(word)
               # print(word)
            else:
               break 
         # if PDF has a keyword, I add it to the results list.          
         if lst:
            results[name] = lst
         else:
            pdfFileObj.close()
         #    os.remove(src) 
         # print(results)
            
      #  if the state has any matching PDFs, I assign it to the complete_results dictionary. 
         if results:
            complete_results[state_name] = results
         else:
            break
      

   # Sending Summary email that contains a list of states/pdfs with keyword from. 
   summary = (json.dumps(complete_results, sort_keys=True, indent=4)).replace('{','').replace('}','').replace(',','').replace('"\n','"').replace('[\n','[').replace('[          ','[').replace('"        ]','" ]').replace('"            "', ' , ').replace('"','')
   sender = 'yasintraiba@gmail.com'
   receivers = [email]
   message = """From: PDF_READER <yasintraiba@gmail.com>
   

   Listed below are the states that have solicitation PDFs with YOUR matching Keywords. 
   
   Attatched to each PDF name are the Keywords that were found within. The State folders and their PDF's can all be found in the "PDFs" folder within the "Tests"" folder
   """ + summary

   gmail_user = "yasintraiba@gmail.com"
   gmail_app_password = ""
   sent_from = "yasintraiba@gmail.com"
   sent_to = email
   email_text = message

   try:
      server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
      server.ehlo()
      server.login(gmail_user, gmail_app_password)
      server.sendmail(sent_from, sent_to, email_text)
      server.close()

      print('The script is complete! Check your email for the list of results.')
   except Exception as exception:
      print("Error: %s!\n\n" % exception)


