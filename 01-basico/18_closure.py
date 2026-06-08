# o closure é u conceito em python onde uma função interna tem acesso as variaveis do escopo da função externa mesmo depois de função externa ter sido executada. 
# isso permite que a função interna "lembre" do ambiente onde ela foi criada mesmo que ela seja chamada fora desse ambiente.

def fazer_saudacao(saudacao):
    # função interna que tem acesso a varavel saudacao da função externa
    def saudacao_personalizada(nome):
        return f"{saudacao}, {nome}"
    #retorna somente a função interna sem executar ela ou seja só a refencia da função interna é retornada, mesmo quando a função externa já tenha sido executada a função interna ainda tem aceso a variavel saudacao da função externa levando com sigo o ambinete onde foi criada.
    return saudacao_personalizada

# cada variavel abaixo é uma instancia diferenta da função interna , casda uma com seu proprio ambinete e sua pripria variavel saudação.
falar_bom_dia = fazer_saudacao("Bom dia")
falar_boa_tarde = fazer_saudacao("Boa tarde")

# as funções abaixo ainda sabem o valor da variavel saudacao meso depois da função externa ter sido executada, ele "lembra" do abinete onde foi criada.
print(falar_bom_dia("Antonio")) # Bom dia, Antonio
print(falar_boa_tarde("Maria")) # Boa tarde, Maria


# usando o closure para criar funções da saudação personalizada.
nomes= ["Jose", "Ana", "Carlos", "Gustavo"]

for nome in nomes:
    print(falar_bom_dia(nome))
    print(falar_boa_tarde(nome))


# resuindo, Um closure é uma função que carrega consigo as variáveis do escopo onde foi criada, permitindo acessá-las mesmo após o término da função externa.


# essa linhas acessam diretaente o valor que a closure capturou
print(falar_bom_dia.__closure__[0].cell_contents)
print(falar_boa_tarde.__closure__[0].cell_contents)