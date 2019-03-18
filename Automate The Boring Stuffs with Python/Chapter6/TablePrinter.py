tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(tbdata):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        colWidths[i] = len(max(tableData[i],key = len))
    for r in range(len(tableData[0])):
        for c in range(len(tableData)):   
            print(tableData[c][r].rjust(colWidths[c]),end=" ")
        print('\n')

printTable(tableData)         


