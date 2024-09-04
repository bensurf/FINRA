#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:57:10 2024

@author: Ben F.
"""

import requests

def get_arbitration_awards(lawyer_name):
    files = finra_search(lawyer_name)
    
def finra_search(lawyer_name):
    response = requests.get("https://www.finra.org/arbitration-mediation/arbitration-awards-online?aao_radios=all&field_case_id_text=&search="+lawyer_name.replace(" ","%20")+"&field_forum_tax=All&field_special_case_type_tax=All&field_core_official_dt%5Bmin%5D=&field_core_official_dt%5Bmax%5D=").text