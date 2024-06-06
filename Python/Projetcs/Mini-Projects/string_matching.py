class String_Matching:

    def __init__(self, s1: str, s2: str):
        self.s1 = s1.lower()
        self.s2 = s2.lower()
        self.E = [[0 for _ in range(len(s1))] for _ in range(len(s2))]

    def match(self):
    
        def recursive(i, j):
            if (i < 0 or j < 0):
                return 0

            elif (i == 0) and (j != 0):
                self.E[j][i] = len(self.s2[0:j+1]) if (self.s1[0] not in self.s2[0:j+1]) else len(self.s2[0:j+1]) - 1

            elif (i != 0) and (j == 0):
                self.E[j][i] = len(self.s1[0:i+1]) if (self.s2[0] not in self.s1[0:i+1]) else len(self.s1[0:i+1]) - 1

            elif (i == 0) and (j == 0):
                self.E[j][i] = 1 if (self.s1[0] != self.s2[0]) else 0

            else:
                if (self.E[j][i] == 0):
                    if (self.s1[i] == self.s2[j]):
                        self.E[j][i] = min(1 + recursive(i-1, j), 1 + recursive(i, j-1), recursive(i-1, j-1))
                    else:
                        self.E[j][i] = min(1 + recursive(i-1, j), 1 + recursive(i, j-1), 1 + recursive(i-1, j-1))

            return self.E[j][i]
        
        recursive(len(self.s1) - 1, len(self.s2) - 1)

        return self.E[len(self.s2) - 1][len(self.s1) - 1]
    

def get_closest_to(word: str, dictionary: list):
    obj = String_Matching(word, dictionary[0])
    minimum = [dictionary[0], obj.match()]

    for w in dictionary[1:]:
        if minimum[1] == 0:
            break

        dif = String_Matching(word, w).match()
        if (minimum[1] > dif):
            minimum[0], minimum[1] = w, dif
    
    return minimum[0]
