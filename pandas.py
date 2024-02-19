import pandas as pd
import csvkit

columns_threshold = 24  
id_column='ID'

# read CSV file, drop columns > columns_threshold
df = pd.read_csv('F:/Users/piotr/Downloads/System_engineer_question3.csv')
df = df.iloc[:, :columns_threshold + 1]

# remove rows where 'id' is null or NaN
#df = df.dropna(subset=[id_column], axis=1)
df = df[df['id'].notna()]



print(df)
df.to_csv('F:/Users/piotr/Downloads/System_engineer_question3v2.csv', index=False)

import csvkit

##csvsql --dialect postgresql --snifflimit 1000 --no-constraints F:/Users/piotr/Downloads/System_engineer_question3v2.csv [export columns for postgres table creation]
