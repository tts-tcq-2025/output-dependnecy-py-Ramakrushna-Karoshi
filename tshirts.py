
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'



assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')

# New test case to make it fail
assert(size(38) == 'S') # Expecting 'S' or 'M', but it will return 'L'

print("All is well (maybe!)")
