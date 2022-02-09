import datetime,csv,re,os,time
def record():
    get_time_n_date()
    dbool = True
    if statuschecker(): 
        with open(os.path.join(rootdirectory,"statuschecker.txt"), "w") as file:
            file.write("0")
    else:
        with open(os.path.join(rootdirectory,"statuschecker.txt"), "w") as file:
            file.write("1")
            dbool = False
            
    keys = ["day","timein","timeout"] #have to revisit
    if not os.path.isfile(os.path.join(rootdirectory,"productivity.csv")):
            with open(os.path.join(rootdirectory,"productivity.csv"), "w") as file:
                file.write("day,timein,timeout\n") 
    with open(os.path.join(rootdirectory,"productivity.csv"), "a") as file:
        if dbool == True:
            string1 = datetimelist[0]
            string2 = str(datetimelist[1])
            string3 = "{},{},".format(string1,string2)
            file.write(string3)
            print("Time Record Start")
            time.sleep(3)

        if dbool == False:
            string3 = str(datetimelist[1])
            file.write(string3+"\n")
            print("Time Record End")
            time.sleep(3) 
        

def statuschecker():
    if not os.path.isfile(os.path.join(rootdirectory,"statuschecker.txt")):
        with open(os.path.join(rootdirectory,"statuschecker.txt"),"w") as file:
            file.write("1")
 
    with open(os.path.join(rootdirectory,"statuschecker.txt"), "r+") as file:
        string = file.read()
        if string == "1":
            #file.write("0")
            return True
        elif string == "0":
            #file.write("1")
            return False    

def time_converter(regexresult):
    return int(regexresult[2])*3600+int(regexresult[3])*60+int(regexresult[4])
datetimelist = []
def get_time_n_date():
    timey = str(datetime.datetime.now())
    regexstring = r"^202\d-\d\d-(\d\d) (\d\d):(\d\d):(\d\d)"
    regexresult = re.search(regexstring,timey)
    int_time = time_converter(regexresult)
    datetimelist.append(regexresult[1])
    datetimelist.append(int_time)
    

if not os.path.isdir(os.path.join(os.path.expanduser('~'),"Documents","productivity-tracker")):
    os.mkdir(os.path.join(os.path.expanduser('~'),"Documents","productivity-tracker"))

rootdirectory = os.path.join(os.path.expanduser('~'),"Documents","productivity-tracker")
 

record()