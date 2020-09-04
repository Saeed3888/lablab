# Author: Saeed Alyami ssa5468@psu
# Collaborator: Vincent Barnes vjb5182@psu
# Collaborator: Lucas Yancey lcy5032@psu,edu
tempo = input ("Enter temperature: ")
corf = input ("Enter unit in F/f or C/c: ")
tempo = float(tempo)

if(corf =="F" or corf == "f"):
  fahrenheit = tempo
  celsius = (fahrenheit - 32) * (5/9)
  celsius = str(celsius)
  fahernheit = str(fahrenheit) 
  print(f'{fahrenheit}° in Fahrenheit is equivalent to {celsius}° Celsius.') 

elif(corf =="C" or corf == "c"): 
  celsius = tempo
  fahrenheit = celsius *1.8 + 32
  celsius = str(celsius)
  fahrenheit = str(fahrenheit)
  print(f'{celsius}° in Celsius is equivalent to {fahrenheit}° Fahrenheit.')
else:
     print(f'Invalid unit({corf}).')