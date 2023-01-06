class employee:
    empno=0;
    empname="";
    basic=0;
    da=0;
    hra=0;
    gross=0;

    def getdata(emp):
        emp.empno=int(input("enter employee number: "))
        emp.empname=input("enter name of employee: ")
        emp.basic=int(input("enter basic salary: "))
        emp.da=.10*emp.basic
        emp.hra=0.05*emp.basic
        emp.gross=emp.da+emp.hra+emp.basic

    def putdata(emp):
        print("\tempno\tname\tbasic\tda\thra\tgross ")
        print("\t",emp.empno,"\t",emp.empname, "\t",emp.basic,"\t ",emp.da,"\t",emp.hra,"\t  ",emp.gross)
    
total_emp=int(input("total number of employee:  "))
emplist=[]
i=0
while i<total_emp:
    emplist.append(employee())
    i=i+1

for i in emplist:
    i.getdata()

for i in emplist:
    i.putdata()
