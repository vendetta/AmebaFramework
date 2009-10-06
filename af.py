#!/usr/bin/env python

import sys

from cytoplasm.af_shell import AFshell

def main():
    counter=0
    
    for item in sys.argv:
        counter+=1
        
    if counter==1:
        
        print " "
        print "             ,,,,,,,,"
        print "           ,|||````||||"
        print "     ,,,,|||||       ||,"
        print "  ,||||```````       `||"
        print ",|||`                 |||,"
        print "||`     ....,          `|||"
        print "||     ::::::::          |||,"
        print "||     :::::::'     ||    ``|||,"
        print "||,     :::::'               `|||"
        print "`||,                           |||"
        print " `|||,       ||          ||    ,||"
        print "   `||                        |||`"
        print "    ||                   ,,,||||"
        print "    ||              ,||||||```"
        print "   ,||         ,,|||||`"
        print "  ,||`   ||   |||`"
        print " |||`         ||"
        print ",||           ||"
        print "||`           ||"
        print "|||,         |||"
        print " `|||,,    ,|||"
        print "   ``||||||||`"
        print " "
        print " "
        
        while 1:
            sys.stdout.flush()
            user_input=raw_input("AFshell> ")
            if user_input.find(" ")>=0:
                command, parameter=user_input.split(" ")
                current_AFshell=AFshell(command, parameter)
                current_AFshell.execute_command()
            else:
                command=user_input
                current_AFshell=AFshell(command, None)
                current_AFshell.execute_command()

if __name__ == "__main__":
    main()