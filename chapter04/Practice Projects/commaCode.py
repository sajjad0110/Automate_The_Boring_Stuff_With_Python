def commaCount(my_list):
    for i in range(len(my_list) - 1):
        print(my_list[i] + ', ', end='')
    print('and ' + my_list[i + 1])


spam = []

# Taking input of elements in spam from the user.
# When the user press Enter, input loop will break.
while True:
    item = input('Enter item ' + str(len(spam) + 1) +
                 ' (or enter nothing to stop): ')

    if item == '':
        break

    spam.append(item)

commaCount(spam)
