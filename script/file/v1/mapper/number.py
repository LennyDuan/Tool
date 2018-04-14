import re

def createNbr(nbr):
    # With '/' Mark E.g/ Vv116/156/186
    split = re.split('([a-zA-Z]+)', nbr)
    head = split[1]
    remain = split[2]
    nums = re.split('\/', remain)
    print(nums)
    print(head)
    nbrs = list(map(lambda ele: ''.join((head, ele)), nums))
    print(nbrs)

    return nbr
