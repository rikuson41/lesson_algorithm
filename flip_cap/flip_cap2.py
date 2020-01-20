def pleaseConformOnepass(caps):
    caps = caps + [caps[0]]
    for i in  range(1, len(caps)):
        if caps[i] != caps[i -1]:
            if caps[i] != caps[0]:
                print('People in positions', i, end='')
            else:
                print(' through', i-1, 'flip your caps!')

cap1 = ['F', 'F', 'B', 'B', 'B', 'F', 'B', 'B', 'B', 'F', 'F', 'B', 'F']

pleaseConformOnepass(cap1)