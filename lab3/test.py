# S = input("enter string:")
# K = int(input("enter key:"))

S = "Peppa Pig"
K = 3

def generate_cipher(S, K):
    S = list(S)  
    C = []  
    index = 0

    #_ABC = ["A","B","C","D","E","F","G","H","I","J","K","M","N","L","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    _abc = ("a","b","c","d","e","f","g","h","i","j","k","m","n","l","o","p","q","r","s","t","u","v","w","x","y","z")
    
    while S:
        X = (index + K - 1) % len(S)
        if S[X] in _abc:
            C.append(S.pop(X-1))
        else:
            C.append(S.pop(X))

        
    return ''.join(C)

result = generate_cipher(S, K)
print(result)


