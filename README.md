![img](/ocr-.jpg) ![img](/Upload.svg)

# BUSINESS_CARD_EXTRACTION-OPTICAL CHARACTER RECOGNITION 
About EasyOCR
Text detection in images is an important technology for various applications, including text processing, image search, and machine translation. 
Advances in optical character recognition (OCR) technology have made document retrieval more accurate and efficient, allowing businesses and organizations to extract useful information from images quickly. a powerful and easy-to-use OCR library that can find and extract text from various formats. Let's look at the features of EasyOCR, its advantages over other OCR libraries, and how it can be implemented in a real-world application.

Jaided AI was founded in 2020. Our goal is to distribute the benefits of AI to the world. The first project is an open-source OCR library called EasyOCR. We build software with the philosophy that it has to be very easy to use while providing state-of-the-art performance. This maximizes AI accessibility for everyone to be ready for the upcoming AI revolution. After the success of our open-source project, we launched our professional service to organizations. This is the Enterprise version of EasyOCR. Here we aim to help organizations worldwide implement AI technology according to their needs.

![img](/easyocr_framework.jpeg)

#
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
![img](/)
