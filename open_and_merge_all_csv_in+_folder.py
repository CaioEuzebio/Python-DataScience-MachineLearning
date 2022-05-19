#Option 1

import glob
import pandas

path = r'path'                    
all_files = glob.glob(os.path.join(path, "*.csv"))     

df_from_each_file = (pd.read_csv(f, sep=';') for f in all_files)
concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)


#Option 2 take a filename as a column and split they char

import glob
import pandas as pd

files = glob.glob(os.path.join(path, "*.csv"))     
dfs = []
for file in files:
    df = pd.read_csv(file)
    df['filename'] = file
    dfs.append(df)
df = pd.concat(dfs, ignore_index=True)
df['filename'] = df['filename'].str[44:-39]

df
