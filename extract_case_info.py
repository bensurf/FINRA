#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:08:41 2024

@author: Ben F.
"""

from openai import OpenAI
import os
import pdfplumber
import csv


f = open("openai_api_key.txt","r")
os.environ["OPENAI_API_KEY"] = f.read()
f.close()

openai_client = OpenAI()


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_case_info(lawyer_name, case_number):
    def process_text_with_openai(text):
        chat_completion = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content":
                       """Below is an arbitration award in a lawsuit of a broker dealer. I would like you to extract the following three pieces of information:
                       
                       1. The claims of the lawsuit
                       2. The monetary awards sought by the plaintiff
                       3. The awards resulting from the arbitration
                       
                       Here is the arbitration award in full:
                           
                        """
                        +
                        text}]
        )
        return chat_completion.choices[0].message.content
    
    pdf_text = extract_text_from_pdf("Awards/"+lawyer_name+"/"+case_number+".pdf")
    result = process_text_with_openai(pdf_text)
    return result
    

def extract_lawyer_cases(lawyer_name):
    folder_name = "Awards/"+lawyer_name
    filenames = os.listdir(folder_name)
    #filenames = filenames[0:3]
    case_numbers = [file.split('.')[0] for file in filenames]
    print(case_numbers)
    
    case_info_dict = {}
    for case in case_numbers:
        case_info_dict[case] = extract_case_info(lawyer_name,case)
    
    return case_info_dict
        
        
def save_lawyer_cases(lawyer_name):
    case_info_dict = extract_lawyer_cases(lawyer_name)
    w = csv.writer(open(lawyer_name+".csv", "w"))

    for case, info in case_info_dict.items():
        w.writerow([case, info])
    

    