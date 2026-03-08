import pandas as pd

alunos = {
    'Nome': ['Maria', 'Jonas', 'Celso', 'João', 'Ana Luiza'],
    'Notas': [10, 8, 9, 3, 5],
    'Genero': ['Feminino', 'Masculino', 'Masculino', 'Masculino', 'Feminino']
}

df = pd.DataFrame(alunos)

# Informações gerais
print("-> Informações estatícas: \n",df.describe(include="all").round())

# Linhas x Colunas
print(f"\nNesta tabela há: {df.shape[0]} linhas e {df.shape[1]} colunas.")

# Quantidade de alunas e alunos
print(f'\nNesta turma há {(df['Genero'] == 'Feminino').sum()} meninas e {(df["Genero"] == 'Masculino').sum()} meninos.')

# Alunos com nota entre 1 e 6
print(f'\nAlunos com nota entre 1 e 6: {((df['Notas'] >= 1 ) & (df['Notas'] <= 6)).sum()} alunos.')

# Utilizando apply
def notas(x):
    return x/2

df['Nota_dividida'] = df['Notas'].apply(notas)
print(df,'\n')

# Ordenando por ordem alfabética os nomes
print(df.sort_values(ascending=True, by=['Nome']))

# Nomes e notas somente de alunas
print('\nAlunas e resultados:')
print(df[df['Genero'].isin(['Feminino'])][['Nome', 'Notas']])