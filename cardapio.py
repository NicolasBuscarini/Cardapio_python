print ("""
*****************************************************
*                                                   *
                 Restaurante Mosca Frita
*****************************************************
*                                                   *
*                                                   *
* Escolha o cardapio que deseja visualizar          *
*                                                   *
* Dia           Prato Principal         Opção       *
* Domingo       Macarronada             Dom         *
* Quarta        Feijoada                Qua         *
* Sexta         Peixe Grelhado          Sex         *
* Sábado        Churrasco               Sab         *
*                                                   *
*****************************************************""")

opc = "entrawhile"
while opc != "DOM" and opc != "QUA" and opc != "SEX" and opc != "SAB":
    opc = str(input("Digite a opção desejada: "))
    opc = opc.upper()
    if opc != "DOM" and opc != "QUA" and opc != "SEX" and opc != "SAB":
        print(" Opção invalida! \n Tente de novo")
    
if opc == "DOM":
    p = 12.90 
    print (f"""Opção Escolhida: Domingo
Prato do dia: Macarronada
R${p:.2f}""")
if opc == "QUA":
    p = 15.50 
    print (f"""Opção Escolhida: Quarta
Prato do dia: Feijoada
R${p:.2f} """)
if opc == "SEX":
    p = 11.00 

    print (f"""Opção Escolhida: Sexta
Prato do dia: Peixe Grelhado
R${p:.2f}""")
if opc == "SAB":
    p = 14.30 
    print (f"""Opção Escolhida: Sabado
Prato do dia: Churrasco
R${p:.2f}""")

qt = int(input("Quandidade: "))
total = p*qt
print (f"Valor a ser pago: R${total:.2f}")

desc = str(input("Desconto? (S/N):"))
desc = desc.upper()
if desc == "S":
    taxa = float(input("Informe a taxa, em porcentagem, de desconto concedida: "))/100
    print(f"\n\nValor do desc: {taxa*total:.2f}")
    total = total - taxa*total
    print(f"Valor a ser pago: {total:.2f} ")
else:
    print("\n\nSem desconto!")
    print(f"Valor a ser pago: {total:.2f} ")
    

