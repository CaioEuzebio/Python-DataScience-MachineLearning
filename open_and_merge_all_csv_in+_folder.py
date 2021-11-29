import glob
import pandas

path = r'path'                    
all_files = glob.glob(os.path.join(path, "*.csv"))     

df_from_each_file = (pd.read_csv(f, sep=';') for f in all_files)
concatenated_df   = pd.concat(df_from_each_file, ignore_index=True)
