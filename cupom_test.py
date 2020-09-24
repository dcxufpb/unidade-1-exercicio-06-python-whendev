import cupom
import pytest

# Refatoramento da verificação de campo obrigatório
def verifica_campo_obrigatorio(mensagem_esperada):
  with pytest.raises(Exception) as excinfo:
    cupom.dados_loja()
  the_exception = excinfo.value
  assert mensagem_esperada == str(the_exception)

# Todas as variáveis preenchidas
cupom.nome_loja = "Loja 1"
cupom.logradouro = "Log 1"
cupom.numero = 10
cupom.complemento = "C1"
cupom.bairro = "Bai 1"
cupom.municipio = "Mun 1"
cupom.estado = "E1"
cupom.cep = "11111-111"
cupom.telefone = "(11) 1111-1111"
cupom.observacao = "Obs 1"
cupom.cnpj = "11.111.111/1111-11"
cupom.inscricao_estadual = "123456789"

TEXTO_ESPERADO_LOJA_COMPLETA = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_loja_completa():
    assert cupom.dados_loja() == TEXTO_ESPERADO_LOJA_COMPLETA

def test_nome_vazio():
    # global nome_loja
    cupom.nome_loja = ""
    verifica_campo_obrigatorio("O campo nome da loja é obrigatório") 
    cupom.nome_loja = "Loja 1"

def test_logradouro_vazio():
    # global logradouro
    cupom.logradouro = ""
    verifica_campo_obrigatorio("O campo logradouro do endereço é obrigatório")
    cupom.logradouro = "Log 1"

TEXTO_ESPERADO_SEM_NUMERO = '''Loja 1
Log 1, s/n C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_numero_zero():
    # global numero
    cupom.numero = 0
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_NUMERO
    cupom.numero = 10

TEXTO_ESPERADO_SEM_COMPLEMENTO = '''Loja 1
Log 1, 10
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_complemento():
    # global complemento
    cupom.complemento = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_COMPLEMENTO
    cupom.complemento = "C1"

TEXTO_ESPERADO_SEM_BAIRRO = '''Loja 1
Log 1, 10 C1
Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_bairro():
    # global bairro
    cupom.bairro = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_BAIRRO
    cupom.bairro = "Bai 1"

def test_municipio_vazio():
    # global municipio
    cupom.municipio = ""
    verifica_campo_obrigatorio("O campo município do endereço é obrigatório")
    cupom.municipio = "Mun 1"

def test_estado_vazio():
    # global estado
    cupom.estado = ""
    verifica_campo_obrigatorio("O campo estado do endereço é obrigatório")
    cupom.estado = "E1"

TEXTO_ESPERADO_SEM_CEP = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_cep():
    # global cep
    cupom.cep = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_CEP
    cupom.cep = "11111-111"

TEXTO_ESPERADO_SEM_TELEFONE = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_telefone():
    # global telefone
    cupom.telefone = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_TELEFONE
    cupom.telefone = "(11) 1111-1111"

TEXTO_ESPERADO_SEM_OBSERVACAO = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111

CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_observacao():
    # global observacao
    cupom.observacao = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_OBSERVACAO
    cupom.observacao = "Obs 1"

def test_cnpj_vazio():
    # global cnpj
    cupom.cnpj = ""
    verifica_campo_obrigatorio("O campo CNPJ da loja é obrigatório")
    cupom.cnpj = "11.111.111/1111-11"

def test_inscricao_estadual_vazia():
    # global inscricao_estadual
    cupom.inscricao_estadual = ""
    verifica_campo_obrigatorio("O campo inscrição estadual da loja é obrigatório")
    cupom.inscricao_estadual = "123456789"

def test_exercicio2_customizado():
    # global nome_loja
    # global logradouro
    # global numero
    # global complemento
    # global bairro
    # global municipio
    # global estado
    # global cep
    # global telefone
    # global observacao
    # global cnpj
    # global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "LOJAS AMERICANAS S.A."
    cupom.logradouro = "R SACADURA CABRAL"
    cupom.numero = 102
    cupom.complemento = ""
    cupom.bairro = "GAMBOA"
    cupom.municipio = "RIO DE JANEIRO"
    cupom.estado = "RJ"
    cupom.cep = "20.221-160"
    cupom.telefone = "(21) 2206-6708"
    cupom.observacao = "47.11-3-02 Comercio varejista de mercadorias em geral"
    cupom.cnpj = "33.014.556/0001-96"
    cupom.inscricao_estadual = "85.687.08-5"

    #E atualize o texto esperado abaixo
    assert cupom.dados_loja() == '''LOJAS AMERICANAS S.A.
R SACADURA CABRAL, 102
GAMBOA - RIO DE JANEIRO - RJ
CEP:20.221-160 Tel (21) 2206-6708
47.11-3-02 Comercio varejista de mercadorias em geral
CNPJ: 33.014.556/0001-96
IE: 85.687.08-5'''
