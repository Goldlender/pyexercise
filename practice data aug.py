import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

pd.set_option('display.float_format', '{:.3f}'.format)

#data = np.array([2.0, 5.0, 7.0, 9.0, 10.5, 12.6, 3.7, 7.8])
data = pd.read_excel(r"D:\MASTERS WORK\New Combined data.xlsx")
data
df = data.drop(columns=['No'])
df.head()

SB = df['S/B']
HB = df['H/B']
BD = df['B/D']
TB = df['T/B']
Pf = df['Pf(kg/m3)']
XB = df['XB(m)']
E = df['E(GPa)']
X50 = df['X50(m)']

# sb = np.std(SB)
# hb = np.std(HB)
# bd = np.std(BD)
# tb = np.std(TB)
# pf = np.std(Pf)
# XB = np.std(XB)
# e = np.std(E)
# x50 = np.std(X50)


mu = 0
sigma = 0.05 
#noise = np.random.normal(mu, sigma)

new_data = [] 

for _ in range(15):
    for _, row in df.iterrows():
        temp = {
            'SB': row['S/B'] + np.random.normal(mu, sigma),
            'HB': row['H/B'] + np.random.normal(mu, sigma),
            'BD': row['B/D'] + np.random.normal(mu, sigma),
            'TB': row['T/B'] + np.random.normal(mu, sigma),
            'Pf': row['Pf(kg/m3)'] + np.random.normal(mu, sigma), 
            'XB': row['XB(m)'] + np.random.normal(mu, sigma),
            'E':  row['E(GPa)'] + np.random.normal(mu, sigma),
            'X50': row['X50(m)'] + np.random.normal(mu, sigma),
        }
        new_data.append(temp)
        print(temp)

#print(len(new_data), 'Entries of synthetically created data.')
#newdf = pd.DataFrame(new_data)
#newdf.to_excel('MBS newest dataset.xlsx', index=False)

#print(noisy_data)

#df.describe()
#noisy_data.describe()

# print(np.std(noisy_data))
# print(np.std(data))

plt.figure(figsize=(10, 5))
plt.plot(df, label='OG data', marker='o')
plt.plot(new_data, label='N data', marker='x')
plt.legend()
plt.title('comparison')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()