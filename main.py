import pandas as pd

data = {
        'Nome' : ['Grylo', 'Bob', 'Wanderson', 'Jô Soares'],
        'Idade':[55, 10, 70, 70],
        'Cidade':['Brazilandia', 'Valinhos', 'Barão Geraldo', 'São Paulo'] 
}

df = pd.DataFrame(data)
print(df)