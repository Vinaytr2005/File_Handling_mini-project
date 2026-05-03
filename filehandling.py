from pathlib import Path
import os
def readfileandfolder():
    path=Path("")
    items=list(path.rglob("*"))
    for i,items in enumerate(items):
        print(f"{i} : {items}")

def createfile():
    try:
        readfileandfolder()
        name=input("please tell ur file name: ")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data=input("enter a contect to insert into file:- ")
                fs.write(data)
            print(f"file created sucessfully....")
        else:
            print("this file alredy exist.!")
    except Exception as err:
        print(f"error occurred {err}")

def readfile():
    try:
        readfileandfolder()
        name=input("which file u want to read: ")
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data=fs.read()
                print(data)
            print("read sucessfully....!")
        else:
            print("file doesnot exist...!")
    except Exception as err:
        print(f"an error occurred as {err}")

def updatefile():
    try:
        readfileandfolder()
        name=input("tell file name to  update: ")
        p=Path(name)
        if p.exists() and p.is_file():
            print("press 1 for changing the name of your file: ")
            print("press 2 for overwriting for ur file: ")
            print("press 3 for appending something for ur file: ")
            res=int(input("tell your response: "))
            if res==1:
                name2=input("tell your new file name: ")
                p2=Path(name2)
                p.rename(p2)
            if res==2:
                with open(p,"w") as fs:
                    data=input("tell what u want to overwrite: ")
                    fs.write(data)
            if res==3:
                with open(p,"a") as fs:
                    data=input("tell what u want to write: ")
                    fs.write(data)
    except Exception as err:
        print(f"an error occurred as {err}")

def deletefile():
    try:
        readfileandfolder()
        name=input("which file u want to delete: ")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("file removed sucessfullly...!")
    except Exception as err:
        print(f"an error occurred as {err}")

print("1 for creating a file")
print("2 for reading a file")
print("3 for updatinga file")
print("4 for delete a file")
choice=int(input("enter a choice: "))
if choice==1:
    createfile()
elif choice==2:
    readfile()
elif choice==3:
    updatefile()
elif choice==4:
    deletefile()