# Ordinal numbers indicate their position in a list, such as 1st and 2nd.
# Most ordinal numbers end in th, except 1,2, and 3. 
# 1) Store the numbers 1 through 9 in a list
# 2) Loop through the list
# 3) Use an if-elif-else chain inside the loop to print the proper ordinal ending for each number.
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", and each result should be on a separate line

for num in range(1,10):
    if num == 1:
        string = f'{num}st'
    elif num == 2:
        string = f'{num}nd'
    else:
        string = f'{num}th'
        
    print(string)