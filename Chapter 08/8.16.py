import making_shirts
making_shirts.make_shirt('s', 'Mortal kombat')
print()

from making_shirts import make_shirt
make_shirt('l', 'Mortal kombat')
print()

from making_shirts import make_shirt as ms
ms('xl', 'Mortal kombat')
print()

import making_shirts as make_s
make_s.make_shirt('xxl', 'Mortal kombat')
print()

from making_shirts import *
make_shirt('xxxxxxxxl', 'Mortal kombat')
