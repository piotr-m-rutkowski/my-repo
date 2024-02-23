import pandas as pd
import csv

def pp(a):
    print('######')
    print(a)

def pp2(vnam):
    for name, value in globals().items():
        if value is vnam:
           print("###",name,": \n",value)
           break

def nnn(nnn):
    for name, value in globals().items():
        if value is nnn:
            print(name)          

def cycler(mmm):
    for name, value in globals().items():
        if 1==1:
            print(name,value,mmm)
            break
            
#list of lists
a = [[1,2,3],["a","b","c"],[4,5,6,7]] 

a1=[1,2,3]
a2=["b","c","d"]
a3=[4,5,6]
az=[a1,a2,a3]

#dictionary of lists
b = {'A':[1,2,3],'B':["a","b","c"],'C':[4,5,6]}

path_csv = r'F:\Users\piotr\Downloads\test1.csv'
path_excel = r'F:\Users\piotr\Downloads\test1.xlsx'

#path.replace('\\','/')

df=pd.read_csv(path_csv)
df2=pd.DataFrame(a)
df3=pd.DataFrame(b)
df4=pd.DataFrame(az)

pp2(a)
pp2(df)
pp2(df2)
pp2(path_csv)
pp2(b)
pp2(df3)
print(df4)
nnn(df4)
cycler(df4)
