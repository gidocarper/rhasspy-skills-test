import subprocess
import os.path
from os import path
import fnmatch, sys


class Skillstarter:

    def __init__(self):
        self.command = None
        self.process = subprocess
        skills_path = os.getcwd() + "/" + os.path.dirname(__file__) + 'skills'

        command = ''
        pattern = 'action-*.py'
        for root, dirs, files in os.walk(skills_path):
            for filename in fnmatch.filter(files, pattern):
                if path.exists(os.path.join(root, filename)):
                    command = command + "python3 " + os.path.join(root, filename).replace( skills_path,'skills') + " & "

        self.command = command[:-3]
        print('command after ' +  self.command)

    def start(self):
        print('start provessing')
        try:
            #self.process = subprocess.run(self.command, shell=True)
            self.process.Popen(self.command, shell=True)
        except (KeyboardInterrupt, SystemExit):
            print(' enden gelaender')
            self.process.terminate()
            self.process.kill()
        #subprocess.run(command, shell=True)

    def stop(self):
        print('stop provessing')
        #try:
        # self.process.terminate()
        # self.process.kill()
        # self.process = None
        #except:
        #    print(' errors while stopping')
        sys.exit()

if __name__ == '__main__':
    skillstarter = Skillstarter()
    skillstarter.start()



#subprocess.run(command, shell=True)
