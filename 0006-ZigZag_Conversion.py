# Think of the rows as floors in a building and a pointer as an elevator.
# Instead of plotting a complex 2D grid full of blank spaces, simply create an array of empty strings, one for each floor. 
# As you read the input word letter by letter, drop the letter into the current floor's string and move the elevator. 
# The only rule is the "bounce": whenever the elevator hits the top floor (row == 0) or the absolute bottom floor (row == numRows - 1), 
# it instantly reverses direction.


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows

        currentRow = 0
        direction = 1

        for char in s:

            rows[currentRow] += char

            if currentRow == 0:
                direction = 1
            elif currentRow == numRows - 1:
                direction = -1

            currentRow += direction

        return "".join(rows)
