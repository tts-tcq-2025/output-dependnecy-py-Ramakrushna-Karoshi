from tshirts import size

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
