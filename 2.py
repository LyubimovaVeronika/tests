
def createDict(k, v):
    res = {}
    if (type(k) != list):
        raise Exception('First_Argument_Not_List_Exception')
    if (type(v) != list):
        raise Exception('Second_Argument_Not_List_Exception')

    for i in range(len(k)):
        try:
            res.update({k[i]: v[i]})
        except IndexError:
            res.update({k[i]: None})
    return res

if __name__ == '__main__':
    import unittest

    a = ['key1', 'key2', 'key3', 'key4']
    b = [1, 2, 3]

    c = ['key5', 'key6', 'key7']
    d = ['a', 'b', 'c']

    class Tests(unittest.TestCase):

        def test_normal_values(self):
            self.assertEqual(createDict(a,b), {'key1': 1, 'key2': 2, 'key3': 3, 'key4': None})
            self.assertEqual(createDict(c,d), {'key5': 'a', 'key6': 'b', 'key7': 'c'})


        def test_notlist_type(self):
            self.assertTrue(createDict(1,['a','b',2]) is None)
            self.assertTrue(createDict(['a','b','c'],'meow') is None)

    unittest.main(verbosity=2)