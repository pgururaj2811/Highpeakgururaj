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
