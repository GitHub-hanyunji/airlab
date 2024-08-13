#module.py
#16번

import random
def f(st,passlen):
    p="".join(random.sample(st,passlen))
    print(f"생성된 암호={p}")