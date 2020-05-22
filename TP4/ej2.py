#!/bin/python3

from hopfield import HopfieldNetwork
import numpy as np



a = np.asarray([
    [ -1, -1, 1, -1, -1  ],
    [ -1, 1, -1, 1, -1  ],
    [ -1, 1, 1, 1, -1  ],
    [ -1, 1, -1, 1, -1  ],
    [ -1, 1, -1, 1, -1  ]
    ]).reshape(1, 25)
b = np.asarray([
    [ -1, 1, 1, 1, -1  ],
    [ -1, 1, -1, 1, -1  ],
    [ -1, 1, 1, 1, -1  ],
    [ -1, 1, -1, 1, -1  ],
    [ -1, 1, 1, 1, -1  ]
    ]).reshape(1, 25)
b = np.asarray([
    [ -1, 1, 1, 1, -1  ],
    [ -1, 1, -1, 1, -1  ],
    [ -1, 1, 1, 1, -1  ],
    [ -1, 1, -1, 1, -1  ],
    [ -1, 1, 1, 1, -1  ]
    ]).reshape(1, 25)

bje = np.asarray([
    [ -1, 1, -1, -1, -1  ],
    [ -1, 1, -1, -1, -1  ],
    [ -1, 1, 1, 1, -1  ],
    [ -1, 1, -1, 1, -1  ],
    [ -1, 1, 1, 1, -1  ]
    ]).reshape(1, 25)

hn = HopfieldNetwork()
hn.store(np.asarray([a, b]))
result = hn.recognize(bje)
print(result.reshape(5, 5))