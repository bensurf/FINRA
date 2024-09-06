#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:57:10 2024

@author: Ben F.
"""

import requests
import os

def get_arbitration_awards(lawyer_name):
    if not os.path.exists("Awards/"+lawyer_name):
        os.makedirs("Awards/"+lawyer_name)
        
    case_numbers = get_arbitration_case_numbers_and_pdfs(lawyer_name)
    
    for case_number, pdf in case_numbers.items():
        filepath = "Awards/"+lawyer_name+"/"+case_number+".pdf"
        if not os.path.exists(filepath):
            url = "https://www.finra.org/sites/default/files/aao_documents/"+pdf+".pdf"
            response = requests.get(url)
            with open(filepath, 'wb') as pdf_object:
                pdf_object.write(response.content)
            
    print("Done downloading all arbitration awards for "+lawyer_name)
    
def get_arbitration_case_numbers_and_pdfs(lawyer_name):
    response = requests.get("https://www.finra.org/arbitration-mediation/arbitration-awards-online?aao_radios=all&field_case_id_text=&search="+lawyer_name+"&field_forum_tax=All&field_special_case_type_tax=All&field_core_official_dt%5Bmin%5D=&field_core_official_dt%5Bmax%5D=").text
    
    response = response.split('/sites/default/files/aao_documents/')
    response = response[1:]
    
    cases = {}
    for i,text in enumerate(response):
        text = text.split(".pdf\" target=\"_blank\">")
        pdf = text[0]
        text = text[1]
        case_number = text.split("</a")[0]
        cases[case_number] = pdf
        
    return cases