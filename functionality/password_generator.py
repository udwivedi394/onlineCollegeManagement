import random

def auto_generate_password():
    temp_lst = []
    symbol_lst = ['@','#','$','<','%','&']
    
    temp_lst.append(chr(random.randrange(48, 58)))
    temp_lst.append(chr(random.randrange(65, 91)))
    temp_lst.append(chr(random.randrange(97, 123)))
    temp_lst.append(symbol_lst[random.randrange(0,6)])
    
    final_pwd = []
    #print(random.randrange(range(48,58), range(65,91)))
    reqd_range = list(range(48,58)) + list(range(65,91)) + list(range(97,123)) + [64,35,36,60,37,38]
    for i in range(random.randrange(8,12)-4):
        final_pwd.append(chr(reqd_range[random.randrange(len(reqd_range))]))
    
    for i in range(4):
        final_pwd.insert(random.randrange(len(final_pwd)), temp_lst[i])
    return "".join(final_pwd)
