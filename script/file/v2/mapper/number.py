import re

def createNbr(nbr):
    # With '/' Mark E.g/ Vv116/156/186
    if '/' in nbr:
        split = re.split('([a-zA-Z]+)', nbr)
        head = split[1]
        remain = split[2]
        nums = re.split('\/', remain)
        nbrs = list(map(lambda ele: ''.join((head, ele)), nums))
        nbrs = '/'.join(nbrs)
    else:
        nbrs = nbr
    return nbrs
