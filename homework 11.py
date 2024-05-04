def print_params (a= 1,b= 'apple',c = True):
   print (a,b,c)

print_params(5)
print_params('kiwi')
print_params(1)
print_params()
print_params(b=25)
print_params(c=[1,2,3])

values_list=[1,5,7]
print_params(*values_list)

values_dict={'a':1,'b':'apple','c':True}
print_params(**values_dict)

values_list_2= [2,1]
print_params(*values_list_2,42)



