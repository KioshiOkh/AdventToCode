with open('inputRPS.in') as file:
    rounds = [i.replace(" ", "") for i in file.read().strip().split("\n")]
    
print(rounds)

#round 1 comb
# A - X = U  = (1 + 3) = 4
# A - Y = W = (2 + 6) = 8
# A - Z = L = (3 + 0) = 3
# B - X = L = (1 + 0) = 1
# B - Y = U = 2 + 3 = 5
# B - Z = W = 3 + 6 = 9
# C - X = W = 1 + 6 = 7
# C - Y = L = 2 + 0 = 2
# C - Z = U = 3 + 3 = 6

#Round 2  -> X LOSS | Y = DRAW | Z = WIN

outcome = {
    "AX":3, "AY":4, "AZ":8, "BX":1, "BY":5, "BZ":9, "CX":2, "CY":6, "CZ":7
}

score = 0
for round in rounds:
    score += outcome[round]
print("Total Score Round 2:", score)