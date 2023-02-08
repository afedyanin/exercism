def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    :param wagons_rows: list[list[tuple]] - the list of rows of wagons.
    :return: list[list[tuple]] - list of rows of wagons.
    """
    red_row, blue_row, orange_row = wagons_rows
    res = []
    for i,red_item in enumerate(red_row):
        res.append([red_item, blue_row[i], orange_row[i]])
    return res

items =  fix_wagon_depot([
                    [(2, "red"), (4, "red"), (8, "red")],
                    [(5, "blue"), (9, "blue"), (13,"blue")],
                    [(3, "orange"), (7, "orange"), (11, "orange")],
                    ])

print(items)
