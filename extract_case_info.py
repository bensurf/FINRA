#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 13:08:41 2024

@author: Ben F.
"""

from openai import OpenAI
import os
import pdfplumber


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
        # response = openai_client.chat.completions.create(
        #     #model="text-davinci-003",
        #     model="gpt-4o-mini",
        #     prompt=text,
        #     max_tokens=150
        # )
        
        chat_completion = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "Hello world"}]
        )
        return response.choices[0].text.strip()
    
    pdf_text = extract_text_from_pdf(lawyer_name+"/"+case_number+".pdf")
    result = process_text_with_openai(pdf_text)
    print(result)

    