#! /usr/bin/python

import os
import sys

commands = ["rm", "cvs remove"]
path = sys.argv[1]

dirs = os.walk(path, topdown=False)

for threeple in dirs:

    for name in threeple[2]:
        abspath = os.path.relpath( threeple[0].replace( " ", "\\ " )+"/"+name.replace(" ","\\ " ) )
        for command in commands:
            try:
                if abspath.find("CVS") == -1:
                    command_string = command+" "+abspath
                    print "\n\nRunning '"+command_string

                    os.system( command_string )
            except KeyboardInterrupt:
                print "Keyboard Interrupt received. Exiting"
                sys.exit()


