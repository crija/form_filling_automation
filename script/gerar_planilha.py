import pandas as pd

# Criar um DataFrame com dados de exemplo
data = {

    'Nome': ['Carla'],
    'Email': ['carlinha@123.com']
    'Telefone': ['51998123093'],

}

df = pd.DataFrame(data)

# Salvar o DataFrame em uma planilha Excel
df.to_excel('planilha_teste.xlsx', index=False)

print("Planilha 'planilha_teste.xlsx' criada com sucesso.")
