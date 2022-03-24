import operator
import unittest
from dejavu import containers


class WarehouseTests(unittest.TestCase):
    
    def test_builtin_types(self):
        # ints
        avail, rem = containers.warehouse([1,2,3])
        self.assertEqual([avail.next() for x in xrange(5)], [1,2,3,0,0])
        
        avail, rem = containers.warehouse([1,2,3])
        self.assertEqual([avail.next() for x in xrange(2)], [1,2])
        self.assertEqual([x for x in rem], [3])
        
        # strings
        avail, rem = containers.warehouse(['fish', 'bananas', 'old pyjamas'])
        self.assertEqual([avail.next() for x in xrange(5)], ['fish', 'bananas', 'old pyjamas', '', ''])
        
        avail, rem = containers.warehouse(['fish', 'bananas', 'old pyjamas'])
        self.assertEqual([avail.next() for x in xrange(2)], ['fish', 'bananas'])
        self.assertEqual([x for x in rem], ['old pyjamas'])
        
        # Empty seq
        avail, rem = containers.warehouse([])
        self.assertRaises(ValueError, avail.next)
    
    def test_custom_classes(self):
        class Thing:
            def __init__(self, value=None):
                self.value = value
        
        things = Thing(1), Thing(2), Thing(3), Thing(4)
        avail, rem = containers.warehouse(things)
        self.assertEqual([avail.next().value for x in xrange(5)],
                         [1, 2, 3, 4, None])
        
        avail, rem = containers.warehouse(things)
        self.assertEqual([avail.next().value for x in xrange(2)], [1, 2])
        self.assertEqual([x for x in rem], [things[2], things[3]])
        
        # Empty seq
        avail, rem = containers.warehouse([], Thing)
        self.assertEqual([avail.next().value for x in xrange(2)], [None, None])
        self.assertEqual([x for x in rem], [])


class GraphTests(unittest.TestCase):
    
    def test_creation(self):
        g = containers.Graph()
        self.assertEqual(g, {})
        
        g = containers.Graph({'a': []})
        self.assertEqual(g, {'a': []})
        
        g = containers.Graph({'a': []}, True)
        self.assertEqual(g, {'a': []})
    
    def test_connect(self):
        g = containers.Graph()
        g.connect('A', 'B')
        self.assertEqual(g, {'A': ['B'],
                             'B': ['A'],
                             })
        g.connect('C', ('A', 'B'))
        self.assertEqual(g, {'A': ['B', 'C'],
                             'B': ['A', 'C'],
                             'C': ['A', 'B'],
                             })
    
    def test_chain(self):
        # Form the undirected graph:
        #   A--B--C--D
        #   |  |\   /
        #   |  | \ /
        #   E--F--G
        g = containers.Graph()
        g.chain('A', 'B', 'C', 'D', 'G', 'F', 'E', 'A')
        g.chain('B', 'F', 'G', 'B')
        self.assertEqual(g, {'A': ['B', 'E'],
                             'B': ['A', 'C', 'F', 'G'],
                             'C': ['B', 'D'],
                             'D': ['C', 'G'],
                             'E': ['F', 'A'],
                             'F': ['G', 'E', 'B'],
                             'G': ['D', 'F', 'B'],
                             })
        
        # Form the directed graph:
        #   A-->B->C->D
        #   |   |     |
        #   +>E-+->F--+->G
        g = containers.Graph(directed=True)
        g.chain('A', 'B', 'C', 'D', 'G')
        g.chain('A', 'E', 'F', 'G')
        g.chain('B', 'F')
        self.assertEqual(g, {'A': ['B', 'E'],
                             'B': ['C', 'F'],
                             'C': ['D'],
                             'D': ['G'],
                             'E': ['F'],
                             'F': ['G'],
                             })
    
    def test_shortest_path(self):
        # Form the graph:
        #   A--B--C--D
        #   |  |\   /
        #   |  | \ /
        #   E--F--G
        g = containers.Graph()
        g.connect('A', ('B', 'E'))
        g.connect('B', ('C', 'F', 'G'))
        g.connect('D', ('C', 'G'))
        g.connect('E', 'F')
        g.connect('F', 'G')
        
        self.assertEqual(g.shortest_path('A', 'D'), ['A', 'B', 'C', 'D'])
        self.assertEqual(g.shortest_path('B', 'A'), ['B', 'A'])
        self.assertEqual(g.shortest_path('E', 'C'), ['E', 'A', 'B', 'C'])
        self.assertEqual(g.shortest_path('A', 'G'), ['A', 'B', 'G'])
        
        # Do the same test again to see if caching works.
        self.assertEqual(g.shortest_path('A', 'D'), ['A', 'B', 'C', 'D'])
        self.assertEqual(g.shortest_path('B', 'A'), ['B', 'A'])
        self.assertEqual(g.shortest_path('E', 'C'), ['E', 'A', 'B', 'C'])
        self.assertEqual(g.shortest_path('A', 'G'), ['A', 'B', 'G'])
        
        # Test invalid paths.
        self.assertRaises(KeyError, g.shortest_path, 'R', 'D')
        self.assertEqual(g.shortest_path('D', 'R'), None)
    
    def test_shortest_path_directed(self):
        # Form the graph:
        #   A-->B->C->D
        #   |   |     |
        #   +>E-+->F--+->G
        g = containers.Graph(directed=True)
        g.connect('A', ('B', 'E'))
        g.connect('B', ('C', 'F'))
        g.connect('C', 'D')
        g.connect('D', 'G')
        g.connect('E', 'F')
        g.connect('F', 'G')
        
        self.assertEqual(g, {'A': ['B', 'E'],
                             'B': ['C', 'F'],
                             'C': ['D'],
                             'D': ['G'],
                             'E': ['F'],
                             'F': ['G'],
                             })
        
        self.assertEqual(g.shortest_path('A', 'D'), ['A', 'B', 'C', 'D'])
        self.assertEqual(g.shortest_path('B', 'A'), None)
        self.assertEqual(g.shortest_path('E', 'C'), None)
        self.assertEqual(g.shortest_path('A', 'G'), ['A', 'B', 'F', 'G'])


if __name__ == "__main__":
    unittest.main(__name__)

