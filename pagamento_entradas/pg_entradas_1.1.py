#Automatização do pagamento dos APs
mes_atual = input("Qual é o mês atual? ")
if mes_atual  in (["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro" ]):
 fr_input1 = "1. Digite o valor de água e esgoto referente a " + mes_atual +" : R$ "
 fr_input2 = "2. Digite o valor da conta de luz da entrada 21 referente a " + mes_atual + " : R$ "
 fr_input3 = "3. Digite o valor da conta de luz da entrada 41 referente a " + mes_atual + " : R$ "
 agua_esgoto  = input(fr_input1)
 light_21 = input(fr_input2)
 light_41 = input(fr_input3)
 valor_receber_total = 0
else: 
 input("o coloque um mês válido")

#Passar tudo de str para int
agua_esgoto_formatada = agua_esgoto.replace(',', '.')
agua_esgoto_valor = float(agua_esgoto_formatada)
light_21_formatada = light_21.replace(',', '.')
light_21_valor = float(light_21_formatada)
light_41_formatada = light_41.replace(',', '.')
light_41_valor = float(light_41_formatada)



#Calcular as cotas dos moradores e o total
total = (agua_esgoto_valor + light_21_valor + light_41_valor)
cota_morador = total/16
print("4. O valor total referente a esse mês é: R$", total)
print("5. Cada morador deve pagar como cota: R$", cota_morador)

#Calcular as cotas dos moradores e dos prédios

cota_predios = total/2
valor_receber_ent_21 = (total/2) - light_21_valor
valor_receber_ent_41 = cota_predios


print("6. O valor a receber da entrada 21 é: R$", valor_receber_ent_21)
print("7. O valor a receber da entrada 41 é: R$", valor_receber_ent_41)


#valores extras
serv_limp = input ("8. qual é o valor do serviço de limpeza? R$ ")
serv_limp = float(serv_limp)
serv_limp_total = serv_limp * 7
res_emerg = input("9. qual é o valor da reserva de emergência? R$ ")
res_emerg = float(res_emerg)
res_emerg_total = res_emerg * 8
print("10. O valor total da taxa do serviço de limpeza é: R$",serv_limp_total)
print("11. O valor total da reserva de emergência é: R$",res_emerg_total)


#função para definir quanto o proprietário deve receber
def responsavel( valor_receber_ent_41, valor_receber_ent_21, res_emerg_total, serv_limp_total):
 valor_receber_total =  (valor_receber_ent_21 + valor_receber_ent_41 + res_emerg_total + serv_limp_total )
 return valor_receber_total

#Cota da entrada 41 somada aos extras
cota_morador_41 = cota_morador + serv_limp + res_emerg
print("12. Cota geral da entrada 41: R$", cota_morador_41)

#Valor total que o responsável deve receber
valor_total_41 = valor_receber_ent_41 + serv_limp_total + res_emerg_total
print("13. O valor total que a entrada 41 vai receber é: R$ ",valor_total_41)
print ("14. O responsável deve receber: R$", responsavel(valor_receber_ent_41, valor_receber_ent_21, res_emerg_total, serv_limp_total))

input()
