# Douglas Vieira
# @ansattz


#1a - Não delete nem modifique esta linha
def incluir_contato(nome, telefone='', email='', instagram=''):
    """ A função inclui um contato na lista sendo o primeiro argumento prioritário;
    str, str, str, str -> list """
    contatoinfo=[]
    newcontactinfo=contatoinfo + [nome,] + [[telefone,]] + [email,] + [instagram,]
    return newcontactinfo


#Casos de teste da questão 1a - Não delete nem modifique esta linha
print(incluir_contato('R. Giggs',))
print(incluir_contato('Lahm','55558888','w@gmail.com'))
print(incluir_contato('Robin van Persie','55559999','robin@gmail.com', '@rvp'))
print(incluir_contato('Lehmann','','leh@protonmail.com',))

incluir_contato('R. Giggs',)
incluir_contato('Lahm','55558888','w@gmail.com')
incluir_contato('Robin van Persie','55559999','robin@gmail.com', '@rvp')
incluir_contato('Lehmann','','leh@protonmail.com',)


#1b - Não delete nem modifique esta linha
def editar_contato(lista, x, st):
    """ A função edita e informa se uma informação foi editada ou se ela já estava na lista;
    list, int, str - > bool """
    if x<0 or x>3:
        return False
    if x != 1:
        return True
    if int(lista[1][0]) == int(st) or int(lista[1][1]) == int(st):
        return False
    else:
        return True


# #Casos de teste da questão 1b - Não delete nem modifique esta linha
print(editar_contato(['Anderson',['21332312','56879791'],'andr@gmail.com','@ander'],1,'21332312'))
print(editar_contato(['A. Arshavin',['21332312','56879791'],'aarsh@gmail.com','@arshv'],1,'56879791'))
print(editar_contato(['A.Cole',['21332312','56879791'],'cole@gmail.com','@acole'],1,'98244587'))
print(editar_contato(['Pires',['21332312','56879791'],'rooney@gmail.com','@wroo'],0,'W. Rooney'))
print(editar_contato(['Touré',['21332312','56879791'],'ferdinand@gmail.com','@ferdinand'],0,'Rio Ferdinand'))
print(editar_contato(['Paul Scholes',['21332312','56879791'],'pscholes@gmail.com','@ppsch'],3,'@pscholes'))
print(editar_contato(['S. Gerrard ',['21332312','56879791'],'grr@gmail.com','@gerrardd'],2,'gerrard@aol.com'))

editar_contato(['Anderson',['21332312','56879791'],'andr@gmail.com','@ander'],1,'21332312')
editar_contato(['A. Arshavin',['21332312','56879791'],'aarsh@gmail.com','@arshv'],1,'56879791')
editar_contato(['A.Cole',['21332312','56879791'],'cole@gmail.com','@acole'],1,'98244587')
editar_contato(['Pires',['21332312','56879791'],'rooney@gmail.com','@wroo'],0,'W. Rooney')
editar_contato(['Touré',['21332312','56879791'],'ferdinand@gmail.com','@ferdinand'],0,'Rio Ferdinand')
editar_contato(['Paul Scholes',['21332312','56879791'],'pscholes@gmail.com','@ppsch'],3,'@pscholes')
editar_contato(['S. Gerrard ',['21332312','56879791'],'grr@gmail.com','@gerrardd'],2,'gerrard@aol.com')


#2  - Não delete nem modifique esta linha
def traducao_RNAm(st):
    """ A função separa cada códon da sequência de nucleotídeos do ARN de forma que nos
    retorne sua correspondência com os aminoácidos;
    str -> str """
    RNAxAm = {
        "UUU": "Phe",
        "CUU": "Leu",
        "UUA": "Leu",
        "AAG": "Lisina",
        "UCU": "Ser",
        "UAU": "Tyr",
        "CAA": "Gln"
    }
    tRNA = RNAxAm[st[0:3]] + '-' + RNAxAm[st[3:6]] + '-' + RNAxAm[st[6:9]]
    return tRNA


#2 O usuário precisa saber que a sequência pode ter sido digitada incorretamente. 
# def traducao_RNAm(st):
#     try:
#         RNAxAm = {
#             "UUU": "Phe",
#             "CUU": "Leu",
#             "UUA": "Leu",
#             "AAG": "Lisina",
#             "UCU": "Ser",
#             "UAU": "Tyr",
#             "CAA": "Gln"
#         }
        
#         tRNA = RNAxAm[st[0:3]] + '-' + RNAxAm[st[3:6]] + '-' + RNAxAm[st[6:9]]
#         return tRNA
#     except KeyError:
#         print('Sequência incorreta!')


#Casos de teste da questão 2 - Não delete nem modifique esta linha
print(traducao_RNAm('UUUUUAUCU'))
print(traducao_RNAm('CAAUAUUCU'))
print(traducao_RNAm('UUAAAGUCU'))

traducao_RNAm('UUUUUAUCU')
traducao_RNAm('CAAUAUUCU')
traducao_RNAm('UUAAAGUCU')
