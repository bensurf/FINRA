#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:08:41 2024

@author: Ben F.
"""

import openai
import pdfplumber


f = open("openai_api_key.txt","r")
openai_api_key = f.read()
f.close()


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_case_info(lawyer_name, case_number):
    text = extract_text_from_pdf(lawyer_name+"/"+case_number+".pdf")
    
    def process_text_with_openai(text):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    
    pdf_text = extract_text_from_pdf("your-document.pdf")
    result = process_text_with_openai(pdf_text)
    print(result)

    