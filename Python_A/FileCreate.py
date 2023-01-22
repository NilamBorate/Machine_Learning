def CreateFile(FileName):
    fd = open(FileName,"w")      #File creation ,file created in the same location


def main():
    print("Enter the file to create")
    Name=input()

    CreateFile(Name)

if __name__=="__main__":
    main()    