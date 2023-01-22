import os

def CreateFile(FileName):
    
    if(os.path.exists(FileName)):
        print("File already existing")
        return
    else:
        fd = open(FileName,"w")      

def main():
    print("Enter the file to create")
    Name=input()

    CreateFile(Name)

if __name__=="__main__":
    main()    