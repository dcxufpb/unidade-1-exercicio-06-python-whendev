nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

# def isNoneOrEmpty(s):
#     return s == None or s == ""

def dados_loja():
    # Implemente aqui
    global numero
    if (nome_loja == ""):
        raise Exception("O campo nome da loja é obrigatório")
    if (logradouro == ""):
        raise Exception("O campo logradouro do endereço é obrigatório")
    if (numero == 0):
        numero = "s/n"
    if (municipio == ""):
        raise Exception("O campo município do endereço é obrigatório")
    if (estado == ""):
        raise Exception("O campo estado do endereço é obrigatório")
    if (cnpj == ""):
        raise Exception("O campo CNPJ da loja é obrigatório")
    if (inscricao_estadual == ""):
        raise Exception("O campo inscrição estadual da loja é obrigatório")
        
    _COMPLEMENTO = ""
    if (complemento != "" and complemento != None):
        _COMPLEMENTO = " " + complemento


    _BAIRRO = ""
    if (bairro != "" and bairro != None) :
        _BAIRRO = bairro + " - "


    _CEP = ""
    _TELEFONE = ""

    if (cep != "" and cep != None) :
        _CEP = "CEP:" + cep
        if (telefone != "" and telefone != None):
            _TELEFONE = " Tel " + telefone
    else :
        _CEP = ""
        if (telefone != "" and telefone != None):
            _TELEFONE = "Tel " + telefone

    _OBSERVACAO = ""

    if(observacao != "" and observacao != None):
        _OBSERVACAO = observacao


    _NUMERO = ""
    if (numero != 0):
        _NUMERO = numero


    if (numero == 0):
        _NUMERO = "s/n"



    show = f'''{nome_loja}
{logradouro}, {_NUMERO}{_COMPLEMENTO}
{_BAIRRO}{municipio} - {estado}
{_CEP}{_TELEFONE}
{_OBSERVACAO}
CNPJ: {cnpj}
IE: {inscricao_estadual}'''
    return show
