from sys import *   #  argv  command line argument argv[0]= file name,argv[1]=first number 


def Script_Task(No):
    if((No % 2)==0):
        print("It is even number")
    else:
        print("It is odd number")    

def main():
    print("________________Marvellous Infosystems Automation__________________")
    
    print("Automation script started with name: ",argv[0])

    if(len(argv) != 2):
        print("Error : Insufficeint argumnets")
        print("Use -h for help and use -u for usage of the script")
        exit()

    if((argv[1] == "-h") or (argv[1] == "-H")):
        print("Help : This script is used to perform _________")
        exit()

    elif ((argv[1]=="-u") or  (argv[1]=="-U")):
        print("Usage : provide ___ number of arguments as ")
        print("First Argument as : _______")
        print("Second Argument as : _______")
        exit()

    else:
        Script_Task(int(argv[1]))

if __name__=="__main__":
    main()    