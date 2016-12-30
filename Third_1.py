def closest_mod_5(x):
    y=1
    while (y<int(x)) or (y%5!=0):
        y+=1
    return y