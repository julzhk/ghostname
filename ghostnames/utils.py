def tuplify_list(l):
    """
    >>> tuplify_list([1,2,3])
[(1, 1), (2, 2), (3, 3)]
>>> tuplify_list(['a','b','c'])
[('a', 'a'), ('b', 'b'), ('c', 'c')]
>>> tuplify_list(['a','b','c',1,2,3])
[('a', 'a'), ('b', 'b'), ('c', 'c'), (1, 1), (2, 2), (3, 3)]
>>> tuplify_list([])
[]
    :param l: iterable
    :return: list of tuples
    """
    return [(i,i) for i in l]