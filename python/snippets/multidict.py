# use lists or sets depends on intended use. Use a list if
# you want to preserve the insertion order of the items. Use a set if you want to eliminate
# duplicates (and don’t care about the order).


d = {
 'a' : [1, 2, 3],
 'b' : [4, 5]
}
e = {
 'a' : {1, 2, 3},
 'b' : {4, 5}
}


from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)

d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)


