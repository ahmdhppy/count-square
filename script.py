data = {
        (0, 0):{'l':(0, 1), 'b':(1, 0)},
        (0, 1):{'l':(0, 2), 'b':()},
        (0, 2):{'l':(0, 3), 'b':(1, 2)},
        (0, 3):{'l':(0, 4), 'b':()},
        (0, 4):{'l':(),     'b':(1, 4)},
        
        (1, 0):{'l':(),     'b':(2, 0)},
        (1, 1):{'l':(1, 2), 'b':(2, 1)},
        (1, 2):{'l':(1, 3), 'b':(2, 2)},
        (1, 3):{'l':(1, 4), 'b':(2, 3)},
        (1, 4):{'l':(),     'b':(2, 4)},
        
        (2, 0):{'l':(2,1), 'b':(3, 0)},
        (2, 1):{'l':(2, 2), 'b':()},
        (2, 2):{'l':(2, 3), 'b':(3, 2)},
        (2, 3):{'l':(2, 4), 'b':(3, 3)},
        (2, 4):{'l':(),     'b':(3, 4)},
        
        (3, 0):{'l':(3, 1), 'b':(4, 0)},
        (3, 1):{'l':(),     'b':(4, 1)},
        (3, 2):{'l':(3, 3), 'b':(4, 2)},
        (3, 3):{'l':(),     'b':()},
        (3, 4):{'l':(),     'b':(4, 4)},
        
        (4, 0):{'l':(4, 1), 'b':()},
        (4, 1):{'l':(4, 2), 'b':()},
        (4, 2):{'l':(4, 3), 'b':()},
        (4, 3):{'l':(4, 4), 'b':()},
        (4, 4):{'l':(),     'b':()},
        }

y = 5 #number of columns
x = 5 #number of row

count = 0
for xx in range(x):
    for yy in range(y):
        for i in range(1,min(x, y)- max(xx,yy)):
            sub_data_1 = (xx,yy)
            sub_data_2 =(xx,yy)
            is_square = True
            if not(sub_data_1 and sub_data_2):
                is_square = False
                break
            for j in range(i):
                sub_data_1 = data[sub_data_1]['l']
                sub_data_2 = data[sub_data_2]['b']
                if not(sub_data_1 and sub_data_2):
                    is_square = False
                    break
            if not is_square:
                break
            for j in range(i):
                sub_data_1 = data[sub_data_1]['b']
                sub_data_2 = data[sub_data_2]['l']
                if not(sub_data_1 and sub_data_2):
                    is_square = False
                    break
            if  is_square:
                count +=1
print(count) 
