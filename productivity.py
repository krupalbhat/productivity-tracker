#! /usr/bin/env python3
import datetime,csv,re,os,time
# All file locations
productivity_folder = os.path.join(os.path.expanduser('~'),"Documents","productivity-tracker")
status_checker_file = os.path.join(productivity_folder,"statuschecker.txt") 
productivity_file= os.path.join(productivity_folder,"productivity.csv")
def record():
    get_time_n_date()
    dbool = True
    if statuschecker(): 
        with open(status_checker_file, "w") as file:                   #Changes the status of file from not recording to recording
            file.write("0")
        reason = input("write the activity you are doing?")    
    else:
        with open(status_checker_file, "w") as file:                #Changes the status of file from recording to not recording
            file.write("1")
            dbool = False
            
    if not os.path.isfile(productivity_file):
            with open(productivity_file, "w") as file:          # Creates productivity.csv if it doesnt exist
                file.write("day,activity,timein,timeout\n") 
    with open(productivity_file, "a") as file:
        if dbool == True:
            string1 = datetimelist[0]
            string2 = str(datetimelist[1])
            string3 = "{},{},{},".format(string1,reason,string2)                                     # while recording starts it will write Date and Record start Time to csv file 
            file.write(string3)
            print("Time Record Start")

        if dbool == False:
            string3 = str(datetimelist[1])                                  # while recording ends it will write and Record end Time to csv file
            file.write(string3+"\n")
            print("Time Record End")
            time.sleep(3) 
        

def statuschecker():
    if not os.path.isfile(status_checker_file):
        with open(status_checker_file,"w") as file:    # Creates file called status checker and writes 1 to status checker 
            file.write("1")
 
    with open(status_checker_file, "r+") as file:
        string = file.read()
        if string == "1":
            #file.write("0")
            return True
        elif string == "0":                                                       # Checks the status and returns True if the time is not recording and vice versa
            #file.write("1")                                                      
            return False    

def time_converter(regexresult):
    return int(regexresult[2])*3600+int(regexresult[3])*60+int(regexresult[4]) #to convert hours and minutes to seconds

datetimelist = []

def get_time_n_date():
    timey = str(datetime.datetime.now())
    regexstring = r"^202\d-\d\d-(\d\d) (\d\d):(\d\d):(\d\d)"
    regexresult = re.search(regexstring,timey)
    int_time = time_converter(regexresult)
    datetimelist.append(regexresult[1])
    datetimelist.append(int_time)
    

if not os.path.isdir(productivity_folder):
    os.mkdir(productivity_folder)

 

record()
