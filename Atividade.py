N = int(input()) 
R = int(input())  
P = int(input())  

total = N
novos = N
dias = 0

while total < P:
    dias += 1
    novos = novos * R
    total = total + novos

print(dias)
