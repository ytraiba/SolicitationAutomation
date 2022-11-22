import PySimpleGUI as sg
from pdf_reader import pdf_reader
from web_downloader import main
import asyncio

sg.theme('TanBlue')

col1  = [[sg.Text(
'''Instructions: 

First, click the "Download Solicitation PDF's" button 
and wait for confirmation that all Downloads are complete

Next, Use the PDF Reader to delete all pdfs that don't
contain a keyword within, and send an update to your email. 
Add keywords one at a time, enter your email address, 
and click the update email button. Finally, click the 
"Read PDF's" button and check your email.  
''', font=(6))], 
[sg.Button('Download Solicitation PDFs')]]

pdfReader = [[sg.Text('PDF Reader', font=('Helvetica', 15, 'bold', 'underline'))],
        [sg.Text('Enter a Keyword Here:        ', font=('Helvetica', 12)), sg.Input(key='-IN-', size=(40,2))],
        [sg.Text('Enter Your Email Here:        ', font=('Helvetica', 12)), sg.Input(key='-EMAIL-', size=(40,2))],
        [sg.Text('Your Added Keywords:        ', font=('Helvetica', 12)), sg.Multiline(size=(40,4), key='-WORDS-', font=('Helvetica', 10))],
        [sg.Button('Add Keyword'), sg.Button('Clear Keywords'), sg.Button('Add Email'), sg.Button('Run Script')]]

layout = [[sg.Text('     Solicitation Finder    ', font=('Helvetica', 22, 'bold'))],
        [sg.Column(col1, element_justification='c' ), sg.Column(pdfReader, element_justification='b')],
        [sg.Output(size=(65, 5), font=('Helvetica', 15) ), sg.Button('Exit')] ]


window = sg.Window('PDF READER', layout, finalize=True, element_justification='c')

keylst = []


while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Add Email':
        userEmail = values['-EMAIL-']
        print('Email Updated')
    elif event == 'Add Keyword':
        keylst.append(values['-IN-'])
        window['-WORDS-'].update(str(keylst).replace("[","").replace("]",""))
    elif event == 'Clear Keywords':
        keylst.clear()
        window['-WORDS-'].update(str(keylst).replace("[","").replace("]",""))
    elif event == "Run Script":
        pdf_reader(keywordlst=keylst, email=userEmail)
    elif event == 'Download Solicitation PDFs':
        asyncio.run(main())
    

window.close()