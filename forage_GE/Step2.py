import pandas as pd
df1 = pd.read_excel("GE_Dataset_ Task1.xlsx",sheet_name="av_engine_data_aic_psql")
df2 = pd.read_excel("GE_Dataset_ Task1.xlsx",sheet_name="av_engine_data_axm_psql")
df3 = pd.read_excel("GE_Dataset_ Task1.xlsx",sheet_name="av_engine_data_pgt_psql")
df4 = pd.read_excel("GE_Dataset_ Task1.xlsx",sheet_name="av_engine_data_fron_psql")
#print([column for column in df1])
#print([column for column in df2])
#print([column for column in df3])
#print([column for column in df4])
a = df1['esn']
b = df2['esn']
c = df3['esn']
d = df4['esn']
a.tolist()
b.tolist()
c.tolist()
d.tolist()
#df = pd.concat([df1,df2,df3,df4],axis=1,join_axes=[df1["esn"]])
df = [df1,df2,df3,df4]
result = pd.concat(df)
print(result)
result.to_excel("test.xlsx")
