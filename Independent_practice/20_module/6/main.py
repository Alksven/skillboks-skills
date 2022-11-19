def function(object):
    object = list(object)
    answer = []
    for i, sym in enumerate(object):
        if i % 2 == 0:
            answer.append(sym)
    print(answer)


object = {100: 200, 300: 'буква', 0: 2}

function(object)