from google.colab import files
import pandas as pd
uploaded=files.upload()

# Get the actual filename from the uploaded dictionary
filename = list(uploaded.keys())[0]

df=pd.read_excel(filename)
print(df)

print(df.shape)
print(df.columns)
print(df.info())

print(df.head(3))
print(df.tail(2))

print(df.iloc[4])
print(df.iloc[8])

print(df)
print(df.loc[2,"Brand"])
print(df.loc[3,"Product"])
print(df.loc[12,"Stock"])

print(df.iloc[4,0])
print(df.iloc[2,1])
print(df.iloc[3,3])

df_dropped=df.drop(columns=["Stock"])
print("After dropping 'Stock' Column:\n",df_dropped)

df.renamed=df.rename(columns={'price':'cost'})
print(df.renamed)

print(df)
print(df.loc[df['BestSeller']==True])
print(df.loc[df['Stock']<40])
print(df.loc[df['Price']<10000])

df_grouped=df.groupby("Brand").agg({'Price': 'mean', 'Stock': 'sum'})
print(df_grouped)

df_grouped=df.groupby('Brand').agg({'Price':['mean','max','min','sum']})
print(df_grouped)

grouped_mean=df.groupby('Brand')['Price'].mean()
print(grouped_mean)

data2={
    "Brand":["SoundMax","TechNova","ByteCore","TimeTrack","EchoBoom"],
    "Rating":[4.2,4.5,4.0,4.1,3.9],
    'discount':[28,40,16,10,5]
}
df_rating=pd.DataFrame(data2)
print(df_rating)

df_merged=df.merge(df_rating,on='Brand')
print(df_merged)

new_data={
    "Product":["Tablet"],
    "Brand":["SmartWare"],
    "Price":["12999"],
    "Stock":[25],
    "BestSeller":[True]
}
df_new=pd.DataFrame(new_data)
print(df_new)

df_concat=pd.concat([df,df_new],ignore_index=True)
print(df_concat)

df["rank"] = df["Price"].rank(ascending=False)
print(df)

print(df.sort_values(by="rank", ascending=True))
print(df.sort_values(by="rank",ascending=False))

df.pivot_table(values='Price',index="Brand",columns="Stock",aggfunc="max")

pd.crosstab(df["Brand"],df["Stock"])

