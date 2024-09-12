import pandas as pd 
import numpy as np 

df = pd.read_excel(r"D:\MASTERS WORK\New Combined data.xlsx")
df.head()

df= df.drop(columns=['No'])

df

SB = df['S/B']
HB = df['H/B']
BD = df['B/D']
TB = df['T/B']
Pf = df['Pf(kg/m3)']
XB = df['XB(m)']
E = df['E(GPa)']
X50 = df['X50(m)']

sb = np.std(SB)
hb = np.std(HB)
bd = np.std(BD)
tb = np.std(TB)
pf = np.std(Pf)
XB = np.std(XB)
e = np.std(E)
x50 = np.std(X50)

dataset = []

# for _ in range(20):
#     for _, row in df.iterrows():
#         temp = {
#             'SB': row['S/B'],
#             'HB': row['H/B'],
#             'BD': row['B/D'],
#             'TB': row['T/B'],
#             'Pf': row['Pf(kg/m3)'],
#             'XB': row['XB(m)'],
#             'E': row['E(GPa)'],
#             'X50': row['X50(m)'],
#         }
#         dataset.append(temp)
#         print(temp)

for _ in range(20):
    for _, row in df.iterrows():
        temp = {
            'SB': row['S/B'] + np.random.normal(sb),
            'HB': row['H/B'] + np.random.normal(hb),
            'BD': row['B/D'] + np.random.normal(bd),
            'TB': row['T/B'] + np.random.normal(tb),
            'Pf': row['Pf(kg/m3)'] + np.random.normal(pf),
            'XB': row['XB(m)'] + np.random.normal(XB),
            'E': row['E(GPa)'] + np.random.normal(e),
            'X50': row['X50(m)'] + np.random.normal(x50),
        }
        dataset.append(temp)
        print(temp)

print(len(dataset), 'Entries synthetically created data.')

newdf = pd.DataFrame(dataset)
newdf.to_excel('new combined mbs dataset.xlsx')