num = []

for i in range(4):
   valor = int(input("Valor"))
   
   while i > 3:
        if valor > num[i]:
            num.append(valor)
            break
    
   num.append(valor)
           
#    if i == 0:
#       num.append(valor)
#    elif i == 1 & valor > num[0]:
#       num.append(valor)
#    elif i == 2 & valor > num[1]:
#       num.append(valor)
#    elif i == 3:
#       num.append(valor)
      
print(num)