print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('{0} and {1}'.format('spam', 'eggs'))

print('{1} and {0}'.format('spam', 'eggs'))

print('This {food} is {adjective}.'.format(
      food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))

'12'.zfill(5)

'-3.14'.zfill(7)

'3.14159265359'.zfill(5)