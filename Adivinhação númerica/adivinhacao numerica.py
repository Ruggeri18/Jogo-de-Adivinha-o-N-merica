import random

print("Bem-Vindo")

while True:
    choice_number = input("Digite o número teto do desafio: ")
    if choice_number.isnumeric():
        choice_number = int(choice_number)
        break
    else:
        print("Erro, digite apenas números!")

random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input("Adivinhe o número: ")

    if answer_user.isnumeric():
        answer_user = int(answer_user)
    else:
        print("Erro: valor digitado não é numérico!")
        continue

    n_choices = n_choices + 1

    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto, o número randômico é menor do que isso...")
    else:
        print("Chutou baixo, o número randômico é maior do que isso...")

print("Numero de tentativas:", n_choices)