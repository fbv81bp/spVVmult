from random import randint as rdi

''' parameters '''
power = 18
vsize = 2**power
total = 1999
match_count = 80
hash_width = 12
''' end of parameters '''

def xxx(state): # "xorshift12"
	x = state
	x ^= (x << 13)
	x ^= (x >> 17)
	x ^= (x << 5)
	return (x + (x >> 16)) & (2**hash_width - 1) # a bit more of randomization 

def create_vec(avoid):
    v = []
    while len(v) < total:
        r = xxx(rdi(0,vsize))
        if r not in avoid:
            if r not in v:
                v.append(r)
    return v
    
def get_bit(num, i):
    return (num >> i) & 1

'''
a tree leaf has 2 directions, left and right, which
can have 2 values: None or [None, None] depending on if there
is anything left to search in that particular direction

tree leaf values are initialized to None, and the tree is
traversed according to individual bits of the sparse vectors'
indexes' bits: 0 branching left, and 1 branching right

only such leafs are initialized with the value True, that
were formerly traversed due to an existing index's upcoming bits
'''
def treez(tree, vec):
    tr2e = list(tree)
    num_idx = 0
    # loop through index values
    for num in vec:
        # retart at the beginning of the tree with every number
        tree_ptr = tr2e
        # loop though value's bits from MSB to LSB
        for pos in range(hash_width -1, -1, - 1):
            bit = get_bit(num, pos)
            # if there was no prior traversal...
            if tree_ptr[bit] == None:
                if (pos > 0):
                    # ...create one
                    tree_ptr[bit] = [None, None]
                else:
                    # or post the index value's position at the
                    # end of the traversal
                    tree_ptr[bit] = num_idx
            # set the traversal pointer to the next leaf
            tree_ptr = tree_ptr[bit]
        num_idx += 1
    return tr2e

'''
simultaneous breadth first search: traverses only overlapping branches
of both trees

it is kind of a sub graph isomoprhism search between the two trees, and
expected is, that only the equal indexes of the both vectors will be
represented by the common tree portion, yet also all of those are going
to be included
'''
def simBFS(tree0, tree1, count, lista):
    ptr0 = tree0
    ptr1 = tree1
    if (type(ptr0) is int) or (type(ptr1) is int): # should be 'AND' actually
        lista.append([ptr0, ptr1])
        return count + 1, lista
    else:
        if ((ptr0[0] != None) and (ptr1[0] != None)):
            next_ptr0 = ptr0[0]
            next_ptr1 = ptr1[0]
            count, lista = simBFS(next_ptr0, next_ptr1, count + 1, lista)
        if ((ptr0[1] != None) and (ptr1[1] != None)):
            next_ptr0 = ptr0[1]
            next_ptr1 = ptr1[1]
            count, lista = simBFS(next_ptr0, next_ptr1, count + 1, lista)
    return count, lista

call_count = 0
test_runs = 12
for _ in range(test_runs): # averaging

    common = [17*i + 23 for i in range(match_count)] # easy to test format for matching indexes
    v_rise = common + create_vec([])
    v_fall = common + create_vec(v_rise)

    v_rise.sort()
    v_fall.sort()

    tree = [None, None]
    tree_rise = treez(tree, v_rise)

    tree = [None, None]
    tree_fall = treez(tree, v_fall)

    #print(tree_rise)
    #print(v_rise)
    #print(tree_fall)
    #print(v_fall)

    count, lista = simBFS(tree_rise, tree_fall, 0, [])
    print('### next run')
    print('* call count:', count)
    print('* match count passed:', len(lista) == match_count) # chacking the number of matching indexes
    #print('* pairs:', lista)
    flag = True
    for i in range(len(lista)):
        if (v_rise[lista[i][0]] != v_fall[lista[i][1]]): # checking if all claimed indexes match
            flag = False
        elif ((v_rise[lista[i][0]] - 23) % 17 > 0): # testing if indexes fit their format
            flag = False
    print('* matching values passed:', flag)
    call_count += count

print('### listA length:', len(v_rise))    
print('### listB length:', len(v_fall))    
print('### average recursion decision count:', call_count / test_runs)
print()
