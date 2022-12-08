class sol:
    def RomtoInt(self, s):
        x = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        y = 0
        for i in range(len(s)):
            if i > 0 and x[s[i]] > x[s[i - 1]]:
                y += x[s[i]] - 2 * x[s[i - 1]]
            else:
                y += x[s[i]]
        return y
print(sol().RomtoInt('ML'))