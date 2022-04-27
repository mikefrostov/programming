#!/bin/python3


from datetime import datetime, timedelta
import logging



path = 'logfile.log'

def generateLogs():
    with open(path, 'a') as f:
        for i in range(1, 10):
            d = datetime.today() - timedelta(days=i)
            #print("writing: " + str(d))
            print(str(d), file=f)

def cutLogs():
    
    try:
        with open(path, 'r+') as f:
            lines = f.readlines()
            base = datetime.today()
            date_list = [base - timedelta(days=x) for x in range(7)]
            print(date_list)
            for line in lines:
                #datetoday = str(datetime.today()).split()[0]
                #print(line.split()[0])
                #print(line)
                #print(date_list[0])
                #print(date_list)
                #if line.strip() in range(datetime.today(), datetime.today() - timedelta(days=7)):
                #if line in date_list:
                print(line)
                #print(datetime.strptime(line.split()[0], "%Y-%m-%d"))
                #print(datetime.strptime(, "%Y-%m-%d"))
                if datetime.strptime(line.split()[0], "%Y-%m-%d") in date_list:        
                    #print("it is in date_list: "+ line)
                    print("line is in date_list: " + line)
                    pass

                #    print(str(line))
    except IOError as e:
        print('Failure', e)
    

if __name__ == "__main__":
    generateLogs()
    cutLogs()





