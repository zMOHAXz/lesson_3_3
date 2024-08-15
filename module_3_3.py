def print_params(a=1,b='str',c=True):
    print(a,b,c)


print_params()
print_params('Home', 0.45)
print_params(b=25)
print_params(c=[1,2,3])
print()

values_list = [737, True]
values_dict = {'c': 0.25}


print_params(*values_list, **values_dict)
print()

values_list_2 = ['33', 33]


print_params(*values_list_2, 0.33)
