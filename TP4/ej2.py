#!/bin/python3

from hopfield import HopfieldNetwork
import numpy as np
import letterUtils as lu

O = -1
I = 1

patterns = np.asarray([
    [-1, 1, 1, 1]
])

hn1 = HopfieldNetwork()
hn1.store(patterns)
res, hist = hn1.recognize([1, -1, -1, -1])
res1, hist1 = hn1.recognize(np.asmatrix([1, -1, -1, -1]))
res2, hist2 = hn1.recognize([-1, -1, -1, -1])

print(res)
print(res1)
print(res2)

letters = np.asarray(
[
np.asarray([
    [ O, O, I, O, O  ],
    [ O, I, O, I, O  ],
    [ I, O, O, O, I  ],
    [ I, I, I, I, I  ],
    [ I, O, O, O, I  ]]).reshape(I, 25),
np.asarray([
    [ I, I, I, I, O  ],
    [ I, O, O, O, I  ],
    [ I, I, I, I, O  ],
    [ I, O, O, O, I  ],
    [ I, I, I, I, O  ]]).reshape(I, 25),
 np.asarray([
    [ I, I, I, I, I  ],
    [ I, O, O, O, O  ],
    [ I, O, O, O, O  ],
    [ I, O, O, O, O  ],
    [ I, I, I, I, I  ]]).reshape(I, 25),
 np.asarray([
    [ I, I, I, I, O  ],
    [ I, O, O, O, I  ],
    [ I, O, O, O, I  ],
    [ I, O, O, O, I  ],
    [ I, I, I, I, O  ]]).reshape(I, 25),
 np.asarray([
    [ I, I, I, I, I  ],
    [ I, O, O, O, O  ],
    [ I, I, I, O, O  ],
    [ I, O, O, O, O  ],
    [ I, I, I, I, I  ]]).reshape(I, 25),
 np.asarray([
    [ O, I, I, I, O  ],
    [ O, I, O, O, O  ],
    [ O, I, I, O, O  ],
    [ O, I, O, O, O  ],
    [ O, I, O, O, O  ]]).reshape(I, 25),
 np.asarray([
    [ O, I, I, I, O  ],
    [ O, I, O, O, O  ],
    [ O, I, O, I, O  ],
    [ O, I, O, I, O  ],
    [ O, I, I, I, O  ]]).reshape(I, 25),
    np.asarray([
    [ O, I, O, I, O  ],
    [ O, I, O, I, O  ],
    [ O, I, I, I, O  ],
    [ O, I, O, I, O  ],
    [ O, I, O, I, O  ]]).reshape(I, 25),
np.asarray([
    [ O, I, I, I, O  ],
    [ O, O, I, O, O  ],
    [ O, O, I, O, O  ],
    [ O, O, I, O, O  ],
    [ O, I, I, I, O  ]]).reshape(I, 25)
]
)

pickedLetters = letters[:3]
hn = HopfieldNetwork()
hn.store(pickedLetters)

slightlyNoisyLetters = [lu.addNoiseEverywhere(x, .1) for x in pickedLetters]

# lu.printLetter(pickedLetters[0].reshape(5, 5), 1)
# lu.printLetter(slightlyNoisyLetters[0].reshape(5, 5), 1)

print('\n\nPicked Letters\n\n')
lu.printLetters(pickedLetters)
print('\n#########################\\nSlightly Noisy Letters\n#########################\\n')
lu.printLetters(slightlyNoisyLetters)

def iterate(letters):

    for l in letters:
        print('************About to recognize letter: *********** ')
        lu.printLetter(l.reshape(5, 5), 1)
        print('**************************************************')
        res, history = hn.recognize(l)
        lu.printLetters(history, shape=(5, 5))
        lu.printLetter(res.reshape(5, 5), 1)

iterate(slightlyNoisyLetters)

reallyNoisyLetters = [lu.addNoiseEverywhere(x, .45) for x in pickedLetters]

print('\n#########################\nReally Noisy Letters\n#########################\n')
lu.printLetters(reallyNoisyLetters[:1])
iterate(reallyNoisyLetters[:1])