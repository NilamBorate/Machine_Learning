
class BookStore:
    NoOfBooks=0

    def __init__(self,Name,Author):
       
        self.Name=Name
        self.Author=Author
        value=int(input("How many books you want?\n"))
        self.NoOfBooks=self.NoOfBooks+value

    def Disply(self):
        print("{} by {} .N0 of books :{}".format(self.Name,self.Author,self.NoOfBooks))
     
     
def main():
    obj1=BookStore("Linux System Programming","Robert Love")
    obj1.Disply()

    obj1=BookStore("C Programming","Dennis Ritchie")
    obj1.Disply()


if __name__=="__main__":
    main()    