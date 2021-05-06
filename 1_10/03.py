import re

aaaa = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
print([len(o) for o in re.sub('[,\.]', '', aaaa).split(' ')])
