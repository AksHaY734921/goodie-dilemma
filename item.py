import random               #to select random variable
while(1):                   #adding one while loop to get the input continuosly from the user
 items={'fitbitplus':7980, 'ipod':22349, 'miband':999, 'cultpass':2799, 'macbookpro':229900, 'digitalcamara':11101, 'alex':9999, 'sandwichroaster':2195,
          'microwave ovan':9800, 'scale':4999}   #storing items in dictionary

 var1=list()
 var2=list()                   #creating two empty list
 item_list=list(items)   #converting dictionary to list


 employee=int(input("enter number of employee"))     #taking input from the user
 for i in range(1, employee+1):
    var1.append(random.choice(item_list))        #choosing items using random function and appending it into list var1         
 for i in range (0, employee):
     print(var1[i],":",items.get(var1[i]))         #printing appended key and values of that key present in dictonary using get function
     var2.append(items.get(var1[i]))            #appending the value of keys to the list c
   

 max_val=max(var2)                          #finding maximum value from choosen item
 min_val=min(var2)                          #finding minimum value from choosen item
 difference=max_val-min_val              #finding the difference between maximum and minimum
 print("and the difference between the chosen goodies with highest price and the lowest price is",difference)    #printing the difference
 
