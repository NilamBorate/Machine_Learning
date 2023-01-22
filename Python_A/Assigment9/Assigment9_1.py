import os

def File_Cheack(FileName):
    
    if(os.path.exists(FileName)):
        print("File already existing")
        return
    else:
       print("No such file or directory")
       
def main():
    print("Enter the file name: ")
    Name=input()

    File_Cheack(Name)

if __name__=="__main__":
    main()    