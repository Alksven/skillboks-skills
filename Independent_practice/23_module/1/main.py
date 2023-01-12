BRUCE_WILLIS = 42
try:
    input_data = input('Enter the string: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')

except ValueError as exc:
    print(type(exc), "— cannot be converted to a number.")
except IndexError as exc:
    print(type(exc), "— out of bounds list.")
except Exception as exc:
    print(type(exc), "other exceptions.")


