#! /usr/bin/python

import os
import sys

commands = ["cvs add"]
path = sys.argv[1]

dirs = os.walk(path)

for threeple in dirs:
  try:
    #add directory
    for command in commands:
        abspath = os.path.relpath( threeple[0].replace( " ", "\\ " ) )
        command_string = command+" "+abspath
        print "\n\nRunning '"+command_string

        os.system( command_string )

    #add files
    for name in threeple[2]:
        abspath = os.path.relpath( threeple[0].replace( " ", "\\ " )+"/"+name.replace(" ","\\ " ) )
        for command in commands:
            if abspath.find("CVS") == -1:
                command_string = command+" "+abspath
                print "\n\nRunning '"+command_string

                os.system( command_string )

  except KeyboardInterrupt:
    print "Keyboard Interrupt received. Exiting"
    sys.exit()
