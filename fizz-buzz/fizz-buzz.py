class Solution:
    def fizzBuzz(self, number: int) -> List[str]:
        strings_count = []
        for i in range(1, number+1):
            if i % 15 == 0:
                strings_count.append("FizzBuzz")
            elif i % 3 == 0:
                strings_count.append("Fizz")
            elif i % 5 == 0:
                strings_count.append("Buzz")
            else:
                strings_count.append(str(i))
        return strings_count