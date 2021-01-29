import datetime
from datetime import date
import collections

#creating a dictionary
my_dict = {}

# input dictionary
n = int(input('number of days:' ))
for i in range(n):
    data = input('Enter date (in YYYY-MM-DD format) & it\'s corresponding value separated by ":" (for example: 2020-05-20:5) : ')
    temp = data.split(':')
    my_dict[temp[0]] = int(temp[1])

# Displaying the dictionary
print(my_dict)

list_1 = list(my_dict.keys())
list_2 = list(my_dict.values())

#print ("Value : %s" %  dict.get('Age'))

x = len(list_1)
my_dict_1 = {}
my_list = []
for i in range(x):
    date = list_1[i]
    year, month, day = map(int, date.split('-'))
    date1 = datetime.date(year, month, day)
    z = date1.strftime("%A")
    l = list_1.index(date)
    y = list_2[l]
    if z not in my_dict_1.keys():
        my_dict_1[z] = y
    else:
        key_list = list(my_dict_1.keys())
        val_list = list(my_dict_1.values())
        p = key_list.index(z)
        q = val_list[p]
        r = q + y
        my_dict_1[z] = r
list_3 = list(my_dict_1.keys())
list_4 = list(my_dict_1.values())
m = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
raj_list = list(sorted(list_3, key=m.index))
my_dict_2 = {}
for i in raj_list:
    p_1 = my_dict_1.get(i)
    my_dict_2[i] = p_1
key_list_1 = list(my_dict_2.keys())
val_list_1 = list(my_dict_2.values())
for k in m:
    if k not in key_list_1:
        k_2 = m.index(k)
        k_3 = m[k_2-1]
        k_4 = key_list_1.index(k_3)
        if (k_4 + 1) < len(key_list_1):
            k_5 = key_list_1[k_4 +1]
            k_6 = m.index(k_5)
            r_1 = k_6 - k_2
            v_1 = val_list_1[k_4]
            v_2 = val_list_1[k_4 + 1]
            r_2 = v_2 - v_1
            s = (r_2/(r_1+1))
            v_3 = v_1 + s
            my_dict_2[k] = v_3
            list_5 = list(my_dict_2.keys())
            list_6 = list(my_dict_2.values())
            raj_list = list(sorted(list_5, key=m.index))
            my_dict_3 = {}
            for i in raj_list:
                p_1 = my_dict_2.get(i)
                my_dict_3[i] = p_1
            key_list_1 = list(my_dict_3.keys())
            val_list_1 = list(my_dict_3.values())
print(my_dict_3)
