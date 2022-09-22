text = input('Enter yhe string: ')
character_number = int(input('Enter character number: '))
sym_list = list(text)

left_sym = sym_list[character_number - 2]
right_sym = sym_list[character_number]

print('Symbol on the left:', left_sym, '\nSymbol on the right:', right_sym)
if sym_list[character_number - 1] == left_sym and sym_list[character_number - 1] == right_sym:
    print('There are two matches.')
elif sym_list[character_number - 1] == left_sym or sym_list[character_number - 1] == right_sym:
    print('There is one coincidence.')
else:
    print('There are no matches.')
