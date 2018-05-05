# Because photoshop is silly.

import os
default_name = "default_"
files = [f for f in os.listdir(".") if f.endswith(".png")]

for f in files:
    letter = f[-5]
    case = "U" if letter.isupper() else "L"
    print(letter, case)
    shortened = default_name + case + f[-5:]
    print("{}:> {}".format(f, shortened))
    #os.rename(f, shortened)
