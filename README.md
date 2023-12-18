![img](/ocr-.jpg) ![img](/Upload.svg)

# BUSINESS_CARD_EXTRACTION-OPTICAL CHARACTER RECOGNITION 
About EasyOCR
Text detection in images is an important technology for various applications, including text processing, image search, and machine translation. 
Advances in optical character recognition (OCR) technology have made document retrieval more accurate and efficient, allowing businesses and organizations to extract useful information from images quickly. a powerful and easy-to-use OCR library that can find and extract text from various formats. Let's look at the features of EasyOCR, its advantages over other OCR libraries, and how it can be implemented in a real-world application.

Jaided AI was founded in 2020. Our goal is to distribute the benefits of AI to the world. The first project is an open-source OCR library called EasyOCR. We build software with the philosophy that it has to be very easy to use while providing state-of-the-art performance. This maximizes AI accessibility for everyone to be ready for the upcoming AI revolution. After the success of our open-source project, we launched our professional service to organizations. This is the Enterprise version of EasyOCR. Here we aim to help organizations worldwide implement AI technology according to their needs.

![img](/easyocr_framework.jpeg)

## KINDLY CHECK OUT THE VIDEO OF THE PROJECT : - [click here](https://www.linkedin.com/posts/narayana-ram-sekar-b689a9201_guvi-guvigeeknetworksiitmresearchpark-activity-7137675483927760896-_KoS?utm_source=share&utm_medium=member_desktop)

#### Hi Everyone 🫶
 * Text detection can be done by various algorithms. Such as tesseract OCR, EasyOCR, and keras ocr. In this project, I used Easyocr as my primary algorithm. And I have given a brief intro about the Easy-OCR above. For reference, I leave a link for other OCRs.
 * [TESSERACT OCT](https://tesseract-ocr.github.io/) - DOCUMENTATION
 * [EASYOCR](https://www.jaided.ai/easyocr/documentation/) - DOCUMENTAION
 * [KERASOCR](https://keras-ocr.readthedocs.io/en/latest/) - DOCUMENTAION
#
##### PROBLEM STATEMENT - 
  *  You have been tasked with developing a Streamlit application that allows users to upload an image of a business card and extract relevant information from it using easyOCR. The extracted information should include the company name, cardholder name, designation, mobile number, email address, website URL, area, city, state, and pin code. The extracted information should then be displayed in the application's graphical user interface (GUI).

## ROADMAP OF THE PROJECT
#### PACKAGE TO BE IMPORT:
#### Package for image processing : 
```
import OS
import re
import easyocr
from io import bytesio
from PIL import image
```
#### Packages for data processing :
```
import pandas
import numpy as np
```
#### Package for database :
```
import psycopg2
```
#### Package for Dashboard :
```
import streamlit
from streamlit_option_menu import option_menu
```
#### Image-to-text conversion :
```
reader = easyocr.Reader(['en'])
result = reader.readtext(image_path)
```


![img](/select.jpg)


#### Data extraction from Image :
```
image_to_text(result):
for i in range(len(details)):
        match1 = re.findall('([0-9]+ [A-Z]+ [A-Za-z]+)., ([a-zA-Z]+). ([a-zA-Z]+)',details[i])    
        match2 = re.findall('([0-9]+ [A-Z]+ [A-Za-z]+)., ([a-zA-Z]+)', details[i])
        match3 = re.findall('^[E].+[a-z]',details[i])
        match4 = re.findall('([A-Za-z]+) ([0-9]+)',details[i])
        match5 = re.findall('([0-9]+ [a-zA-z]+)',details[i])    
        match6 = re.findall('.com$' , details[i])
        match7 = re.findall('([0-9]+)',details[i])
        if details[i] == details[0]:
        ......
image=image_to_text(result)
df=pd.DataFrame(image)
```
| Name | Designation | Company_Name | contact | email | website | state | pincode |
| -----| ----------- | ------------ | ------- | ----- | ------- | ----- | ------- |
| Selva | DATA MANAGER | Selva Digitl tech | +123-456-7890 | WWW XYZI.com | hello@XYZ1.com | TamilNadu | 600113 |

#### Dashboard Creation : 
###### Home page :
 * The code for the session button. Where need not to go sidemenu always to switch tabs
```
st.set_page_config(page_title="BUSIESS CARD EXTRACTION",
                   layout="wide",
                   page_icon="🧊",
                   initial_sidebar_state='auto'
                   )

if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option',0) + 1) % 3
    manual_select = st.session_state['menu_option']
else:
    manual_select = None
```
![img](/Home_page.jpg)

 * The switch is useful to change the tabs.
#
###### Upload image : 
 * The Streamlit allow us to upload file by using st.file_uploader()
![img](/upload1.jpg)
###### create table SQL : 
 * The Streamlit allow us to dataframe allow us to show data in dataframe format st.datframe() and I store table creation funcation in st.button. 
![img](/upload2.jpg)
###### Update and transmit to sql : 
 * The Streamlit allow us to get data from user and store it in text format by using st.text_input().Once i get all the desire update data from user i stored the update query in st.button() [update]
![img](/upload3.jpg)

###### Delete from Dashboard : 
 * The Streamlit allow us show tabs with the primary tab. And it can be done by using st.option_menu. To use this we need to install option_menu as it is the third party source. Delete tab allow user to delete the data by using the name of the card.
![img](/upload4.jpg)
### Explore more methods in streamlit : 
[Streamlit](https://docs.streamlit.io/) - To Create simple and interactive UI




<p align="left">
<b><em>TOP LANGUAGE:</em></b> <br/>


![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Narennrs1&layout=compact)


<p align="left">
<b><em>Point of Contacting:</em></b> <br/>
  
<a href="mailto:narennrsj@gmail.com">![narennrsj@gamil.com](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a> <a href="<https://www.linkedin.com/in/narayana-ram-sekar-b689a9201/>">![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)</a>
