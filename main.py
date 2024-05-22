goal = 12
possible_numbers = [1, 2]

mul_lookup = {}
paths = []

for a in possible_numbers:
    for b in possible_numbers:
        c = a * b
        if c not in mul_lookup:
            mul_lookup[c] = [a, b]
print(mul_lookup)


class Add(a, b):
    def __init__(self):
        self.a = a
        self.b = b
        self.result = a + b
        self.path = [a, b]
        if self.result not in mul_lookup:
            mul_lookup[self.result] = self.path
        else:
            mul_lookup[self.result].append(self.path)
        print(mul_lookup)


def find_path():
    if goal in mul_lookup:
        paths.append(mul_lookup[goal])
        return paths
    else:
        for a in possible_numbers:
            for b in possible_numbers:
                c = a * b
                if c in mul_lookup:
                    paths.append(mul_lookup[c])
                    return paths


f = find_path()
print(f)
