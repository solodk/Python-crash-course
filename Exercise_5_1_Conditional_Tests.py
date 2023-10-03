# Write a series of conditional tests. 
# Print a statement describing each test and your prediction for the results of each test.
# Create at least 10 tests. Have at least 5 tests evaluate  to True and another 5 tests evaluate to False

some_string = 'I like cars'
evaluation = 'cars' in some_string
print(f'Do i like cars? I predict True. {evaluation}')

evaluation = 2**4 > 4**2
print(f'Do 2^4 is greater than 4^2? I predict False. {evaluation}')

#evaluation = 2 in '1234'
print(f'Do 2 is in "1234" string? I predict False. You can`t compare string with int')