#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:57:10 2024

@author: Ben F.
"""

import requests
import os

def get_arbitration_awards(lawyer_name):
    files = finra_search(lawyer_name)
    
def finra_search(lawyer_name):
    response = requests.get("https://www.finra.org/arbitration-mediation/arbitration-awards-online?aao_radios=all&field_case_id_text=&search="+lawyer_name+"&field_forum_tax=All&field_special_case_type_tax=All&field_core_official_dt%5Bmin%5D=&field_core_official_dt%5Bmax%5D=").text
    
    pdf_names = response.split('/sites/default/files/aao_documents/')
    pdf_names = pdf_names[1:]
    for i,name in enumerate(pdf_names):
        pdf_names[i] = name.split(".pdf")[0]
    
    
    for name in pdf_names:
        if not os.path.exists(lawyer_name):
            os.makedirs(lawyer_name)
        url = "https://www.finra.org/sites/default/files/aao_documents/"+name+".pdf"
        response = requests.get(url)
        filepath = lawyer_name+"/"+name+".pdf"
        with open(filepath, 'wb') as pdf_object:
            pdf_object.write(response.content)
            
    print("Done downloading all arbitration awards for "+lawyer_name)