# https://leetcode.com/problems/reorder-data-in-log-files/
def reorderLogFiles():
    letters, digits = [], []
    logs = ['2 A', '1 B', '4 C', '1 A']

    logs.sort( key=lambda x: (x.split()[0], x.split()[1]) )
    print( logs )


reorderLogFiles()
