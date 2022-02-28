import subprocess
import time
import sys
import os
import re
print("""\n
                      `. ___
                     __,' __`.                _..----....____
         __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
   _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
 ,'________________                          \`-._`-','
  `._              ```````````------...___   '-.._'-:
     ```--.._      ,.                     ````--...__\-.
             `.--. `-`                       ____    |  |`
               `. `.                       ,'`````.  ;  ;`
                 `._`.        __________   `.      \'__/`
                    `-:._____/______/___/____`.     \  `
                                |       `._    `.    \.
                                `._________`-.   `.   `.___

AUTOMATOR
""")
pingip = input("what remote host to ping after CMD has run?")
cmdping = ('ping',pingip,'-c 3')
log = open("log.txt", "w")
with open("cmd.txt", "r") as file:
        content = file.read()
        content_list = content.splitlines()
        file.close()

cleanping = re.sub("[^a-zA-Z0-9 . -]+","",str(cmdping))

for f in content_list:
        p = os.popen(f)
        p1 = os.popen(cleanping)
        pingoutput = p1.read()
        if 'Destination Host Unreachable' in pingoutput:
                print("can't see remote host")
                time.sleep(3)
                p2 = os.popen(cleanping)
                ping2output = p2.read()
                if 'Destination Host Unreachable' in ping2output:
                        with open("badcmdlist.txt", "w") as output:
                                output.write(f)
                                output.close()
                                sys.exit(1)
                
        else:
                print(f, "has run")
                print(f, "HAS RUN", file=log)






log.close()
