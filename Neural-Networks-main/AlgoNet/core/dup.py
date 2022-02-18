import pandas as pd


df_state=pd.read_csv("ALGO-USD(1).csv")


Dup_Rows = df_state[df_state.duplicated()]

print("\n\nDuplicate Rows : \n {}".format(Dup_Rows))

DF_RM_DUP = df_state.drop_duplicates(keep=False)

print('\n\nResult DataFrame after duplicate removal :\n', DF_RM_DUP.head(n=5))
