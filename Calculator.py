def cal(n1,n2,op):
    if(op=="+"):
        result=n1+n2
    elif(op=="-"):
        result=n1-n2
    elif(op=="*"):
        result=n1*n2
    elif(op=="/"):
        result=n1/n2
    elif(op=="%"):
        result=n1%n2
    else:
        print("wrong choice!!")
    return result

def inp():
    n1=float(input("\n\tEnter first operand: "))
    n2=float(input("\n\tEnter second operand: "))
    return n1,n2
    
def operat():
    op=str(input("\n\tEnter the operator (+,-,*,/,%): "))
    return op

nvcon=True
a=True
print("\t    CALCULATOR\n")
while(a==True):
    if(nvcon==True):
        n1,n2=inp()
    op=operat()
    r = cal(n1,n2,op)
    print("\n\t    ",n1,op,n2)
    print("\t     =",int(r))

    con_check=str(input("\n\tDo you wish to continue? (Y/N): "))
    if(con_check=="N" or con_check=="n"):
        print("\n\tThank-you!!\n")
        break

    nv_check=str(input("\n\tDo you wish to enter new operands? (Y/N): "))
    if(nv_check=="N" or nv_check=="n"):
        nvcon=False
    else:
        nvcon=True