# Sparse Vector-Vector multiplication
A sparse vector-vector multiplication, that was aimed at lowering the number of comparisons between the compressed sparse indexes of two vectors, for power consumption's sake. What I found, is that it still takes roughly M+N comparisons, as I should have expected, but those are single bit comparisons, very effective, low power and fast in hardware.

Originally I decided to improve the comparison count or at least energy efficiency, because some of the newest AI LLM models have only 1 to 4 bits of data per non-zero dimension, after model compression, in their embedding vectors. In which case the multiplication of vector elements transforms into a simple, cheap table lookup. With that, at the same time, merging the sparse vectors' index lists may become the actual bottleneck...

## How it works
I really strongly suggest to inspect my code, but generally speaking it converts the index values' bits startig from MSB, moving towards LSBs into two unbalanced trees, where the first levels branch between vector indexes having a 0 versus 1 in their MSBs, and then so forth. Then the comparison and search for matching indexes happens by traversing the trees of both vectors simultaneously, and branching only in such directions, that both trees take. Essentially it is a kind of sub graph isomorphism between the two trees.

## Sub graph isomorphism
Aaand sub graph isomorphism is very interesting, because it is a very generic pattern matching, and so, I may have proven, that all, even this very abstarct mathematical operation - namely vector product - based AI systems constitute of a huge magnitude of delicately assembled sub graph isomorphism searches!

And to me that counts. ;)
