file1 = open("myprog1.py","w")
file2 = open("myprog2.py","w")


prog1= """
def replace(s):
    strn = s.replace("a" or "A",'*')
    print(strn)
def reverse(s):
    lst=[]
    newstr=''
    words = s.split(' ')
    for i in words:
        revword=i[::-1]
        lst.append(revword)
    newstr=''.join(lst)
    print("original string is ", s)
    print("Reversed string is ", newstr)

while(1):
    print("1 replace 'a' by '*' ")
    print("2 Reverse every word in a string")
    print("3 Quit")
    print()
    choice = int(input("Enter your choice "))
    if (choice==1):
        s =  input("Enter the string")
        replace(s)
    elif (choice==2):
        s = input("Enter the string ")
        reverse(s)
    elif(choice==3):
        break
    else:
        print("Wrong Choice")
    

"""




prog2="""
def replist(lst):
    rlist=lst*2
    print("Original List", lst)
    print("Repiclated list", rlist)
    rlist.sort()
    print("Replicated List sorted in descending order", rlist)
    print()
    rlist.sort(reverse=True)
    print("Replicated List sorted in descending order",rlist)
    print()
def swaplist(lst):
    n=len(lst)
    print("Original List ", lst)
    if(n%2!=0):
        n= n-1
    for i in range(0,n,2):
        lst[i],lst[i+1]=lst[i+1],lst[i]
    print("List after swapping ",lst)
    print()
while(1):
    print("1 Replicating and sorting the list")
    print("2 Swapping elements in a list")
    print("3 Quit")
    choice = int(input("Enter the choice "))
    if(choice==1):
        lst=eval(input("Enter the list elements "))
        print()
        replist(lst)
    elif(choice==2):
        lst=eval(input("Enter the List elements"))
        print()
        swaplist(lst)
        print()
    elif(choice==3):
        break
    else:
        print("Wrong Choice")
"""


prog3=""" 
t=()
n=int(input("enter the number of students"))
for x in range(1,n+1):
    print("enter the marks of student",x)
    t1=()
    for y in range(1,4):
        print("enter the mark in subject",y)
        mark=float(input())
        t1=t1+(mark,)
    print("marks of student",x,"\t=",t1)
    t=t+(t1,)
print("marks of all the five students are as follows")
print(t)
for i in range(len(t)):
    tot=sum(t[i])
    avg=round(tot/3,2)
    print("\n student",i+1,"\t marks=",t[i],"\t Total=",tot,"\t Average=",avg )

"""

prog4="""
def palindrome(s):
    r=s[::-1]
    print("reversed string is",r)
    if(r==s):
        print("the string is palindrome")
    else:
        print("the string is not a palindrome")
while(1):
    print("1 to fine whether the given string is palindrome or not")
    print("2 quit")
    print()
    choice=int(input("enter your choice"))
    if(choice==1):
        s=input("enter the string")
        palindrome(s)
        print()
    elif(choice==2):
        break
    else:
        print("wrong choice")

"""

prog7="""
import pickle
def create_stu():
    f1=open("file.dat","wb+")
    d={}
    n=int(input("no of records to add:"))
    for i in range(n):
        d["rno"]=int(input("enter the student roll number:"))
        d["sname"]= input("enter the student name:")
        pickle.dump(d,f1)
    f1.close()
def search_stu():
    try:
        f1=open("file.dat","rb")
        x=int(input("enter the roll number to search:"))
        while True:
            y=pickle.load(f1)
            if y["rno"]==x:
                print("student name is:",y["sname"])
                break
    except:
        print("record not present")
        f1.close()
while True:
    print('''1.create a student record.
2.search a student name
3.exit''')
    a=int(input("enter your choice:"))
    if a==1:
        create_stu()
    elif a==2:
        search_stu()
    elif a==3:
        break
    else:
        print("entered a wrong choice")

"""

prog5 =""" 
def sep_word():
    f1=open("file.txt","r")
    for line in f1:
        x= line.split()
        for word in x:
            print(word,"#",end="")
    print()
    f1.close()
def file_copy():
    f1 = open("file.txt","r")
    f2 = open("file1.txt","w")
    for line in f1:
        for i in line:
            if i in "Aa":
                break
            else:
                f2.write(line)
    f1.seek(0)
    f2.seek(0)
    a=f1.read()
    b= f1.read()
    print("Original File ", a)
    print("Copied File, ",b)
    f1.close()
    f2.close()
while True:
    print('''1 Seperate the words by # 
          2 Remove lines containing 'a' and copy the file 
          3 Exit''')
    a = int(input("Enter your choice"))
    if a==1:
        sep_word()
    elif a==2:
        file_copy()
    else:
        break


"""

prog6="""
def count():
    vowels=0
    consonants=0
    upper_case=0
    lower_case=0
    f1=open("file.txt","r")
    y=f1.read()
    for i in y:
        if i.isalpha():
            if i.isupper():
                upper_case+=1
            else:
                lower_case+=1
            if i in ["A","E","I","O","U","a","e","i","o","u"]:
                vowels+=1
            else:
                consonants+=1
    print(f"Vowels={vowels}, consonants={consonants}, Upper Case={upper_case}, Lower Case = {lower_case}")
    f1.close()
while True:
    print("1 To count the number of vowels/consonants/uppercase/lowercase\n2 Exit")
    a = int(input("Enter the choice"))
    if a ==1:
        count()
    else:
        break

"""

prog8="""
import csv
def create():
    f1 = open("file.csv", "w+", newline='')
    wob = csv.writer(f1)
    n = int(input("Enter the number of records"))
    for i in range(n):
        user_id=input("Enter the user id: ")
        password=input("Enter the password: ")
        a = [user_id,password]
        wob.writerow(a)
    f1.close()
def search(y):
    f1 = open("file.csv", "r")
    rob= csv.reader()
    for i in rob:
        if i[0] ==y:
            print("password is ", i[1])
            break
    else:
        print("Record not present")
while True:
    print('''
          1 Create CSV with userid and password
          2 Search Password for userid
          3 exit
''')
    x = int(input("Enter the choice: "))
    if x ==1:
        create()
    elif x==2:
        y = input("Enter the userid: ")
        search(y)
    elif x==3:
        break
    else:
        print("Invalid Option")
                

"""


prog9= """
import random

def startthegame(mylist):
    count=1
    while count<=6:
        randnumb= random.randint(1,6)
        mylist.append(randnumb)
        count+=1
    return mylist
mylist=[]
newlist=[]
numlist=startthegame(mylist)
print("******************* STIMULATING DICE RANDOM NUMBER GENERATION *******************")
for x in range(1,7):
    print(f"Number generanted at the {x} time of dice thrown.. {numlist[x-1]}")
    print("**************************************")
    if(len(numlist))==len(set(numlist)):
        print("All numbers from 1 to 6 have been generated successfully")
    else:
        print("Some numbers have been generated multiple times")
        for x in numlist:
            if(x not in newlist):
                newlist.append(x)
            if numlist.count(x)>1:
                print(x,"has been generated for ", numlist.count(x),"times")
            else:
                continue
    """


prog10="""
import pickle
def create_stu():
    f1 = open('file.dat','wb+')
    n=int(input("Enter the number of Records "))
    for i in range(n):
        rno=int(input("Enter the roll number "))
        name=input("Enter the name ")
        mark=int(input("Enter the mark "))
        lst=[rno,mark,name]
        pickle.dump(lst,f1)
    f1.close()
def update():
    f1 = open("file.dat","rb+")
    re=[]
    try:
        while True:
            x=pickle.load(f1)
            re.append(x)
    except:
        f1.seek(0)
        n=int(input("Enter roll number to update mark "))
        for i in re:
            if i[0]==n:
                y= int(input("Enter the mark to update "))
                i[2]=y
                pickle.dump(i,f1)
            else:
                pickle.dump(i,f1)
    f1.close()
def display():
    try:
        f1=open("file.dat","rb")
        while True:
            record=pickle.load(f1)
            print(record)
    except:
        f1.close()
while True:
    print('''
          1. create student record
          2. input a roll number
          3. display file after updation
          4. exit
''')
    a = int(input("Enter the choice "))
    if a ==1:
        create_stu()
    elif a==2:
        update()
    elif a==3:
        display()
    else:
        break"""





def prog():
    print("""
          1. Menu Driven Python programs for string operations
          2. Menu Driven Python programs for list operations
          3. Nested tuple python programs to store marks of students
          4. Python program to find whether the given str is palindrome or not
          5. Read a file line by line and display each word seperated by '#'
          6. Function to count the number of vowels consonants uppercase lowercase
          7. Create binary file with name and roll no
          8. Create a CSV file bu entering username and password
          9. Write a random number generator that generates random numbers from 1 to 6 (stimulaes dice)
          10.Create a binary file with roll number names and marks

""")
    yp1= int(input("Enter your first program number: "))
    yp2 = int(input("Enter your second program number: "))
    return (yp1,yp2)

def program1(n):
    if n==1:
        file1.write(prog1)
    if n==2:
        file1.write(prog2)
    if n==3:
        file1.write(prog3)
    if n==4:
        file1.write(prog4)
    if n==5:
        file1.write(prog5)
    if n==6:
        file1.write(prog6)
    if n==7:
        file1.write(prog7)
    if n==8:
        file1.write(prog8)
    if n==9:
        file1.write(prog9)
    if n==10:
        file1.write(prog10)

def program2(n):
    if n==1:
        file2.write(prog1)
    if n==2:
        file2.write(prog2)
    if n==3:
        file2.write(prog3)
    if n==4:
        file2.write(prog4)
    if n==5:
        file2.write(prog5)
    if n==6:
        file2.write(prog6)
    if n==7:
        file2.write(prog7)
    if n==8:
        file2.write(prog8)
    if n==9:
        file2.write(prog9)
    if n==10:
        file2.write(prog10)
def start():
    a = prog()
    p1=a[0]
    p2=a[1]
    program1(p1)
    program2(p2)
    
