a = "abcdee"
b = "aecdbe"


def compare_perm(a, b):
    if a is None or b is None:
        raise Exception()

    if len(a) != len(b):
        return False
    m = {}

    for elem in a:
        if m.get(elem) is None:
            m[elem] = 1
        else:
            m[elem] += 1

    for elem in b:
        if m.get(elem) is None:
            return False
        m[elem] -= 1

    for count in m.values():
        if count != 0:
            return False

    return True


compare_perm("a", "ab")
compare_perm("", "")
compare_perm(None, None)
compare_perm(None, "None")
compare_perm("abc", "cba")
compare_perm("aab", "baa")
compare_perm("aab", "bba")
