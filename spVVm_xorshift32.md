## Interpretation

With xorshift32's randomization I get two well fairly balanced hash tries, whose simultaneous traversal doesn't
require signifacntly more steps to match. The surplus comes from the tries having 32 layers instead of the minimal
bit width needed to represent all vector dimensions. So O(M+N) comparisons aka. branchings are the minimal needed,
while in addition the traversal has to reach the last layer for every valid pair. Meanwhile the hash-like randomness
cancels out wrong branches very early.

So interestingly a much more capable dimension indexing ie. 32 bits for 4096 dimensions instead of just 12 still
don't require way more computation than the number of non-zero indexes summed.

### Dump

* call count: 4301
* matches: 19
* pairs: [[0, 0], [26, 16], [132, 127], [339, 339], [497, 560], [558, 623], [566, 630], [888, 945], [927, 987], [1064, 1108], [1113, 1153], [1167, 1212], [1267, 1319], [1361, 1410], [1475, 1501], [1581, 1591], [1785, 1781], [1846, 1844], [1857, 1854]]
* test: True
* call count: 4108
* matches: 9
* pairs: [[0, 0], [315, 321], [566, 570], [904, 883], [1116, 1100], [1226, 1206], [1714, 1676], [1798, 1761], [1847, 1844]]
* test: True
* call count: 4331
* matches: 20
* pairs: [[1, 0], [46, 57], [99, 118], [142, 156], [295, 324], [564, 619], [743, 760], [771, 788], [784, 803], [824, 850], [1113, 1129], [1224, 1248], [1275, 1296], [1306, 1326], [1394, 1411], [1469, 1465], [1529, 1525], [1725, 1730], [1772, 1774], [1927, 1908]]
* test: True
* call count: 4109
* matches: 11
* pairs: [[0, 0], [194, 188], [408, 364], [886, 819], [1039, 980], [1054, 995], [1086, 1024], [1256, 1194], [1342, 1299], [1426, 1373], [1878, 1850]]
* test: True
* call count: 4201
* matches: 12
* pairs: [[0, 0], [481, 481], [675, 699], [800, 834], [877, 912], [1047, 1040], [1098, 1080], [1165, 1141], [1192, 1163], [1199, 1167], [1244, 1203], [1268, 1232]]
* test: True
* call count: 4279
* matches: 18
* pairs: [[0, 0], [140, 108], [293, 254], [362, 320], [557, 531], [581, 561], [591, 573], [783, 750], [1058, 1050], [1079, 1076], [1245, 1244], [1435, 1472], [1534, 1572], [1615, 1655], [1623, 1659], [1625, 1660], [1733, 1757], [1975, 1977]]
* test: True
* call count: 4387
* matches: 18
* pairs: [[0, 0], [85, 76], [261, 303], [308, 340], [473, 502], [495, 524], [521, 547], [541, 565], [608, 631], [824, 843], [1086, 1098], [1174, 1195], [1270, 1295], [1277, 1304], [1540, 1552], [1737, 1751], [1867, 1856], [1980, 1979]]
* test: True
* call count: 4421
* matches: 17
* pairs: [[0, 0], [625, 627], [647, 651], [663, 681], [831, 875], [882, 917], [1011, 1044], [1014, 1045], [1039, 1066], [1100, 1119], [1234, 1259], [1465, 1479], [1479, 1491], [1860, 1850], [1910, 1913], [1913, 1922], [1938, 1951]]
* test: True
* call count: 4193
* matches: 15
* pairs: [[0, 0], [229, 284], [247, 299], [445, 521], [592, 661], [598, 665], [607, 676], [815, 867], [1005, 1056], [1083, 1128], [1225, 1262], [1414, 1432], [1645, 1679], [1657, 1690], [1783, 1802]]
* test: True
* call count: 4275
* matches: 14
* pairs: [[0, 0], [10, 11], [249, 274], [276, 300], [351, 387], [452, 515], [649, 672], [758, 784], [765, 790], [1210, 1230], [1300, 1314], [1460, 1465], [1526, 1531], [1830, 1850]]
* test: True
* call count: 4205
* matches: 15
* pairs: [[1, 0], [154, 141], [248, 251], [314, 313], [383, 375], [1003, 983], [1056, 1040], [1078, 1067], [1175, 1156], [1245, 1218], [1278, 1259], [1566, 1553], [1645, 1629], [1699, 1683], [1727, 1701]]
* test: True
* call count: 4175
* matches: 12
* pairs: [[0, 0], [726, 705], [752, 731], [787, 768], [812, 795], [997, 983], [1006, 994], [1205, 1217], [1410, 1402], [1692, 1663], [1832, 1796], [1848, 1811]]
* test: True
