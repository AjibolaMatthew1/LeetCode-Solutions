class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer = 0

        for roman in s:
            integer += roman_dict[roman]

        if "IV" in s:
            integer -= 2
        if "IX" in s:
            integer -= 2
        if "XL" in s:
            integer -= 20
        if "XC" in s:
            integer -= 20
        if "CD" in s:
            integer -= 200
        if "CM" in s:
            integer -= 200

        return integer 
