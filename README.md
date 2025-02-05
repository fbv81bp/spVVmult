# spVVmult
A sparse vector-vector multiplication, that was aimed at lowering the number of comparisons between the compressed sparse indexes of two vectors, for power consumption's sake. What I found, is that it still takes roughly M+N comparisons, as I should have expected, but those are single bit comparisons, very effective, low power and fast in hardware. While the data format that it uses also may enable a 50% further compression of the respective vectors altogether!

## How it works
I really strongly suggest to inspect my code, but generally speaking it converts the index values' bits startig from MSB, moving towards LSBs into two unbalanced trees, where the first levels branch between vector indexes having a 0 versus 1 in their MSBs, and then so forth. Then the comparison and search for matching indexes happens by traversing the trees of both vectors simultaneously, and branching only in such directions, that both trees take. Essentially it is a kind of sub graph isomorphism between the two trees.

## Sub graph isomorphism
Aaand sub graph isomorphism is very interesting, because it is a very generic pattern matching, and so, I may have proven, that all, even this very abstarct mathematical operation - namely vector product - based AI systems constitute of a huge magnitude of delicately assembled sub graph isomorphism searches!

And to me that counts. ;)
