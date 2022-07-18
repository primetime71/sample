import pandas as pd

df=pd.read_excel('sample.xlsx')



def new_sal():

        # if df['age']>=20 and df['age']<=24:
        #     updated_sal=df['new_sal']=df['sal']+df['sal']*3/100
        #     return updated_sal 

        # elif df['age']>=25 and df['age']<=28:
        #     updated_sal=df['new_sal']=df['sal']+df['sal']*6/100
        #     return updated_sal 
        
        # elif df['age']>29 and df['age']<=32:
        #     updated_sal=df['new_sal']=df['sal']+df['sal']*8/100
        #     return updated_sal 
        
        # elif df['age']>32:
        #     updated_sal=df['new_sal']=df['sal']+df['sal']*12/100
        #     return updated_sal 
        if df['age']>=20 and df['age']<=24:
            updated_sal=df['sal']+df['sal']*3/100
            return updated_sal 

        elif df['age']>=25 and df['age']<=28:
            updated_sal=df['sal']+df['sal']*6/100
            return updated_sal 
        
        elif df['age']>29 and df['age']<=32:
            updated_sal=df['sal']+df['sal']*8/100
            return updated_sal 
        
        elif df['age']>32:
            updated_sal=df['sal']+df['sal']*12/100
            return updated_sal 
      


for i in df.iterrows():
    df['new_sal']=new_sal()



print(df)
    

