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
        
    case_numbers = get_arbitration_case_numbers(lawyer_name)
    
    for name in case_numbers:
        filepath = "Awards/"+lawyer_name+"/"+name+".pdf"
        if not os.path.exists(filepath):
            url = "https://www.finra.org/sites/default/files/aao_documents/"+name+".pdf"
            response = requests.get(url)
            with open(filepath, 'wb') as pdf_object:
                pdf_object.write(response.content)
            
    print("Done downloading all arbitration awards for "+lawyer_name)
    
def get_arbitration_case_numbers(lawyer_name):
    response = requests.get("https://www.finra.org/arbitration-mediation/arbitration-awards-online?aao_radios=all&field_case_id_text=&search="+lawyer_name+"&field_forum_tax=All&field_special_case_type_tax=All&field_core_official_dt%5Bmin%5D=&field_core_official_dt%5Bmax%5D=").text
    
    case_numbers = response.split('/sites/default/files/aao_documents/')
    case_numbers = case_numbers[1:]
    for i,name in enumerate(case_numbers):
        case_numbers[i] = name.split(".pdf")[0]
        
    return case_numbers