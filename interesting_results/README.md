Hashing the otherwise anyway random numbers can only balance the hash trie structured unbalanced tree, and seemingly the algorithm finishes in around 75% of the O(N+M) comparisons, theoretically needed in a worst case two pointer solution.

Okay, I haven't tested for any corner cases. True. Any corner cases for hashed random values?

Awh... but I see now: I assumed perfect, ie. collisionless hashing! :/ So at best this might only showcase some theoretical minimum. Even in that case, it might be sub-tree-isomorphism that is the cheapest, simplest for matching sparse vectors indexes (?!). I mean maybe it isn't just a more complex way of solving sth that can be solved simpler... but the other way around.

Yet again! Perfect "hashing" might just be possible, since we are talking about vector indexes, that are strictly growing numbers as such. Perhaps like simply taking the upper third number of bits starting with MSB, stretching each bit to two, and then adding that number to the lower two thirds of the index. This way compressing 18 bits to 12 bits so, that all 12 bit numbers should be different - at fitst thought...
