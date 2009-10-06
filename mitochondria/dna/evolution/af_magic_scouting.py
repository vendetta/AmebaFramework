#!/usr/bin/env python

import os

class MagicScouting:
    
    """ Using Nmap, Ameba can analize a lot of thing about a host or network """
    
    def __init__(self, target):
        self.target=target
        
    
    def validate_nmap(self):
        return 1
    
    def validate_target(self):
        number_dots=self.target.find(".")
        number_slash=self.target.find("/")
        if number_dots==4:
            if number_slash==0 or number_slash==1:
                return 1
            else:
                return 0
    
    def launch_scouting(self):
        if self.target.find("/")==1:
            host, range=self.target.split("/")
            counter=0
            while counter<=range:
                do_it(host)
                counter+=1
        else:
            do_it(host)
    
    def do_task(self):
        if self.validate_nmap():
            if self.validate_target():
                self.launch_scouting()
        else:
            print "[!!] There is a problem with organelles... please check external software!"
            
    def do_it(self, host):
        ping_recognition="nmap -sP "+host+" -oA "+host
        ping_clean="cat "+host+".gnmap >> cleaned."+host
        
        os.system(ping_recognition)
        os.system(ping_clean)
        file_cleaned="cleaned."+host
        file_descriptor=open("file_cleaned", "r")
        for line in file_descriptor.readlines():
            ip_target=line
        ip_target=ip_target[6:]
        ip_target=ip_target[:ip_target.find(" ")]
        
        
        