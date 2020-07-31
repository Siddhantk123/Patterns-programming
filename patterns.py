#1
'''
0         **
1        ****
2       ******
3      ********
4     **********
5      ********
6       ******
7        ****
8         **
'''
#METHOD 1 (LENTHY)
def pat1():
    p=5
    for i in range(0,6):
            for k in range(0,p):
                print(" ",end="")
            p=p-1        
            for j in range(0,i):
                print("**",end="")
            print()
    a=1
    b=4

    for i in range(0,5):
        print((" "*a)+("**"*b))
        a=a+1
        b=b-1
    #METHOD 2(SMALL AND CRISP)

    a=4
    b=1
    for i in range(10):
        if i<=4:
            print(" "*a +"**"*b)
            a=a-1
            b=b+1

        else:
            
            print(((" ") * (a+1)) +(("**") * (b-1)))
            b=b-1
            a=a+1

#pat1()     

#2

'''
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''       

def pat2():
    a=1
    n=int(input("Enter the number of Rows\n"))+1
    for i in range(0,n):
        for j in range(0,i):
            print(a,end=" ")
            a+=1
        print()   
#pat2()              


#3
'''
ASCII code pattern
A 
B C
D E F
G H I J
K L M N O
P Q R S T U


'''
def pat3():
    a=65
    for i in range(0,7):
        for j in range (0,i):
            print(chr(a),end=" ")
            a+=1
        print()    

#pat3()
#4

'''
A
B B
C C C
D D D D 
E E E E E
F F F F F F 
G G G G G G G 
'''
def pat4():
    a=65
    for i in range(0,7):
        for j in range (0,i+1):
            print(chr(a),end=" ")
        a+=1
        print()    

#pat4()
#print(chr(65))

#5
'''
ASCII code pattern
a
b c
d e f
g h i j
k l m n o 
p q  r s t u 


'''
def pat5():
    a=97
    for i in range(0,7):
        for j in range (0,i):
            print(chr(a),end=" ")
            a+=1
        print()    

#pat5()

#6

'''
a
b b
c c c
d d d d
e e e e e
f f f f f f
g g g g g g g
'''
def pat6():
    a=97
    for i in range(0,7):
        for j in range (0,i+1):
            print(chr(a),end=" ")
        a+=1
        print()    

#pat6()

#7
#printing star patern
'''
  0 1 2 3 4 5 6
0   * *   *  *
1  *    *      *
2    *       *
3      *   *
4        *
'''
def pat7():
    for row in range(6):
        for col in range(7):
            if(row==0 and col%3!=0) or (row==1 and col%3==0) or(row-col==2) or (row+col==8):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print() 
pat1()
pat2()
pat3()
pat4()
pat5()
pat6()
pat7()       

















    
        
    



        

        





    

    







