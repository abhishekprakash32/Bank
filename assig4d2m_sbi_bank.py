# Using list, function, if else, if elif, for loop,while loop and random packages from https://pypi.org/
import random
import itertools
a = "Welcome To SBI"
print(a.center(72,'*'))
global withd1
global dep1
dep1 = ['500']
cd1 = ['CR']
 
    
def _create():
    import random
    global n
    n = random.randint(1000000000,90000000000)
    b = input("Enter Your Name = ")
    c = input("Enter Your Address =")
    e = input("Enter Your DOB =") 
    f = input("Enter Your Gender (M/F)=")
    g = input("Enter Your Mobile Number =")
    h = input("Enter Your Email Id =")
    i = input("Enter Your PAN Number =")
    j = input("Enter Your Aadhar Number =")
    k = input("Account Type (Saving/Current/Joint)=")
        
    print("__________________________________________________")
    print(f"Congrants Your Account With Account Number={n}") 
    print(f"Customer name={b}")
    print(f"Address={c}")
    print(f"DOB={e}")
    print(f"Gender={f}")
    print(f"Mobile No.={g}")
    print(f"Email ID={h}")
    print(f"PAN No.={i}")
    print(f"Aadhar No.={j}")
    print(f"Account type={k}")
    global bal
    bal = 500.0
    print(f"Account number={n}")
    global fix_acc
    fix_acc = n
    print(f"Your Current Balance = Rs.{bal}")
def glob():
    
    
    acc1 = int(input("Enter Account No.="))
    if acc1 == fix_acc:
        
        
        dep = float(input("Enter Amount To Deposite = "))
        dep2= f'{dep}'
        cd = 'CR'
        dep1.append(dep2)
        cd1.append(cd)
      
        print(f"Account No.={acc1}")
        print(f"Amount of Rs.{dep} Successfully Credited into Account Number -")
        global bal
        bal = bal + dep
        print(f"Total Balance={bal}")
        
    else:
        print("Please enter correct account number!!!!")
    
def glob1():
    
    
    acc2 = int(input("Enter Account No.="))
    if acc2 == fix_acc:
        withd = float(input("Enter Amount To Withdraw="))
        withd2 = f'{withd}'
        cd2 = 'DR'
        dep1.append(withd2)
        cd1.append(cd2)
        print(f"Account No.={acc2}")
        print(f"Amount of Rs.{withd} Successfully debited into Account Number -")
        global bal
        bal = bal-withd
        print(f"Total Balance={bal}-{withd}={bal}")
    else:
        print("Please enter correct account number!!!!")
    
def glob2():
    print(f"Account No.={n}")
    print("***********Your Mini Statement***********")
    print("Sr No.\tAmount\t\tCR/DR")
    
    l=1
    for k,m in zip(dep1[::-1],cd1[::-1]):
        
        print(f"{l}\t{k}\t\t{m}\t")
        l+=1
        if l == 6:
            break
while(True):
    a = int(input("To create account press 1 and To Exit for press 0:-"))
    if a == 0:
        exit()
    elif a == 1:
        _create()
        d = 'yes'
        while(d == 'yes'):    
            print("SBI Offers Following Services ")
            print("1\tDeposite Money")
            print("2\tWithdraw Money")
            print("3\tMini Staement [Last 5 Transactions]")
            print("4\t Exit")
            d = int(input("Enter your choice=")) 
            if d not in (1,2,3,4):
                print("Number you entered is invalid")
            elif d == 1:
                glob()
            elif d == 2:
                glob1()
            elif d == 3:
                glob2()
            elif d == 4:
                exit()
            d = input("Do you want to continue [yes/no] = ") 
    elif a != 1:
        print("Please enter correct number!!!!")
   

