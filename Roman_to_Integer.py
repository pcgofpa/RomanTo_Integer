# Given a roman numeral convert to the integer it represents.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
s = "III"

class Solution:
    def romanToInt(s:str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        romanInt = 0
        
        for n in range(len(s)-1):
            if roman[s[n]] < roman[s[(n+1)]]:
                romanInt -= roman[s[n]]
            else:
                romanInt += roman[s[n]]
        return romanInt + roman[s[-1]]
    
    print(romanToInt(s = "III"))
    print(romanToInt(s = "LVIII"))
    print(romanToInt(s = "MCMXCIV"))
    print(romanToInt(s = "MMXXIII"))
Solution()