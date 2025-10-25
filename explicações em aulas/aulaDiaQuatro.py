# Aula 4 de Python 📘
# Antes de executar, é recomendado usar o Google Colab (para melhor visualização e interatividade), mas pode usar o VSCode normalmente.
# Conteúdo:
# - [x] Funções
# - [x] Parâmetros e Argumentos


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import math
import time


preso_np = np.random.rand(10_000_000)
type(preso_np)

preso_list = list(preso_np)
type(preso_list)

t0 = time.time()
desc = preso_np * 0.90
final = desc + 5
reaz = np.sqrt(preso_np)
print("numPy: ", time.time() - t0,"segundos")

t0 = time.time()
desc = [p * 0.90 for p in preso_list]
final = [p + 5 for p in desc]
reaz = [math.sqrt(p) for p in preso_list]
print("python puro: ", time.time() - t0,"segundos")

vetor = np.array([17,21,100,34])
print("\nvetor (array 1D):")
print(vetor)

# verificando atributos
print('Formato do vetor:', vetor.shape)
print('Número de dimensões:', vetor.ndim)
print('Número total de elementos no vetor:', vetor.size)


matriz = np.array([[1,2,3],[4,5,6]])
print("\nmatriz (array 2D):")
print(matriz)
print('Formato do vetor:', matriz.shape)
print('Número de dimensões:', matriz.ndim)
print('Número total de elementos no vetor:', matriz.size)


arr = np.arange(24).reshape(4,3,2)
print("\n(Array 3D):\n")
print(arr)
print('Formato do vetor:', arr.shape)
print('Número de dimensões:', arr.ndim)
print('Número total de elementos no vetor:', arr.size)

vetor = np.array([17,21,100,34])
print("\nvetor (array 1D):")
print(vetor)

# verificando atributos
print('Formato do vetor:', vetor.shape)
print('Número de dimensões:', vetor.ndim)
print('Número total de elementos no vetor:', vetor.size)


matriz = np.array([[1,2,3],[4,5,6]])
print("\nmatriz (array 2D):")
print(matriz)
print('Formato do vetor:', matriz.shape)
print('Número de dimensões:', matriz.ndim)
print('Número total de elementos no vetor:', matriz.size)


arr = np.arange(24).reshape(4,3,2)
print("\n(Array 3D):\n")
print(arr)
print('Formato do vetor:', arr.shape)
print('Número de dimensões:', arr.ndim)
print('Número total de elementos no vetor:', arr.size)


dados = np.arange(16).reshape(4,4)
print(f"Matriz Original: \n{dados}")

np.random.seed(42)

n_users = 500

n_visits = np.random.randint(1, 51, size = n_users)

valor_carrinho = 0

# gerar o tempo no site (distribuindo normal, correlacioanndo com visitas)
# média de 20min, desvio padrão de 5, com um bônus por visita
time_on_site = np.random.normal(loc = 20, scale = 5, size = n_users) + n_visits * 0.5

time_on_site = np.round(time_on_site, 2)

# gerar o numero de item no carrinho (depende de visitas e tempo)
# usuários que visitam mais e passam mais tempo, tendem adicionar mais itens
items_on_cart = np.random.randint(0, 8, size = n_users) + (n_visits // 10)

# garante que o tempo no site influencie positivamente
items_on_cart = (items_on_cart + (time_on_site // 15)).astype(int)
items_on_cart

# valor compra
buy_value = (items_on_cart * 35) + np.random.normal() 

# se não houver items no carrinho, o valor da compra deve ser 0
buy_value[items_on_cart == 0] = 0
buy_value[buy_value < 0] = 0 # corrigir valores negativos
buy_value = np.round(buy_value, 2)

#unindo tudo um uma única matriz
# cada linha representa um usuário, cada linha uma métrica
ecomerce_data = np.column_stack((n_visits, time_on_site, items_on_cart, buy_value))

print("\nMatriz de dados do e-commerce:")
print("\nExemplo da nossa massa de dados:", ecomerce_data.shape)
print(ecomerce_data[:5])




# Calculando as Estatísticas
media_valor = np.mean(valor_col)
mediana_valor = np.median(valor_col)
std_valor = np.std(valor_col)


# --- GRÁFICO ---
plt.figure(figsize = (12, 5))
plt.hist(valor_col, bins = 30, color = 'skyblue', edgecolor = 'black', alpha = 0.7)
plt.axvline(media_valor, color = 'red', linestyle = '--', linewidth = 2, label = f'Média = R$ {media_valor:.2f}')
plt.axvline(mediana_valor, color = 'orange', linestyle = '--', linewidth = 2, label = f'Mediana = R$ {mediana_valor:.2f}')
plt.axvline(media_valor + std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'+1 DP = R$ {media_valor + std_valor:.2f}')
plt.axvline(media_valor - std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'-1 DP = R$ {media_valor - std_valor:.2f}')
plt.title('Distribuição dos Valores de Compra')
plt.xlabel('Valor da Compra (R$)')
plt.ylabel('Frequência')
plt.legend()
plt.grid(alpha = 0.3)
plt.show()

# Separando colunas
visitas_col = dados_ecommerce[:, 0]
tempo_col   = dados_ecommerce[:, 1]
itens_col   = dados_ecommerce[:, 2]
valor_col   = dados_ecommerce[:, 3]


# Calculando as Estatísticas
media_valor = np.mean(valor_col)
mediana_valor = np.median(valor_col)
std_valor = np.std(valor_col)


# --- GRÁFICO ---
plt.figure(figsize = (12, 5))
plt.hist(valor_col, bins = 30, color = 'skyblue', edgecolor = 'black', alpha = 0.7)
plt.axvline(media_valor, color = 'red', linestyle = '--', linewidth = 2, label = f'Média = R$ {media_valor:.2f}')
plt.axvline(mediana_valor, color = 'orange', linestyle = '--', linewidth = 2, label = f'Mediana = R$ {mediana_valor:.2f}')
plt.axvline(media_valor + std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'+1 DP = R$ {media_valor + std_valor:.2f}')
plt.axvline(media_valor - std_valor, color = 'green', linestyle = ':', linewidth = 2, label = f'-1 DP = R$ {media_valor - std_valor:.2f}')
plt.title('Distribuição dos Valores de Compra')
plt.xlabel('Valor da Compra (R$)')
plt.ylabel('Frequência')
plt.legend()
plt.grid(alpha = 0.3)
plt.show()

np.random.seed(42)

n_users = 500

n_visits = np.random.randint(1, 51, size = n_users)

valor_carrinho = 0

# gerar o tempo no site (distribuindo normal, correlacioanndo com visitas)
# média de 20min, desvio padrão de 5, com um bônus por visita
time_on_site = np.random.normal(loc = 20, scale = 5, size = n_users) + n_visits * 0.5

time_on_site = np.round(time_on_site, 2)

# gerar o numero de item no carrinho (depende de visitas e tempo)
# usuários que visitam mais e passam mais tempo, tendem adicionar mais itens
items_on_cart = np.random.randint(0, 8, size = n_users) + (n_visits // 10)

# garante que o tempo no site influencie positivamente
items_on_cart = (items_on_cart + (time_on_site // 15)).astype(int)
items_on_cart

# valor compra
buy_value = (items_on_cart * 35) + np.random.normal()

# se não houver items no carrinho, o valor da compra deve ser 0
buy_value[items_on_cart == 0] = 0
buy_value[buy_value < 0] = 0 # corrigir valores negativos
buy_value = np.round(buy_value, 2)

#unindo tudo um uma única matriz
# cada linha representa um usuário, cada linha uma métrica
ecomerce_data = np.column_stack((n_visits, time_on_site, items_on_cart, buy_value))

print("\nMatriz de dados do e-commerce:")
print("\nExemplo da nossa massa de dados:", ecomerce_data.shape)
print(ecomerce_data[:5])


np.random.seed(42)

n_users = 500

n_visits = np.random.randint(1, 51, size = n_users)

valor_carrinho = 0

# gerar o tempo no site (distribuindo normal, correlacioanndo com visitas)
# média de 20min, desvio padrão de 5, com um bônus por visita
time_on_site = np.random.normal(loc = 20, scale = 5, size = n_users) + n_visits * 0.5

time_on_site = np.round(time_on_site, 2)

# gerar o numero de item no carrinho (depende de visitas e tempo)
# usuários que visitam mais e passam mais tempo, tendem adicionar mais itens
items_on_cart = np.random.randint(0, 8, size = n_users) + (n_visits // 10)

# garante que o tempo no site influencie positivamente
items_on_cart = (items_on_cart + (time_on_site // 15)).astype(int)
items_on_cart

# valor compra
buy_value = (items_on_cart * 35) + np.random.normal()

# se não houver items no carrinho, o valor da compra deve ser 0
buy_value[items_on_cart == 0] = 0
buy_value[buy_value < 0] = 0 # corrigir valores negativos
buy_value = np.round(buy_value, 2)

#unindo tudo um uma única matriz
# cada linha representa um usuário, cada linha uma métrica
dados_ecommerce = np.column_stack((n_visits, time_on_site, items_on_cart, buy_value))

print("\nMatriz de dados do e-commerce:")
print("\nExemplo da nossa massa de dados:", dados_ecommerce.shape)
print(dados_ecommerce[:5])


# Filtro para visitantes que não compraram
visitantes_sem_compra = dados_ecommerce[dados_ecommerce[:, 3] == 0]


print("\n--- ANÁLISE: VISITANTES QUE NÃO COMPRAM ---\n")
print(f"Número de visitantes que não compraram: {visitantes_sem_compra.shape[0]}")


# Estatísticas deste segmento
media_tempo_sem_compra = np.mean(visitantes_sem_compra[:, 1])
media_visitas_sem_compra = np.mean(visitantes_sem_compra[:, 0])


print(f"Média de visitas desses visitantes: {media_visitas_sem_compra:.2f}")
print(f"Apesar de não comprarem, eles passam em média {media_tempo_sem_compra:.2f} min no site.")

# Calcula a matriz de correlação
matriz_correlacao = np.corrcoef(dados_ecommerce, rowvar = False)


# Define os nomes das variáveis
nomes_variaveis = ["Visitas", "Tempo no Site", "Itens no Carrinho", "Valor da Compra"]


# Converte em DataFrame para exibir com rótulos
df_correlacao = pd.DataFrame(matriz_correlacao,
                             index = nomes_variaveis,
                             columns = nomes_variaveis)


# Matriz de correlação (mapa de calor)
plt.figure(figsize = (7, 5))
sns.heatmap(df_correlacao, annot = True, cmap = "Blues", fmt = ".2f")
plt.title("Matriz de Correlação")
plt.show()


df_dsa = pd.read_csy("datasetnovo.csv")


## ------------------------------------


df_dsa = pd.read_csv("datasetnovo.csv")

df_dsa.head(3)

df_dsa.shape
df_dsa.columns

df_dsa.info()
df_dsa.isnull().sum()
df_dsa.corr()
df_dsa.describe()

df_dsa['horas_estudo_mes'].describe()

sns.histplot(data = df_dsa, x = 'horas_estudo_mes', kde = True)

x = np.array(df_dsa['horas_estudo_mes'])
type(x)
x

x = x.reshape(-1,1)
type(x)
x

y = df_dsa['salario']
type(y)
y

plt.scatter(x , y, color='green', label='dados reais historicos')
plt.xlabel('horas_estudo_mes')
plt.ylabel('salario')
plt.legend()
plt.show()

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.2, random_state=42)
print(f'{x_treino.shape}1treiX {x_teste.shape}2testX \n\n {y_treino.shape}1treiY {y_teste.shape}2testY')

modelo = LinearRegression()
modelo
## ou modelo.fit(x_treino, y_treino)

plt.scatter(x , y, color='green', label='dados reais historicos')
plt.plot(x, modelo.predict(x), color='red', label='regressao linear')
plt.xlabel('horas_estudo_mes')
plt.ylabel('salario')
plt.legend()
plt.show()

score =  modelo.score(x_teste, y_teste)
print(f"Coeficiente de determinação (R2): {score:.2f}")
modelo.intercept_
modelo.coef_
horas_estudo_novo = np.array([[54]])
salario_previsto = modelo.predict(horas_estudo_novo)
print(salario_previsto)


# Criando uma Series (uma única coluna)
s = pd.Series([10, 20, 30, 40, 50], name = 'Valores')# Criando uma Series (uma única coluna)
s = pd.Series([10, 20, 30, 40, 50], name = 'Valores')
print(s)

dados = {
    'Nome': ['Ana', 'Bruno', 'Fabiana', 'Ronaldo', 'Eliana', 'Matias'],
    'Idade': [28, 34, 29, 17, None, 78],
    'Cidade': ['Blumenau', 'São Paulo', 'Blumenau', 'São Paulo', 'Salvador', 'São Paulo'],
    'Salário': [None, 7500, 6200, 9300, 8100, 15400]
}

type(dados)
print(dados)

df_dsa = pd.DataFrame(dados)

type(df_dsa)
print('\n--- Exemple de Dataframe ---\n')
print(df_dsa)

df_dsa.to_csv('dados_funcionarios_sem_indice.csv', index=False, encoding='utf-8')
df_dsa.to_csv('dados_funcionarios_com_indice.csv', encoding='utf-8')
df_dsa_1 = pd.read_csv('dados_funcionarios_sem_indice.csv')
df_dsa_1.head(6)



# ## intervalo nada para fazer vou me incomodar com esse cadastro de novo kkkkk ###
# print("Olá! Vamos criar seu cadastro.")
# nome = input("Qual é o seu nome? ") 
# sobrenome = input("Qual é o seu sobrenome? ") 
# idade = int(input("Quantos anos você tem? "))
# email = input("Qual é o seu email? ")
# while True:
#     senha = input("Digite a senha: ")
#     comSenha = input("Confirme a senha: ")

#     if senha == comSenha:
#         print("Senha confirmada com sucesso.")
#         break  # sai do loop se estiver correta
#     else:
#         print("As senhas não coincidem. Tente novamente.\n")

# while True:
#     termos = input("Você aceita os termos? (sim ou não) ").strip().lower()

#     if termos == 'sim' or termos == 's':
#         print("Você aceitou os termos.")
#         break  # sai do loop se aceitou
#     elif termos == 'não' or termos == 'nao' or termos == 'n':
#         print("Você não aceitou os termos. Por favor, aceite para continuar.\n")
#         # continua pedindo até aceitar
#     else:
#         print("Resposta inválida sobre os termos. Responda com 'sim' ou 'não'.\n")


# nomeFull = nome + " " + sobrenome
# ano_nascimento = 2025 - int(idade) # convertendo idade para inteiro

# print("Seja bem-vindo, " + nomeFull + "!")
# print("Você tem ", idade, " anos.") # calculada como string

# print(f"seus dados:\n nome: {nomeFull}\n, idade: {idade}\n, email: {email}\n, senha: {senha}\n, termos: {termos}\n, data de naciento: {ano_nascimento} \n Fim do cadastro programa.")
#cadastro finalizado com sucesso! :)