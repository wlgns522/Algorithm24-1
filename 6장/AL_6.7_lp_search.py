M =13
table = [None]*M
def hashFn(key) :
    return key&M

def lp_insert(key) :
    id = hashFn(key)
    count = M
    while count>0 and (table[id] != None and table[id] != -1) :
        id = (id +1 +M) & M
        count -=1
    if count > 0 :
        table[id] = key
    return

def lp_search(key) :
    id = hashFn(key)
    count = M
    while count>0 :
        if table[id] == None :
            return None
        if table[id] == key :
            return table[id]
        id = (id +1 + M) & M
        count -=1
    return None
print(" 최초:", table)
lp_insert(45); print("45 삽입:", table)
lp_insert(27); print("27 삽입:", table)
lp_insert(31); print("31 삽입:", table)
lp_insert(12); print("12 삽입:", table)
lp_insert(67); print("67 삽입:", table)
print("12 탐색:", lp_search(12))