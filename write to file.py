# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 01:01:52 2020
writing to files
@author: Ayush Gupta
"""
# w mode first clears the file then writes
# a mode appends in an existing file or creates a new file
# r+ enables reading or writing both but it starts fron starting and overrede required characters


# with open('a.txt','r+') as f:
#     f.seek(len(f.read()))
#     f.write('\nhello this is a new text\n')
#     print(f.read())
# # print(f.closed)  


#######################
with open('a.txt','r') as rf:
    with open('file.txt','w') as wf:
    # f.seek(len(f.read()))
          wf.write(rf.read())
    print(wf.read())
# print(f.closed)        
    


