nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

answer_list = [x for w in range(len(nice_list)) for y in range(len(nice_list[w])) for x in nice_list[w][y]]

print(answer_list)
