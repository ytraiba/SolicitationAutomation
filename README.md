# Solicitation Automation

I created these scripts along with a graphical user interface to automate 
the process of downloading new project solicitiations for [Infrasense.](www.infrasense.com) 
PDF's that have information on new projects are downloaded from government websites and 
searched for keywords (bridge, infrared, etc.) that indicate the project might be of interest to
Infrasense. 
## Lessons Learned

I learned how to:

* Interact with and navigate through the browser using Playwright
* Use Python's OS module to open, edit, and delete files. 
* Create a Front-End using python and allow non-technical users to run my scripts
* Run functions asyncronously to improve dowload speeds

## Dependencies

* [Playwright for python](https://playwright.dev/python/docs/intro) 
* [PyPDF2](https://pypi.org/project/PyPDF2/)
* [PySimpleGui](https://www.pysimplegui.org/en/latest/#install)
* [BeautifulSoup](https://www.geeksforgeeks.org/beautifulsoup-installation-python/)
* [Textract](https://pypi.org/project/textract/)

## Demo

Once the nessesary dependencies are installed and your environment running, navigate into the "tests" folder and
enter the command "python gui.py" to open to user interface. Click "Download PDF's" to run the playwright scripts.

<img src="https://github.com/ytraiba/SolicitationAutomation/blob/main/readmes/guiSS.png" alt="drawing" style="width:600px;"/>

After a few minutes, The PDFs have completed downloading into their corresponding State's folder. 

<img src="https://github.com/ytraiba/SolicitationAutomation/blob/main/readmes/image.png" alt="drawing" style="width:600px;"/>
<img src="https://github.com/ytraiba/SolicitationAutomation/blob/main/readmes/image (1).png" alt="drawing" style="width:350px;"/>

Enter in the keywords (one at a time) that are of interest. Enter in your email address and hit "add email". Finally, click "Run Script". 
Your email will recieve an update similar to the one below that inform the user of which PDFs have the keywords you entered. 

<img src="https://github.com/ytraiba/SolicitationAutomation/blob/main/readmes/autom2.png" alt="drawing" style="width:600px;"/>
<img src="https://github.com/ytraiba/SolicitationAutomation/blob/main/readmes/autom.png" alt="drawing" style="width:700px;"/>





