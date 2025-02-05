from random import randint as rdi

power = 17   # about 100k wide vectors
match = 500    # only two matching indexes between most vectors
total = 1000 # non-zero dimensions

matching = [97] + [rdi(0, 2**power-1) for i in range(match)]
non_matching_rise = []

def create_vec(v_skip):
    non_matching = []
    while len(non_matching) < total - match:
        r = rdi(0, 2**power-1)
        if r not in v_skip:
            non_matching.append(r)
    return matching + non_matching
    
v_rise = create_vec(matching)
v_fall = create_vec(v_rise)

v_rise.sort()
v_fall.sort()

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
        for pos in range(power -1, -1, - 1):
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

tree = [None, None]
tree_rise = treez(tree, v_rise)

tree = [None, None]
tree_fall = treez(tree, v_fall)

#print(tree_rise)
#print(v_rise)
#print(tree_fall)
#print(v_fall)

'''
simultaneous breadth first search: traverses only overlapping branches
of both trees

it is kind of a sub graph isomoprhism search between the two trees, and
expected is, that only the equal indexes of the both vectors will be
represented by the common tree portion, yet also all of those are going
to be included
'''
def simBFS(tree0, tree1, count):
    ptr0 = tree0
    ptr1 = tree1
    if (type(ptr0) is int) or (type(ptr1) is int): # should be 'AND' actually
        print(ptr0, ptr1)
    else:
        if ((ptr0[0] != None) and (ptr1[0] != None)):
            next_ptr0 = ptr0[0]
            next_ptr1 = ptr1[0]
            count = simBFS(next_ptr0, next_ptr1, count)
        if ((ptr0[1] != None) and (ptr1[1] != None)):
            next_ptr0 = ptr0[1]
            next_ptr1 = ptr1[1]
            count = simBFS(next_ptr0, next_ptr1, count)
    return count + 1

print('count', simBFS(tree_rise, tree_fall, 0))

