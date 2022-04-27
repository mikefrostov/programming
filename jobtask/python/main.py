#!/bin/python3


from datetime import datetime, timedelta
import logging


path = 'logfile.log'

def generateLogs():
    with open(path, 'a') as f:
        for i in range(1, 10):
            d = datetime.today() - timedelta(days=i)
            print("writing: " + str(d))
            print(str(d), file=f)

def cutLogs():
    
    try:
        with open(path, 'r+') as f:
            lines = f.readlines()
            print(str(lines))
            for line in lines:
                print(str(line))
                #if line.strip() in range(datetime.today(), datetime.today() - timedelta(days=7)):
                #    print(str(line))
    except IOError as e:
        print('Failure', e)
    

if __name__ == "__main__":
    generateLogs()
    cutLogs()





