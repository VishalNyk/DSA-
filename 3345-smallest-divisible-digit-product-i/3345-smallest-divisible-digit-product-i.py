class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def get_digit_product(num: int) -> int:
            prd = 1
            while num > 0:
                prd *= num % 10
                num //= 10
            return prd

        # Start checking from n onwards
        while True:
            if get_digit_product(n) % t == 0:
                return n
            n += 1
