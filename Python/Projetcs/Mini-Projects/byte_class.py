"""
This example introduce us into the `binary` operators in Python. Those are:
1) Left-Shift
2) Rigth-Shift
3) Logical-AND
4) Logical-OR
5) Logical-XOR
6) Logical-NOT

We are going to `complete` the calss using the ability to change a specific bit.
"""

class Byte:
    def __init__(self, s = ""):
        if s == "":
            self.array = [0 for _ in range(8)]
        else:
            self.array = [int(c) for c in s]

    def __str__(self) -> str:
        return "".join([str(d) for d in self.array])
    
    def __lshift__(self, total):
        for _ in range(total):
            self.array.append(0)
            self.array.pop(0)

    def __rshift__(self, total):
        for _ in range(total):
            self.array.insert(0, 0)
            self.array.pop()

    def __and__(self, obj):
        new_byte = Byte("")

        for i in range(8):
            new_byte.array[i] = self.array[i] * obj.array[i]

        return new_byte
    
    def __or__(self, obj):
        new_byte = Byte("")

        for i in range(8):
            new_byte.array[i] = self.array[i] | obj.array[i]

        return new_byte
    
    def __xor__(self, obj):
        new_byte = Byte()

        for i in range(8):
            new_byte.array[i] = self.array[i] ^ obj.array[i]

        return new_byte
    
    def __invert__(self):
        new_obyte = Byte()

        for i in range(8):
            new_obyte.array[i] = 1 if (self.array[i] == 0) else 0
        
        return new_obyte
    
    def __len__(self):
        return len(self.array)
    
    def __getitem__(self, item):
        return self.array[item]
    
    def __setitem__(self, key, value):
        self.array[key] = value

    


b1 = Byte()
b2 = Byte("11010101")
b3 = Byte("10000011")

print(b1, b2, b3)

b2 << 2 # Performs left-shift
b2 >> 2 # Performs right-shift

print(b2 & b3) # Performs logical-and
print(b2 | b3) # Performs logical-or
print(b2 ^ b3) # Performs logical-xor
print(~b3)     # PErforms logical-not

b3[1] = 1

for bit in b3:
    print(bit, end='|')
print()
