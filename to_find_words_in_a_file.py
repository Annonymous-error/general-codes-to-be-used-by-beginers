# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 01:35:30 2020

@author: Ayush Gupta
"""


with open('any_file','r') as rf:
    with open('file.txt','a') as wf:
        page=file.read()
        link_exist = True
        while link_exist:
            pos = page.find('<a href=')
            if pos == -1:
                
                link_exist=False
            
            else:
                
                first_quote = line.find('\"',pos)
                second_quote = line.find('\"',first_quote)
                a=line[first_quote:second_quote]
                wf.write(url +'\n')
                page=page[second_quote:]