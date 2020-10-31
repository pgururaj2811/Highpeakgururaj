Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:27:37) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 

d = {'Fitbit plus'  : 7980,
     'Ipods'         : 22349,
     'MI Brand'      : 999,
     'Cult Pass'     : 2799,
     'Macbook'       : 229900,
     'Digital Camera': 11101,
     'Alexa'         : 9999,
     'Sandwich Toster': 2195,
     'Microwave Oven': 9800,
     'Scale'         : 4999 
   }

x = sorted(d.items(), key=lambda item: item[1])

n = int(input('Enter the number of employees:'))

min,index = x[n-1][1]-x[0][1],0
for i in range(0,len(x)-n):
   
    if (x[i+n-1][1] - x[i][1]) < min:
        
        min = x[i+n-1][1] - x[i][1]
        index = i

for i in range(index,index+n):
    print(x[i])
    
print('the difference between the chosen goodie with highest price and the lowest price is',x[index+n-1][1] - x[index][1])

    



