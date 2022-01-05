import datetime,csv,re,os
def record():
    get_time_n_date()
    dbool = True
    if statuschecker(): 
        with open("statuschecker.txt", "w") as file:
            file.write("0")
    else:
        with open("statuschecker.txt", "w") as file:
            file.write("1")
            dbool = False
            
    keys = ["day","timein","timeout"] #have to revisit
    with open("productivity.csv", "a") as file:
        
        if not os.path.isfile("productivity.csv"):
            writer.writerow("{},{},{}".format(keys[0],keys[1],keys[2]))
        if dbool == True:
            string1 = datetimelist[0]
            string2 = str(datetimelist[1])
            string3 = "{},{},".format(string1,string2)
            file.write(string3)
        if dbool == False:
            string3 = str(datetimelist[1])
            file.write(string3+"\n") 
        

def statuschecker():
    with open("statuschecker.txt", "r+") as file:
        if not os.path.isfile("statuschecker.txt"):
            file.write("1")
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
    

    


record()