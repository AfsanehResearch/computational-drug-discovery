def show_info(**kwargs):
    print(kwargs)
show_info(name = "caffeine", formula = "C8H10N4O2", charge = 0)
print( "====finished ===")

def show_info(**kwargs):
    for key, value in kwargs.item():
            print(key, "=", value)
show_info(name= "caffeine", formula = "C8H10N4O2", charge = 0)