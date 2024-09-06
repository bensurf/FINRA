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
    
    pdf_text = extract_text_from_pdf(lawyer_name+"/"+case_number+".pdf")
    result = process_text_with_openai(pdf_text)
    print(result)

    