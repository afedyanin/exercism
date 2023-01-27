class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        rowStrings = matrix_string.split('\n')
        for rowString in rowStrings:
            items = rowString.split(' ')
            row = []
            for item in items:
                row.append(int(item))
            self.rows.append(row)
    
    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        items = []
        for row in self.rows:
            items.append(row[index-1])
        return items
    