# atividade 02 Idade e peso

Idade = int(input(" Digite a sua idade"))
Peso = float(input(" Digite o seu peso"))

if Idade < 20 and Peso <= 60:
    print("Com", Idade, "anos e no peso de ", Peso, "Kilos, você está no risco 9 ")
elif Idade < 20 and Peso > 60 and Peso <= 90 :
    print("Com", Idade, "anos e no peso de ", Peso, "Kilos, você está no risco 8 ")
elif Idade < 20 and Peso > 90 :
    print("Com", Idade, "anos e no peso de ", Peso, "Kilos, você está no risco 7 ")
elif Idade >= 20 and Idade <= 50 and Peso <= 60 :
    print("Com", Idade, "anos e no peso de ", Peso, "Kilos, você está no risco 6 ")
elif Idade >= 20 and Idade <= 50 and Peso > 60 and Peso <= 90 :
    print("Com", Idade, "anos e no peso de ", Peso, "Kilos, você está no risco 5 ")
elif Idade >= 20 and Peso > 90 :
    print("Com", Idade, "anos e no peso de ", Peso, "Kilos, você está no risco 4 ")
elif Idade > 50 and Peso < 60 :
    print("Com", Idade, "anos e no peso de ", Peso, "Kilos, você está no risco 3 ")
elif Idade > 50 and Peso > 60 and Peso <= 90 :
    print("Com", Idade, "anos e no peso de ", Peso, "Kilos, você está no risco 2 ")
elif Idade > 50 and Peso > 90 :
    print("Com", Idade, "anos e no peso de ", Peso, "Kilos, você está no risco 1 ")