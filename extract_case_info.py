#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:08:41 2024

@author: Ben F.
"""

import openai
import pdfplumber


openai.api_key = 'your-api-key'


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def extract_case_info(lawyer_name, case_number):
    text = extract_text_from_pdf(lawyer_name+"/"+case_number+".pdf")
    
    print(text)
    