import schedule
import os
import psutil
import time
from sys import *


def ProcessDisply(log_dir = "Marvellous"):
    listprocess = []

    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-" * 80
    log_path = os.path.join(log_dir,"MarvellousLog%s.log" %(time.ctime()))
    f = open(log_path,'w')
    f.write(separator + "\n") 
    f.write("Marvellous Infosystems Process Logger : "+time.ctime() + "\n") 
    f.write(separator + "\n") 
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=["pid","name","username"])
            vms = proc.memory_info().vms/(1024 * 1024)
            pinfo['vmsr'] = vms
            listprocess.append(pinfo)

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass


    for element in listprocess:
        f.write("%s\n" % element)

def main():
    print("Marvellous Infosystems by piyush khairnar")
    print("Application name : "+argv[0])

    if(len(argv) != 2):
        print("Error: Invalid number of argumnets")
        exit()

    if(argv[1]=="-h")  or (argv[1]=="-H"):
        print("This Script is used log record of running processes")  
        exit()

    if(argv[1]=="-u")  or (argv[1]=="-U"):
        print("Usage : ApplicationName AbsolutePath_of_Directory")  
        exit()


    try:
        ProcessDisply(argv[1])
        
    except ValueError:
        print("Error : Invalid datatype of input")  

    except Exception as E:
        print("Error : Invalid input",E)      
    
if __name__ =="__main__":
    main()
    
