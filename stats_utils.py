from datetime import date, datetime
import numpy as np
from statistics import mean, stdev
import pandas as pd
import math
import re

def get_data(csv_file_dir_string):
    data = pd.read_csv(csv_file_dir_string, delimiter=",")
    return data

# para cortar casas decimais
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

# para extrair porcentagens da amostra
def percentage(sample_n, valuable_amount):
    x = valuable_amount / sample_n
    return x

# para calcular a idade
def calculate_age(born, answer_date):
    return int(answer_date.year - born.year - ((answer_date.month, 
                                            answer_date.day) < 
                                           (born.month, born.day))

def comparar_chefe (pai, mae):
    for item in niveis_educacionais:
        if pai == item[0]:
            nivel_pai = item[1]
        if mae == item[0]:
            nivel_mae = item[1]
    if nivel_pai > nivel_mae:
        return nivel_pai
    elif nivel_mae > nivel_pai:
        return nivel_mae
    elif nivel_mae == nivel_pai:
        return nivel_mae
               
# cálculo sociodemográfico
def calculo_sociodem (banheiro, 
                      empregados,
                      carros, 
                      computadores, 
                      loucas, 
                      geladeiras, 
                      freezers,
                      roupas, 
                      microondas,
                      secadores,
                      tv,
                      moto, 
                      encanamento,
                      pavimentacao,
                      educacao):
    escore = 0

    if banheiro == 0:
        escore += 0
    elif banheiro == 1:
        escore += 3
    elif banheiro == 2:
        escore += 7
    elif banheiro == 3:
        escore += 10
    elif banheiro == 4:
        escore += 14
        
    if empregados == 0:
        escore += 0
    elif empregados == 1:
        escore += 3
    elif empregados == 2:
        escore += 7
    elif empregados == 3:
        escore += 10
    elif empregados == 4:
        escore += 13
    
    if carros == 0:
        escore += 0
    elif carros == 1:
        escore += 3
    elif carros == 2:
        escore += 5
    elif carros == 3:
        escore += 8
    elif carros == 4:
        escore += 11
        
    if computadores == 0:
        escore += 0
    elif computadores == 1:
        escore += 3
    elif computadores == 2:
        escore += 6
    elif computadores == 3:
        escore += 8
    elif computadores == 4:
        escore += 11
        
    if loucas == 0:
        escore += 0
    elif loucas == 1:
        escore += 3
    elif loucas == 2:
        escore += 6
    elif loucas == 3:
        escore += 6
    elif loucas == 4:
        escore += 6
        
    if geladeiras == 0:
        escore += 0
    elif geladeiras == 1:
        escore += 2
    elif geladeiras == 2:
        escore += 3
    elif geladeiras == 3:
        escore += 5
    elif geladeiras == 4:
        escore += 5
        
    if freezers == 0:
        escore += 0
    elif freezers == 1:
        escore += 2
    elif freezers == 2:
        escore += 4
    elif freezers == 3:
        escore += 6
    elif freezers == 4:
        escore += 6
        
    if roupas == 0:
        escore += 0
    elif roupas == 1:
        escore += 2
    elif roupas == 2:
        escore += 4
    elif roupas == 3:
        escore += 6
    elif roupas == 4:
        escore += 6   
    
    if tv == 0:
        escore += 0
    elif tv == 1:
        escore += 1
    elif tv == 2:
        escore += 3
    elif tv == 3:
        escore += 4
    elif tv == 4:
        escore += 6
        
    if microondas == 0:
        escore += 0
    elif microondas == 1:
        escore += 2
    elif microondas == 2:
        escore += 4
    elif microondas == 3:
        escore += 4
    elif microondas == 4:
        escore += 4
        
    if moto == 0:
        escore += 0
    elif moto == 1:
        escore += 1
    elif moto == 2:
        escore += 3
    elif moto == 3:
        escore += 3
    elif moto == 4:
        escore += 3
            
    if secadores == 0:
        escore += 0
    elif secadores == 1:
        escore += 2
    elif secadores == 2:
        escore += 2
    elif secadores == 3:
        escore += 2
    elif secadores == 4:
        escore += 2
        
    if encanamento == "Sim":
        escore += 4
    
    if pavimentacao == "Sim":
        escore += 2
        
    escore = escore + educacao
    
    def calcular_classe_social(escore):
        if escore <= 16:
            return "6" # D e E
        elif (escore >= 17 and escore <= 22):
            return "5" # C2
        elif (escore >= 23 and escore <= 28):
            return "4" # C1
        elif (escore >= 29 and escore <= 37):
            return "3" # B2
        elif (escore >= 38 and escore <= 44):
            return "2" # B1
        elif (escore >= 45):
            return "1" # A
        
    return calcular_classe_social(escore)

def filter_date(data, birthdate_column_header_string, 
                answer_date_column_header_string ,
                lower_cut, upper_cut):
    '''
    data must be pandas dataframe
    lower_cut: idade mínima aceitável
    upper_cut: idade máxima aceitável
    '''
    birthdate = data[birthdate_column_header_string]
    answer_date = data[answer_date_column_header_string]
    date_booleans = []
    for pair in zip(birthdate, answer_date):
        birth_date_object = datetime.strptime(pair[0], '%Y-%m-%d')
        answer_date_object = datetime.strptime(pair[1][0:10],'%Y/%m/%d')
        age = calculate_age(birth_date_object, answer_date_object)
        if (age >= lower_cut and age <= upper_cut):
            date_booleans.append(True)
        else:
            date_booleans.append(False)
    return date_booleans

               
def alter_pd_age_column(data, data_de_nascimento_string_header, 
                        carimbo_de_data_e_hora_header, 
                        column_header_output_string="Idade"):
               
    for index in data.index:
        birth_date_object = datetime.strptime(data.loc[index, data_de_nascimento_string_header], '%Y-%m-%d')
        answer_date_object = datetime.strptime(data.loc[index, carimbo_de_data_e_hora_header][0:10],'%Y/%m/%d')
        data.loc[index, column_header_output] = calculate_age(birth_date_object, answer_date_object)
               
def alter_pd_column(data, function, column_header_input, column_header_output=None):
               
    '''
    column_header_input: título da coluna que se está analisando
    column_header_output: caso seja utilizada uma coluna diferente da que serve como input
    '''
              
    if column_header_output == None:    
        data.loc[index,column_header_input] = function(data.loc[index, column_header_input])
    else:
        data.loc[index,column_header_output] = function(data.loc[index, column_header_input])                            