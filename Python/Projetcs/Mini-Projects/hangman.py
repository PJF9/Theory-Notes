from random import randint


print('Welcome to Hangman game (only lower char allowed) :) --- Enjoy!!!')

def First_User_Input():
    databases = ["petros", "animal", "joy", "something"]

    return databases[randint(0, len(databases) - 1)]


def draw(lives):
    if lives == 5:
        print(''' 
        ________
        |       |
        |
        |
        |
        |
        |
        ''')
    elif lives == 4:
        print('''
        ________
        |       |
        |     (' ')
        |         
        | 
        |    
        ''')
    elif lives == 3:
        print('''
        ________
        |       |
        |     (' ')
        |       |      
        |     _//_
        |   
        ''')
    elif lives == 2:
        print('''
            _______
        |       |
        |     (' ') 
        |    ---|---   
        |     _//_
        |
        ''')
    elif lives == 1:
        print('''
        ________
        |       |
        |     (' ') 
        |    ---|---   
        |     _//_
        |    _______
        ''')
    elif lives == 0:
        print('''
        ________
        |       |
        |     (' ') 
        |    ---|---   
        |    ^.//.^^
        |    _^_^_^_
        ''')


def main():
    secret_input = First_User_Input()

    # Lives 
    lives = 5

    # Declaring the Lists
    List_Secret_Word = []
    List_User_Letters = []

    # Filling the Lists
    for i in range(len(secret_input)):
        List_Secret_Word.append(secret_input[i])
        List_User_Letters.append('_')

    # Starter 'word'
    print(*List_User_Letters, sep=' ')

    # Main Loop
    while lives > 0:
        
        # Check loop
        while True:
            # User letter
            user_word = input('Give me a letter : ')

            if len(user_word) > 1:
                print('Letters only please. Try again')

            else:
                break

        # If already in word
        if user_word in List_User_Letters:
            print(f'{user_word} is already in secret word')
        
        # If letter in word
        if (user_word in List_Secret_Word) and (user_word not in List_User_Letters):
            
            for i in range(len(List_Secret_Word)):
                
                if user_word == List_Secret_Word[i]:
                    List_User_Letters[i] = user_word
                    print(f'"{user_word}" is in secret word')
                    print(*List_User_Letters, sep=' ')   
                    print()
        
        elif user_word in List_User_Letters:
            print()

        else:
            # If not in secret word
            print(f'{user_word} is not in secret word')
            lives -= 1
            print(*List_User_Letters, sep=' ')
            print()
            print(f'You have {lives} lives left')
            print()

        draw(lives)

        # End game
        if lives == 0:
            print('I am sorry you lost')
            a = ''.join(List_Secret_Word)
            print(f'The secret word was {a}')
            break
        
        if List_User_Letters == List_Secret_Word:
            print('Corgatulations you find the secret word!!!')
            break

main()
