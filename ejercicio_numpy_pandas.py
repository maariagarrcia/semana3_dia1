import numpy as np
from colorama import Fore
import pandas as pd


def matrices():
    # crear una  matriz de 2*3*5 con valores aleatorios enteros
    a = np.random.randint(0, 100, (2, 3, 5))
    # Crear una matriz de 2*3*5 con valores aleatorios 

    print(Fore.YELLOW+"Matriz de  2*3*5:"+Fore.WHITE)
    print(a)
    print()
    # crear una matriz de 5*2*3 con valores = 1
    b = np.ones((5, 2, 3))
    print(Fore.YELLOW+"Matriz de 5*2*3"+Fore.WHITE)
    print(b)
    # a y b tienen el mismo tamaño?
    print()
    print(Fore.YELLOW+"Vamos a ver si tienen el mismo tamaño"+Fore.WHITE,a.shape == b.shape)

    # valores maximos minimos y medio de a
    d_max = a.max()
    d_min = a.min()
    d_mean = a.mean()
    print()
    print(Fore.YELLOW+"Vamos a ver los valores maximos, minimos y el valor del medio"+Fore.WHITE,d_max, d_min, d_mean)

    f = np.empty((2, 3, 5))
    print(Fore.YELLOW+"Matriz vacia de 2*3*5"+Fore.WHITE)
    print(f)


    for i in range(2):
        for j in range(3):
            for k in range(5):
                if a[i][j][k] > d_min and a[i][j][k] < d_mean:
                    f[i][j][k] = 25
                elif a[i][j][k] >= d_mean and a[i][j][k] < d_max:
                    f[i][j][k] = 75
                elif a[i][j][k] == d_max:
                    f[i][j][k] = 100
                else:
                    f[i][j][k] = 0


    print()
    print(Fore.YELLOW+"Matriz f:"+Fore.WHITE)
    print(f)
def  Dataframe():
    matriz = [[53.1, 95.0, 67.5, 35.0, 78.4],
              [61.3, 40.8, 30.8, 37.8, 87.6],
              [20.6, 73.2, 44.2, 14.6, 91.8],
              [57.4, 0.1, 96.1, 4.2, 69.5],
              [83.6, 20.5, 85.4, 22.8, 35.9],
              [49.0, 69.0, 0.1, 31.8, 89.1],
              [23.3, 40.7, 95.0, 83.8, 26.9],
              [27.6, 26.4, 53.8, 88.8, 68.5],
              [96.6, 96.4, 53.4, 72.4, 50.1],
              [73.7, 39.0, 43.2, 81.6, 34.7]]
    
    df = pd.DataFrame(matriz)
    print()
    print(Fore.YELLOW+"Dataframe:"+Fore.WHITE)
    print(df)
    
    # Rename the data frame columns based on the names in the list below.
    
    
    colnames = ['Score_1', 'Score_2', 'Score_3', 'Score_4', 'Score_5']
    df.columns = colnames
    print()
    print(Fore.YELLOW+"Dataframe con nombres de columnas:"+Fore.WHITE)
    print(df)
    
    # Create a subset of this data frame that contains only the Score 1, 3, and 5 columns.
    df_subset = df[['Score_1', 'Score_3', 'Score_5']]
    print()
    print(Fore.YELLOW+"Dataframe con nombres de columnas:"+Fore.WHITE)
    print(df_subset)
    
    #From the original data frame, calculate the average Score_3 value.
    print()
    print(Fore.YELLOW+"Promedio de Score_3:"+Fore.WHITE)
    print(df['Score_3'].mean())
    
    # Create a Pandas DataFrame from the dictionary of product orders below.
    orders = {'Description': ['LUNCH BAG APPLE DESIGN',
      'SET OF 60 VINTAGE LEAF CAKE CASES ',
      'RIBBON REEL STRIPES DESIGN ',
      'WORLD WAR 2 GLIDERS ASSTD DESIGNS',
      'PLAYING CARDS JUBILEE UNION JACK',
      'POPCORN HOLDER',
      'BOX OF VINTAGE ALPHABET BLOCKS',
      'PARTY BUNTING',
      'JAZZ HEARTS ADDRESS BOOK',
      'SET OF 4 SANTA PLACE SETTINGS'],
     'Quantity': [1, 24, 1, 2880, 2, 7, 1, 4, 10, 48],
     'UnitPrice': [1.65, 0.55, 1.65, 0.18, 1.25, 0.85, 11.95, 4.95, 0.19, 1.25],
     'Revenue': [1.65, 13.2, 1.65, 518.4, 2.5, 5.95, 11.95, 19.8, 1.9, 60.0]}
    
    df = pd.DataFrame(orders)
    print()
    print(Fore.YELLOW+"Dataframe:"+Fore.WHITE)
    print(df)
    
    # Calculate the total quantity ordered and revenue generated from these orders.
    print()
    print(Fore.YELLOW+"Cantidad total ordenada "+Fore.WHITE)
    print(df['Quantity'].sum())
    print()
    print(Fore.YELLOW+"Ingresos generados por estos pedidos:"+Fore.WHITE)
    print(df['Revenue'].sum())

