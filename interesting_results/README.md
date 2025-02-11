Hashing the otherwise anyway random numbers can only balance the hash trie structured unbalanced tree, and seemingly the algorithm finishes in around 75% of the O(N+M) comparisons, theoretically needed in a worst case two pointer solution.

Okay, I haven't tested for any corner cases. True. Any corner cases for hashed random values?

Awh... but I see now: I assumed perfect, ie. collisionless hashing! :/ So at best this might only showcase some theoretical minimum. Even in that case, it might be sub-tree-isomorphism that is the cheapest, simplest for matching sparse vectors indexes (?!). I mean maybe it isn't just a more complex way of solving sth that can be solved simpler... but the other way around.
