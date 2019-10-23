def find_sum_of_two(A, val):
    seen_values = set()
    for a in A:
        if val - a in seen_values:
            return True
        else:
            seen_values.add(a)
    return False


def test(v, val, expected):
    output = find_sum_of_two(v, val)
    print("exist(A, " + str(val) + ") = " + str(output) + "\n")
    assert expected == output


def main():
    v = [2, 1, 8, 4, 7, 3]
    test(v, 3, True)
    test(v, 20, False)
    test(v, 1, False)
    test(v, 2, False)
    test(v, 7, True)


main()
