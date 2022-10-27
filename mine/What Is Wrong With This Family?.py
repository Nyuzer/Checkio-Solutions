# https://py.checkio.org/en/mission/wrong-family/

def is_family(tree):

    tree.sort()
    # son check, every one can be son just 1 time
    son = []
    for f_s in tree:
        son.append(f_s[1])
    if len(son) != len(set(son)):
        return False
    # daddy check, every one should be daddy or have a daddy
    family = tree[0]
    tree = tree[1:]
    loop = 0
    while True:
        if loop > len(tree) or len(tree)==0:
            break
        if tree[0][0] in family and tree[0][1] not in family:
            family.append(tree[0][1])
            tree = tree[1:]
            loop = 0
        elif tree[0][1] in family and tree[0][0] not in family:
            family.append(tree[0][0])
            tree = tree[1:]
            loop = 0
        else:
            tree.append(tree[0])
            tree = tree[1:]
            loop += 1
    return not len(tree)


