from operator import truediv
def main():
    numberofingredient=long(input())
    createpowerpuff = list(map(long,raw_input().split()))
    Quantity = list(map(long,raw_input().split()))
    res = list(map(truediv, Quantity, createpowerpuff))
    print long(min(res))
