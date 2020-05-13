# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 14:32:38 2020
To create class
@author: Ayush Gupta
"""


class Room:
     def __init__(self, room_no,resident,phone_number,check_in_time,check_out_time):
         # init method/constructor gets called
         self.room_no=room_no
         self.resident=resident
         self.phone_number=phone_number
         self.check_in_time=check_in_time
         self.check_out_time=check_out_time
         
room100=Room(100,'ayush','66464','12.00','1.00')         
        
print(room100.room_no)
          