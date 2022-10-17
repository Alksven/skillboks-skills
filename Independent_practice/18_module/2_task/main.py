name = input('Enter Name: ')
duty = int(input('How much should? '))

message = '{0}! {0}, Hello! How are you, {0}? Where is my {1} dollars? {0}! '.format(
    name,
    duty
)
print(message)