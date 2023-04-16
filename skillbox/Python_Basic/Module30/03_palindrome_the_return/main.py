from collections import Counter


def can_be_poly(text):
    counter = Counter(text)
    odd_count = sum(1 for count in counter.values() if count % 2 == 1)
    if odd_count <= 1:
        return True

    return False


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))