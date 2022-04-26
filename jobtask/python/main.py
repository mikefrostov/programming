#!/bin/python3


from datetime import datetime, timedelta
import logging

def generateLogs():
    with open('logfile.log', 'a') as f:
        for i in range(1, 10):
            d = datetime.today() - timedelta(days=i)
            print("writing: " + str(d))
            print(str(d), file=f)

def cutLogs():
    pass

if __name__ == "__main__":
    generateLogs()
#    cutLogs()





