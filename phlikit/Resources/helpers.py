from random import random, randint

def generate_link_id(): 
    entropy = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','1','2','3','4','5','6','7','8']
    id = ''

    for i in range(7):
        num = randint(0, 25)
        id += entropy[num]

    return id
