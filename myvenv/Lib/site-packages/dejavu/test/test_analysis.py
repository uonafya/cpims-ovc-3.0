import datetime
import unittest

from dejavu import analysis


class Thing(object):
    def __init__(self, color, size, date):
        self.color = color
        self.size = size
        self.date = date

things = []
for color, year in [('red', 2004), ('yellow', 2003),
                    ('blue', 2002), ('green', 2001)]:
    d = datetime.date(year, 1, 1)
    for size in xrange(5):
        things.append(Thing(color, size, d))


class CrossTabTests(unittest.TestCase):
    
    def test_creation(self):
        ctab = analysis.CrossTab()
        ctab = analysis.CrossTab(things)
    
    def test_count(self):
        ctab = analysis.CrossTab(things, 'color', 'size')
        self.assertEqual(ctab.results()[0],
                         {('blue',): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1},
                          ('yellow',): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1},
                          ('green',): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1},
                          ('red',): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}},
                         )
        ctab = analysis.CrossTab(things, ('color', lambda x: x.date.year), 'size')
        self.assertEqual(ctab.results()[0],
                         {('blue', 2002): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1},
                          ('yellow', 2003): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1},
                          ('green', 2001): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1},
                          ('red', 2004): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1}},
                         )
    
    def test_sum(self):
        ctab = analysis.CrossTab(things, (), 'size')
        self.assertEqual(ctab.results()[0], {(): {0: 4, 1: 4, 2: 4, 3: 4, 4: 4}})
        ctab.source[0].size = 4
        self.assertEqual(ctab.results()[0], {(): {0: 3, 1: 4, 2: 4, 3: 4, 4: 5}})
        ctab.groups = (lambda x: x.date.year,)
        self.assertEqual(ctab.results(),
                         ({(2001,): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1},
                           (2002,): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1},
                           (2003,): {0: 1, 1: 1, 2: 1, 3: 1, 4: 1},
                           (2004,): {      1: 1, 2: 1, 3: 1, 4: 2}},
                          [0, 1, 2, 3, 4])
                         )
        ctab.groups = ('size',)
        ctab.pivot = lambda x: x.date.year
        self.assertEqual(ctab.results(),
                         ({(0,): {2001: 1, 2002: 1, 2003: 1,        },
                           (1,): {2001: 1, 2002: 1, 2003: 1, 2004: 1},
                           (2,): {2001: 1, 2002: 1, 2003: 1, 2004: 1},
                           (3,): {2001: 1, 2002: 1, 2003: 1, 2004: 1},
                           (4,): {2001: 1, 2002: 1, 2003: 1, 2004: 2}},
                          [2001, 2002, 2003, 2004])
                         )


if __name__ == "__main__":
    unittest.main(__name__)

