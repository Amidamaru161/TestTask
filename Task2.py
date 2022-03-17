import math
file_name1=input("Укажите абсолютный путь к файлу1: ")  #"C:\circle.txt" "C:\dot.txt""
file_name2=input("Укажите абсолютный путь к файлу2: ")
file_dot=open(file_name2,'r')
file_circle=open(file_name1,'r')
data_circle=[]
for line in file_circle:
    n=line.rstrip('\n')
    n=(list(filter(str.isdigit, n)))
    for string in n :
        data_circle.append(float(string))        
x_circle=data_circle[0]
y_cicrle=data_circle[1]
r_circle=data_circle[2]
for line in file_dot :
    n=line.rstrip('\n')
    n=list(filter(str.isdigit, n))
    x_y=list(map( float, n))
    x=x_y[0]
    y=x_y[1] 
    l=math.sqrt((x-x_circle)**2+(y-y_cicrle)**2)
    if l>r_circle:
        print(0,end='\n')
    elif l<r_circle:
        print(1,end='\n')
    else:
        print(2,end='\n')
    

file_dot.close()
file_circle.close()


            



