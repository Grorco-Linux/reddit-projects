

def pascalmaker(x):

    pascallist = [[1],[1,1]]

    for row in range(x+1):
        if row > 2:
            pascallist.append([1,1])

            for pos in range(1,row-1):
                temp = pascallist[row-2][pos-1]+pascallist[row-2][pos]
                pascallist[row-1].insert(pos,temp)

    for row in range(len(pascallist)):
        for col in range(len(pascallist[row])):
            if row != len(pascallist):
                if col == 0:
                    print(''.zfill(len(pascallist[-1])-row).replace('0', ' ')+str(pascallist[row][col]),end=' ')
                else:
                    print(str(pascallist[row][col]), end=' ')
        print('')

x = input('enter the number of rows you want to show for the triangle: ')

pascalmaker(int(x))
