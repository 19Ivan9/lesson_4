print('tack1:')
ex_srt = 'helloworld'
if len(ex_srt) >= 2:
    result = ex_srt[0:2] + ex_srt[-2:]
    print(result)
else:
    print('')

ex_srt1 = 'my'
if len(ex_srt1) >= 2:
    result = ex_srt1[0:2] + ex_srt1[-2:]
    print(result)
else:
    print('')

ex_srt2 = 'x'
if len(ex_srt2) >= 2:
    result = ex_srt2[0:2] + ex_srt2[-2:]
    print(result)
else:
    print('')


print('tack2:')
print('Enter the phone number in the specified format"3805048562"\n'
      +'Use available operators: "MTS","Kyivstar","Live"')
phone_number = input()
if phone_number.isdigit() and len(phone_number) == 10:
    print('ok')
    if phone_number[0:5] == '38050':
        print('Using MTS')
    elif phone_number[0:5] == '38039':
        print('Using Kyivstar')
    elif phone_number[0:5] == '38063':
        print('Using Live')
    else:
        print('Error! This number cannot be used')
elif phone_number.isdigit() and (len(phone_number) < 10 or len(phone_number) > 10):
    print('Invalid number of characters!')
else:
    print('Number entered incorrectly')

print('tack3:')
name = 'ivan'
my_name = input("What's your name? ")

if name == my_name:
    print(f'Hallo {my_name}')
elif my_name == name.capitalize() or my_name == name.upper() or my_name == name.lower():
    print(f'Hallo {my_name}')
else:
    if my_name.isalpha():
        i = 0
        while i <= len(name)-1:
            if my_name[i] == name[i]:
                i += 1
            elif my_name[i] == name[i].upper():
                i += 1
            elif my_name[i] == name[i].lower():
                i += 1
            else:
                break

        print(f'Hallo {my_name}')
    else:
        print('Invalid input format')
