import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Adivinhe un numero de 1 a {x}: '))
        if guess < random_number:
            print('Muito baixo. Vai de novo.')
        elif guess > random_number:
            print('Muito alto. Vai de novo.')

    print(f'Boaaa! Você acertou era o numero: {random_number} !!')


def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high'
        feedback = input(f'Ok meu palpite e {guess} ele e maior (H),'
                         'menor (L),ou eu acertei (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'A alma da maquina acertou mais uma {guess}.')


guess(10)
