import random

n = 0
count = 0
print()
while True:
    print('''Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29''')
    try:
        level = int(input())
        if level in [1, 2]:
            if level == 1:
                while count < 5:
                    int_operator = random.choice(['+', '-', '*'])
                    task = f'{random.randint(2, 9)} {int_operator} {random.randint(2, 9)}'
                    print(task)
                    while True:
                        user_ans = input()
                        try:
                            if int(user_ans) == eval(task.strip()):
                                count += 1
                                print('Right!')
                                n += 1
                                break
                            else:
                                count += 1
                                print('Wrong')
                                break
                        except ValueError:
                            print('Incorrect format.')
                print(f'Your mark is {n}/5. Would you like to save the result? Enter yes or no.')
                user_response = input()
                if user_response in ['y', 'YES', 'Yes', 'Y']:
                    with open('results.txt', 'a') as results_file:
                        user_name = input('What is your name?\n')
                        results_file.write(f'{user_name}: {n}/5 in level 1 (simple operations with numbers 2-9)')
                        print('The results are saved in "results.txt".')
                        exit()
                else:
                    exit()
            else:
                while count < 5:
                    num = random.randint(11, 29)
                    print(num)
                    while True:
                        user_ans = input()
                        try:
                            if int(user_ans) == (num * num):
                                count += 1
                                print('Right!')
                                n += 1
                                break
                            else:
                                count += 1
                                print('Wrong')
                                break
                        except ValueError:
                            print('Incorrect format.')
                print(f'Your mark is {n}/5. Would you like to save the result? Enter yes or no.')
                user_response = input()
                if user_response in ['y', 'YES', 'Yes', 'Y']:
                    with open('results.txt', 'a') as results_file:
                        user_name = input('What is your name?\n')
                        results_file.write(f'{user_name}: {n}/5 in level 2 (integral squares of 11-29)')
                        print('The results are saved in "results.txt".')
                        exit()
                else:
                    exit()
        else:
            print('Incorrect format.')
    except ValueError:
        continue


