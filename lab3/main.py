S = input("enter string:")
K = int(input("enter key:"))

def generate_cipher(S, K):
    S = list(S)  
    C = []  
    index = 0  
    
    while S:
        index = (index + K - 1) % len(S)
        C.append(S.pop(index)) 
        
    return ''.join(C)

result = generate_cipher(S, K)
print(result)