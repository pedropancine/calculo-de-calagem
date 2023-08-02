while True:
    produtor = str(input('Digite seu nome? -> '))
# Coleta de Dados da Análise de Solo
    k = float(input('Digite a quantidade de K? -> '))
    ca = float(input('Digite a quantidade de Ca? -> '))
    mg = float(input('Digite a quantidade de Mg? -> '))
    na = float(input('Digite a quantidade de Na? -> '))
    al = float(input('Digite a quantidade de Al? -> '))
    h_al = float(input('Digite a quantidade de H+Al? -> '))
    try:
        v2 = int(input('\033[32m'+'Qual é o seu V2?\n'
                       '1 - para cereais e tubérculos = 50%\n'
                       '2 - para leguminosas e cana-de-açúcar, utilizado no Cerrado = 60%\n'
                       '3 - para hortaliças, café e frutas = 70%\n'
                       '-> '+'\033[0;0m'))
        if v2 in [1, 2, 3]:
            if v2 == 1:
                v2 = 50
            elif v2 == 2:
                v2 = 60
            else:
                v2 = 70
        else:
            print('\033[31m'+'Valor inválido. Utilize apenas 1, 2 ou 3 como entrada.'+'\033[0;0m')
            break
    except ValueError:
        print('\033[31m'+'Entrada inválida.'+'\033[0;0m')

# Cálculos
    sb = ca + mg + na
    t = k + ca + mg + al
    T = k + ca + mg + h_al
    v = sb / T * 100

    print(f'Soma de Bases (Sb) é {sb:.2f} cmolc/dm³')
    print(f'A CTC efetiva (t) é {t:.2f} cmolc/dm³')
    print(f'A CTC a pH=7 (T) é {T:.2f} cmolc/dm³')
    print(f'A saturação de bases é {v:.2f} cmolc/dm³')

# Descobrir a % do PRNT a ser usado na NC
    prnt = int(input('Qual é o PRNT (%) a ser trabalhado? -> '))
    f = 100/prnt

    NC = ((v2 - v)/100) * T * f
    print('\033[42m'+f'A necessidade de calagem do Sr(a). {produtor} é de {NC:.2f} t/ha'+'\033[0;0m')
    break
# Foram gastas 5 horas e 3 minutos nesse script
