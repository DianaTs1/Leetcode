class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        column = ["a", "b", "c", "d", "e", "f", "g", "h"]
        row = [1, 2, 3, 4, 5, 6, 7, 8]
        
        column_index = column.index(coordinates[0])
        row_index = row.index(int(coordinates[1]))        
        
        if (column_index == 0 and row_index == 0):
            return False
        elif (column_index % 2 == 0 and row_index % 2 == 0):
            return False
        elif (column_index % 2 == 1 and row_index % 2 == 1):
            return False
        else:
            return True