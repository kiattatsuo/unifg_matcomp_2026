print("A B C | S")
print("---------")

for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:

            
            S = (C and not B) or (A and B)

            
            S = int(S)

            print(A, B, C, "|", S)