# -*- coding: utf-8 -*-
"""Глеб Балчиди

   Тестовое задание для курса Junior BackEnd Dev

"""

class Solution:
  
  def __init__(self):
    s = self
    self.EXPLANATION_RULES =  (
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    )

  def roman_to_arabic(self, s: str) -> int:
    s = s.upper()
    ret = 0
    for arab, roman in self.EXPLANATION_RULES:
        while s.startswith(roman):
            ret += arab
            s = s[ len( roman ):]
    return ret

solution = Solution()
answer = solution.roman_to_arabic('IV')
print(answer)
