#!/usr/bin/env python

import sys

class AFshell:
    
    """AFShell: command line interface"""

    
    def __init__(self, command, parameter):
        self.command=command
        self.parameter=parameter
        
    def help(self):
        if self.parameter==None:
            print " "
            print "  Core commands"
            print "  ============="
            print " "
            print "  Command          Description"
            print "  -------          -----------"
            print "  "
            print "  help             Show details about the core commands"
            print "  show             Show details about resources"
            print "  select           Select a resource for use it"
            print "  load             Load a external resource for use it"
            print "  save             Save options for future sesions"
            print "  magic            Use pre-defined scripts for doing something"
            print "  version          Show information about Ameba Framework"
            print "  exit             Exit from a resource"
            print "  quit             Exit from Ameba Framework"
            print " "
            print "  Try \"AFshell> help [command]\" for details..."
            print " "
        elif self.parameter=="help":
            print " "
            print "  Show information about compoverver onents and recources."
            print " "
            print "  Syntaxis:"
            print "  AFshell> help [options]"
            print " "
            print "  Example:"
            print "  AFshell> help help"
            print " "
        elif self.parameter=="magic":
            print " "
            print "  Use pre-defined script for do task."
            print " "
            print "  Syntax:"
            print "  AFshell> magic [task]"
            print " "
            print "  Example:"
            print "  AFshell> magic scouting"
            print " "
            
        elif self.parameter=="show":
            print " "
            print "  Show options related to a command, resource or component."
            print " "
            print "  Syntaxis:"
            print "  AFshell> show [options]"
            print " "
            print "  Example:"
            print "  AFshell> show exploits"
            print " "
        elif self.parameter=="select":
            print " "
            print "  Select a component for use it."
            print " "
            print "  Syntax:"
            print "  AFshell> select [option]"
            print " "
            print "  Example:"
            print "  AFshell> select test/hackme"
            print " "
        elif self.parameter=="load":
            print " "
            print "  Load a external resource for uset it."
            print " "
            print "  Syntax:"
            print "  AFshell> load [resource]"
            print " "
            print "  Example:"
            print "  AFshell> load Trapper"
            print " "
        elif self.parameter=="save":
            print " "
            print "  Save enviroment preferences for future use."
            print " "
            print "  Syntax:"
            print "  AFshell> save"
            print " "
        elif self.parameter=="version":
            print " "
            print "  Show version of Ameba Framework."
            print " "
            print "  Syntax:"
            print "  AFshell> version [options]"
            print " "
        elif self.parameter=="exit":
            print " "
            print "  Back to a previos state."
            print " "
            print "  Syntax:"
            print "  AFshell> exit"
            print " "
        elif self.parameter=="quit":
            print " "
            print "  Exit from Ameba."
            print " "
            print "  Syntax:"
            print "  AFshell> quit"
            print " "
        else:
            print " "
            print "Page not found, please try again..."
            print " "
    
    def show(self):
        if self.parameter=="magic":
            print " "
            print " Magic task "
            print "============"
            print " "
            file_reader=open("./cytoplasm/af_magic_task.afc", "r")
            for line in file_reader.readlines():
                print line
            file_reader.close
        else:
            print " "
            print "[!!] Ameba can't show the thing that you want!"
            print " "
    
    def version(self):
        print " "
        print "  ---------------------------------------"
        print " | Ameba Framework 0.0.3                 |"
        print " | Copyright -c- 2009                    |"
        print " | Carlos A. Lozano <vendetta@bugcon.org>|"
        print "  ---------------------------------------"
        print " "
    
    def quit(self):
        sys.exit(0)
        
    def execute_command(self):
        
        if self.command=="quit":
            self.quit()
        if self.command=="version":
            self.version()
        if self.command=="help":
            self.help()
        if self.command=="show":
            self.show()