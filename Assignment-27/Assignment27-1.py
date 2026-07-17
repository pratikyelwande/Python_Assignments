class BookStore:
    NoOfBooks=0
    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoOfBooks += 1
    def Display(self):
        print(f"Book Name is {self.Name} and Author is {self.Author}")
        print(f"No of books : {BookStore.NoOfBooks}")

def main():
    obj1 = BookStore("Linux Sys","Robert")
    obj2 = BookStore("C Programming","Dennis")
    obj1.Display()
    obj2.Display()

if __name__ == "__main__":
    main()

