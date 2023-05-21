# n=int(input("enter a number : "))
# print('your number is : ',n)
# studentList=['vaasu','atharva','jyoti']
# for i in studentList:
    
#     print('student name is  ',i)

# i=20

# while i>10:
#     print(i)
#     i=i-3
# n=int(input("enter a no."))
# for i in range(0,n):
#     if(i%2!=0):
#         neg=-i
#         print(neg,end=' ')
#     else:
#         print(i,end=' ')
# name='atharava'
# print(name.find('z'))
import matplotlib.pyplot as p
months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
sales=[12000,10000,8300,13400,6700,9485,8499,2039,27840,738,9303,9191]
sales2=[1200,13000,7300,14800,7600,9850,8599,2039,25840,538,9803,119900]
p.plot(months,sales)
p.plot(months,sales2)
p.ylabel('amount(in Rs.)')
p.xlabel('Month')
p.title('Sales of comparison')
p.show()

# n=int(input('enewhfuehfiejfhi121314h'))
# for i in range(0,n):
#     bin=str(i)
#     if(bin.find('2')==-1 and bin.find('3')==-1 and bin.find('4')==-1 and bin.find('5')==-1 and bin.find('6')==-1 and bin.find('7')==-1 and bin.find('8')==-1 and bin.find('9')==-1):
#         print(i,end=' ')


# print('\\nYou Are Hacked !!!')