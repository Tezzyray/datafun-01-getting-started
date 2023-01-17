"""
Complete the script.
"""
temp_1=input('Please enter the temperature: ')
print('temp_1')
temp_2=input('Please enter the temperature: ')
print('temp_2')
temp_3=input('please enter the temperature: ')
print('temp_3')
temp1=int(temp_1)
print(temp1)
temp2=float(temp_2)
print(temp2)
temp3=float(temp_3)
print(temp3)
 
print ('Sum of temperatures:', temp1+ temp2+ temp3)
print('Average of temperature:', (round((temp1+temp2+temp3)/3, 2)))
print('Product of temperatures:', temp1*temp2* temp3)
print('min:', min(temp1,temp2,temp3))
print('max:', max(temp1,temp2,temp3))
print('range:', min(temp1,temp2,temp3), '-', max(temp1,temp2,temp3))

if temp3<0:
    print('Its below freeing temperature at the daycare')
if temp3==0:
    print('Its freezing at daycare')
if temp3>0:
    print('its above freezing at daycare')