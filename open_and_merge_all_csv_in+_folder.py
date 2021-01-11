import glob

df = pd.concat(map(pd.read_csv, glob.glob('data/*.csv')))
