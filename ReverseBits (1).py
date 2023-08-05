def reverse_binary(n):
    rbs = bin(n)[:1:-1]  
    return int(rbs, 2)  


