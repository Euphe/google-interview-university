"""
https://stackoverflow.com/questions/44407768/reset-loop-at-value-variable

I'm probably doing this wrong, I started python very recently. 
I need to move the dict(value, mod) key that this loop is evaluating for, either up or down one number, every time it is evaluated. Then re-evaluate it for that new "value".
"""
points = 20
stat_dict = {0:5, 1:5, 2:4, 3:4, 4:3, 5:3, 6:2, 7:2, 8:1, 9:1, 10:1, 11:1, 12:1,
             13:2, 14:2, 15:3, 16:3, 17:4, 18:4, 19:5, 20:5, 21:6, 22:6}

def stat_sel(user):
    global points
    for values, mods in stat_dict.items():
        if user >= mods:
            remn_dr = user-mods
            #here I want to move to the right or left one space key in my dict()
            #and then terminate this loop
            points = points - user + remn_dr
            return points


        else:
             print("Can't")


x= int(input('> '))
stat_sel(x)
print(stat_dict)