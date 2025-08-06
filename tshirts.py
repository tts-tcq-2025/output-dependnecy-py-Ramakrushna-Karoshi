
# def size(cms):
#     if cms < 38:
#         return 'S'
#     elif cms > 38 and cms < 42:
#         return 'M'
#     else:
#         return 'L'


# assert(size(37) == 'S')
# assert(size(40) == 'M')
# assert(size(43) == 'L')

# print("All is well (maybe!)")


#***************************************************************************************************************#
#***************************************************************************************************************#
#***************************************************************************************************************#


def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


# test code 
# from size_module import size

def test_size_edge_case():
    assert size(38) == 'S', "Expected size(38) to return 'S', but got something else"

def test_all_cases():
    assert size(36) == 'S'
    assert size(39) == 'M'
    assert size(43) == 'L'

if __name__ == "__main__":
    test_size_edge_case()
    test_all_cases()
    print("All tests completed.")



