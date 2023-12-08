#----------------------------------------------:IMMPORT MODULAS:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import streamlit as st
import cv2
import easyocr
import io
from io import BytesIO
from streamlit_option_menu import option_menu
import psycopg2
import pandas as pd
import re
from PIL import Image
import numpy as np
#----------------------------------------------:SQL CONNECTION:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#@st.cache_resource
mydb=psycopg2.connect(host='localhost',user='postgres',password='Sql0991',database='bz_card',port=5432)
cursor=mydb.cursor()

create='''create table if not exists bs(id SERIAL PRIMARY KEY,
                                        name varchar(100),
                                        designation varchar(100),
                                        company_name varchar(100),
                                        contact varchar(100),
                                        email varchar(100),
                                        website varchar(100),
                                        address text,
                                        pincode varchar(100),
                                        image_byt bytea)'''
cursor.execute(create)
mydb.commit()
#----------------------------------------------:Data extraction:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def uploaded_image(Card_img):
    imdict = {'Name': [], 'Designation': [], 'Company': [], 'Contact': [],
                  'Email': [], 'Website': [],
                  'Address': [], 'Pincode': []
                  }
    imdict['Name'].append(add1[0])
    imdict['Designation'].append(add1[1])

    for i in range(2, len(add1)):
        if add1[i].startswith('+') or (add1[i].replace('-', '').isdigit() and '-' in add1[i]):
            imdict['Contact'].append(add1[i])

        elif '@' in add1[i] and '.com' in add1[i]:
            smaller = add1[i].lower()
            imdict['Email'].append(smaller)

        elif 'www' in add1[i] or 'WWW ' in add1[i] or 'wwW' in add1[i]:
            smaller = add1[i].lower()
            imdict['Website'].append(smaller)

        elif 'Tamil Nadu' in add1[i] or 'TamilNadu' in add1[i] or add1[i].isdigit():
            imdict['Pincode'].append(add1[i])

        elif re.match(r'^[A-Za-z]', add1[i]):
            imdict['Company'].append(add1[i])

        else:
            remove_colon = re.sub(r'[.,;]', '', add1[i])
            imdict['Address'].append(remove_colon)

    for key, values in imdict.items():
        if len(values) > 0:
            concat_string = ' '.join(values)
            imdict[key] = [concat_string]
        else:
            values = 'NA'
            imdict[key] = [values]
    return imdict
#----------------------------------------------:PAGE STEPUP:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

st.set_page_config(page_title="BUSIESS CARD EXTRACTION",
                   layout="wide",
                   initial_sidebar_state='auto'
                   )

if st.session_state.get('switch_button', False):
    st.session_state['menu_option'] = (st.session_state.get('menu_option',0) + 1) % 3
    manual_select = st.session_state['menu_option']
else:
    manual_select = None

with st.sidebar:    
    selected = option_menu("Main menu", ["Home", "Upload", 'About'], 
        icons=['house', 'cloud-upload', 'gear'], 
        manual_select=manual_select, key='menu_4')
st.button(f":red[Switch Tab] {st.session_state.get('menu_option',1)}", key='switch_button')
selected
#----------------------------------------------:IMAGE READER/EDIT:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
df=[]
im_df=[]

def ecocr():
    read=easyocr.Reader(["en"])
    return read

if selected=="Upload":
    #GET IMAGE FROM USER
    st.caption(":red[Upload the Business card]")
    bz_cd=st.file_uploader("Upload",label_visibility="collapsed",type=["png","jpg"],accept_multiple_files=False,help="Only .png & .jpg are allowed")
    #Process the image to df
    if bz_cd != None:
        get_img = Image.open(bz_cd)
        st.image(get_img,width=300,caption="Uploaded Business card")
        read=st.button(":red[Read Image]")
        if read:
            reader_ocr = ecocr()
            add1 = reader_ocr.readtext(np.array(get_img),detail=0)
            df=uploaded_image(add1)
            im_df=pd.DataFrame(df)
            st.dataframe(im_df)

        #Image to bytes
            im_by= io.BytesIO()
            get_img.save(im_by,format="png")
            im_data=im_by.getvalue()

            dict1={"Image":[im_data]}
            im_df1=pd.DataFrame(dict1)
            Image_df=pd.concat([im_df,im_df1],axis=1)

        #Store the DF to Database
            create=st.button(":red[Create Database]")
            if create:
                with st.spinner("Kindly wait for few mins"):
                    insert='''insert into bs(name,
                                            designation,
                                            company_name,
                                            contact,
                                            email,
                                            website,
                                            address,
                                            pincode,
                                            image_byt)
                                            values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                    for index,row in Image_df.iterrows():
                        values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8])
                        cursor.execute(insert,values)
                        mydb.commit()
                    st.success("All DONE")
            
            selected1 = option_menu(
                menu_title="MANAGE DATA",
                options=["UPDATE", "DELETE"],
                icons=["database-add", "database-dash"],
                menu_icon="database-gear",
                default_index=0,
                orientation="horizontal")
            
            if selected1 =="UPDATE":
                cl1,cl2=st.columns(2)
                with cl1:
                    edit_name=st.text_input("Name",df['Name'][0])
                    edit_des=st.text_input("Designation",df['Designation'][0])
                    edit_co=st.text_input("Company",df['Company'][0])
                    edit_cont=st.text_input("Contact",df['Contact'][0])
                with cl2:
                    edit_em=st.text_input("Email",df['Email'][0])
                    edit_wb=st.text_input("Website",df['Website'][0])
                    edit_ad=st.text_input("Address",df['Address'][0])
                    edit_pn=st.text_input("Pincode",df['Pincode'][0])

                if st.button("Update"):
                    qr='''update bs set name=%s,designation=%s,company_name=%s,contact=%s,email=%s,website=%s,address=%s,pincode=%s 
                        where name=%s'''
                    values=(edit_name,edit_des,edit_co,edit_cont,edit_em,edit_wb,edit_ad,edit_pn)
                    cursor.execute(qr,values)
                    mydb.commit()
                    up=cursor.fetchall()
                    st.caption("ALl done")
                    st.dataframe(pd.DataFrame(up,columns=("name","designation","company_name","contact","email","website","address","pincode")))

if selected=="Home":
    st.subheader(":red[BUSINESS CARD TEXT EXTRACTION USING EASYOCR]")
    st.subheader(":gray[IMPORTANCE OF OCR]")

    st.write('''Text detection in images is an important technology for a variety of applications, including text processing, image search, and machine translation. 
             Advances in optical character recognition (OCR) technology have made document retrieval more accurate and efficient, allowing businesses and organizations to quickly extract useful information from images. 
             This article introduces EasyOCR, a powerful and easy-to-use OCR library that can find and extract text from a variety of formats. 
             Let's look at the features of EasyOCR, its advantages over other OCR libraries, and how it can be implemented in a real-world application.''')
    
    st.subheader(":gray[EASYOCR]")

    st.write('''Jaided AI was founded in 2020. Our goal is to distribute the benefits of AI to the world. The first project is an open source OCR library called EasyOCR. We build software with the philosophy that it has to be very easy to use while providing state-of-the-art performance. 
             This is to maximize AI accessiblity for everyone to be ready for the upcoming AI revolution.
             After the success of our open source project, we launched our professional service to organizations. This is the Enterprise version of EasyOCR. 
             Here we aim to help organizations around the world implementing AI technology according to their own need.''')
    
    image=("D:\\DTM9\\CS-3\\easyocr_framework.jpeg")
    ey_image=Image.open(image)
    st.image(ey_image,caption="EASYOCR FRAMEWORK")

if selected=="About":
    st.subheader(":red[My Contact]")
    st.subheader(":green[Project - BizCardX_Extracting Business Card Data]")
    st.link_button("LinkedIn","https://www.linkedin.com/in/narayana-ram-sekar-b689a9201/")
    st.link_button("GitHub","https://github.com/Narennrs1")