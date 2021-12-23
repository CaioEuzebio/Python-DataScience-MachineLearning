df_keep = pd.merge(df_keep,df_with_infos[['KEY','INFO_REQUESTED']], on='KEY',how='left').drop_duplicates().reset_index()
