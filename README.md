# Solicitation Automation

The scripting software along with a graphical user interface was created to automate 
the process of downloading new project solicitations for [Infrasense.](www.infrasense.com) 
PDFs that have information on new projects are downloaded from government websites and 
searched for keywords (bridge, infrared, etc.) that indicate the project might be of interest to
Infrasense.
## Dependencies

* [Playwright for python](https://playwright.dev/python/docs/intro) 
* [PyPDF2](https://pypi.org/project/PyPDF2/)
* [PySimpleGui](https://www.pysimplegui.org/en/latest/#install)
* [BeautifulSoup](https://www.geeksforgeeks.org/beautifulsoup-installation-python/)
* [Textract](https://pypi.org/project/textract/)

## Demo

Once the necessary dependencies are installed and your environment running, navigate into the "tests" folder and
enter the command "python gui.py" to open to user interface. Click "Download PDFs" to run the playwright scripts.

<img src="https://github.com/ytraiba/SolicitationAutomation/blob/main/readmes/guiSS.png" alt="drawing" style="width:600px; height:275px;"/>

After a few minutes, The PDFs have completed downloading into their corresponding State's folder. 

<img src="https://github.com/ytraiba/SolicitationAutomation/blob/main/readmes/image.png" alt="drawing" style="width:600px; height:275px;"/><img src="https://github.com/ytraiba/SolicitationAutomation/blob/main/readmes/image (1).png" alt="drawing" style="width:350px; height:275px;"/>

Enter the keywords (one at a time) that are of interest. Enter your email address and hit "add email". Finally, click "Run Script". 
Your email will receive an update similar to the one below that informs the user of which PDFs have the keywords you entered. Any PDF's that do not contain any PDFs will be deleted from their folders. 

<img src="https://github.com/ytraiba/SolicitationAutomation/blob/main/readmes/autom2.png" alt="drawing" style="width:600px; height:275px;"/>
<img src="https://github.com/ytraiba/SolicitationAutomation/blob/main/readmes/autom.png" alt="drawing" style="width:700px;"/>





