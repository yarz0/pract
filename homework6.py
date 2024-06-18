my_dict = {'wifi' : 'qwerty' , 'admin' : 'admin' , 'login' : 'password' , 'user' : 1234567890}
print(my_dict)
print(my_dict['wifi'])
print(my_dict.get('wifi1', 'Not existing value: None'))
my_dict.update({'user1' : 123456 , 'Kirill' : 10101010 })
del my_dict['user1']
print(my_dict)

my_set = {1, 2, 3, 4, 5 ,1 ,2, 3, 'String', True, (1, 2, 3)}
print(my_set)
my_set.update([6,9])
my_set.remove('String')
print(my_set)
