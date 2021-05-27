#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

# Function class average marks of each subjects
def averagemarks(sdf):
    print(df1.mean(axis = 0, skipna = True))


def studentperformance(sdf):
    physicsavg = sdf.loc[:,"PHYSICS"].mean()
    chemistryavg = sdf.loc[:,"CHEMISTRY"].mean()
    compscnavg = sdf.loc[:,"COMPUTER SCIENCE"].mean()
    mathematicsavg = sdf.loc[:,"MATHEMATICS"].mean()
    englishavg = sdf.loc[:,"ENGLISH"].mean()
   
    print("Class Topper")
    print("-----------------------------------------------------")
    print("Name :"+sdf.iloc[0][1])
    print("PHYSICS :"+str(sdf.iloc[0][2]))
    print("CHEMISTRY :"+str(sdf.iloc[0][3]))
    print("COMPUTER SCIENCE :"+str(sdf.iloc[0][4]))
    print("MATHEMATICS :"+str(sdf.iloc[0][5]))
    print("ENGLISH :"+str(sdf.iloc[0][6]))
    print("-----------------------------------------------------")
    failcount=0
    for index, row in sdf.iterrows():
        if(index !=1):
            print("-----------------------------------------------------")
            print("Name             :"+row["NAME"])
            print("PHYSICS          :"+str(row["PHYSICS"])+"|| Class Top: "+str(sdf.iloc[0][2])+" || Class Avg: "+ str(physicsavg)+"|| Percentile :"+str(np.percentile(sdf.loc[:,"PHYSICS"], index)))
            print("CHEMISTRY        :"+str(row["CHEMISTRY"])+"|| Class Top: "+str(sdf.iloc[0][3])+" || Class Avg: "+ str(chemistryavg)+"|| Percentile :"+str(np.percentile(sdf.loc[:,"CHEMISTRY"], index)))
            print("COMPUTER SCIENCE :"+str(row["COMPUTER SCIENCE"])+"|| Class Top: "+str(sdf.iloc[0][4])+"|| Class Avg: "+ str(compscnavg)+"|| Percentile :"+str(np.percentile(sdf.loc[:,"COMPUTER SCIENCE"], index)))
            print("MATHEMATICS      :"+str(row["MATHEMATICS"])+"|| Class Top: "+str(sdf.iloc[0][5])+" || Class Avg: "+ str(mathematicsavg)+"|| Percentile :"+str(np.percentile(sdf.loc[:,"MATHEMATICS"], index)))
            print("ENGLISH          :"+str(row["ENGLISH"])+"|| Class Top: "+str(sdf.iloc[0][6])+" || Class Avg: "+ str(englishavg)+"|| Percentile :"+str(np.percentile(sdf.loc[:,"ENGLISH"], index)))
            print("-----------------------------------------------------")
            if(row["GRADE"]=='F'):
                failcount=failcount+1

    Percent= ((len(sdf)-failcount)/len(sdf))*100
    failcount=0



#Read .csv file
df = pd.read_csv (r'/home/sndphs/Desktop/python project/grade_card.csv')
df1 =df

df1['Rating_Rank'] = df1['PERCENTAGE'].rank(ascending = 0)
df1 = df1.set_index('Rating_Rank') 
df1 = df1.sort_index() 
df1.pop('TOTAL')
df1.pop('PERCENTAGE')
#df1.pop('GRADE')

print (df1)
averagemarks(df1)
print("*****************************************************")
studentperformance(df1)
print("*****************************************************")



# In[8]:


df1.head()


# #  Class average marks of each subjects

# In[3]:


import matplotlib.pyplot as plt
sub=["PHY","CHEM","COMP","MATH","ENG"]
left=1,2,3,4,5
a=df1.loc[:,"PHYSICS"].mean()
b=df1.loc[:,"CHEMISTRY"].mean()
c=df1.loc[:,"COMPUTER SCIENCE"].mean()
d=df1.loc[:,"MATHEMATICS"].mean()
e=df1.loc[:,"ENGLISH"].mean()
avg=[a,b,c,d,e]
plt.title("Class avg marks of each subject")
plt.xlabel("subject")
plt.ylabel("average")
plt.bar(left,avg,tick_label=sub,width=0.8,color=['red','green','blue','yellow','black'])
plt.show()


# # Performance of the student compared with topper and average of the class

# In[5]:


val=input("enter the rank number of a student")
N=int(val)
for index, row in df1.iterrows():
    if(index ==N):
        print("Name             :"+row["NAME"])
        print("PHYSICS          :"+str(row["PHYSICS"]))
        print("CHEMISTRY        :"+str(row["CHEMISTRY"]))
        print("COMPUTER SCIENCE :"+str(row["COMPUTER SCIENCE"]))
        print("MATHEMATICS      :"+str(row["MATHEMATICS"]))
        print("ENGLISH          :"+str(row["ENGLISH"]))
        k=row["PHYSICS"]
        l=row["CHEMISTRY"]
        m=row["COMPUTER SCIENCE"]
        n=row["MATHEMATICS"]
        o=row["ENGLISH"]

f=df1.iloc[0][2]
g=df1.iloc[0][3]
h=df1.iloc[0][4]
i=df1.iloc[0][5]
j=df1.iloc[0][6]
                        
N=5
y1=[f,g,h,i,j]
y2=[k,l,m,n,o]
y3=[a,b,c,d,e]
xvalues = np.arange(N)

plt.bar(xvalues,y1,color='b', label ='Topper')
plt.bar(xvalues,y2, color='r', bottom =y1, label = 'Student')
plt.bar(xvalues,y3,color='y',label='Average')
plt.xticks(xvalues, ('PHY', 'CHEM', 'COMP', 'MATH', 'ENG'))

plt.xlabel('Topper')
plt.ylabel('Student')
plt.title('COMPARISON')
plt.legend()

plt.show()


# # Subject wise percentile of the student

# In[6]:


val=input("enter the rank number of the student")
N=int(val)
for index, row in df1.iterrows():
    if(index ==N):
        print("Name                        :"+row["NAME"])
        print("PHYSICS Percentile          :"+str(np.percentile(df1.loc[:,"PHYSICS"],index)))
        print("CHEMISTRY Percentile        :"+str(np.percentile(df1.loc[:,"CHEMISTRY"],index)))
        print("COMPUTER SCIENCE Percentile :"+str(np.percentile(df1.loc[:,"COMPUTER SCIENCE"],index)))
        print("MATHEMATICS Percentile      :"+str(np.percentile(df1.loc[:,"MATHEMATICS"],index)))
        print("ENGLISH Percentile          :"+str(np.percentile(df1.loc[:,"ENGLISH"],index)))
        p=(np.percentile(df1.loc[:,"PHYSICS"],index))
        q=(np.percentile(df1.loc[:,"CHEMISTRY"],index))
        r=(np.percentile(df1.loc[:,"COMPUTER SCIENCE"],index))
        s=(np.percentile(df1.loc[:,"MATHEMATICS"],index))
        t=(np.percentile(df1.loc[:,"ENGLISH"],index))

sub=["PHY","CHEM","COMP","MATH","ENG"]
left=1,2,3,4,5
per=[p,q,r,s,t]
plt.title("Percentile of each subject")
plt.xlabel("subject")
plt.ylabel("percentile")
plt.bar(left,avg,tick_label=sub,width=0.8,color=['green','red'])
plt.show()



# # Toppers of the class

# In[7]:


T=input("enter the number of toppers you need")
u=int(T)
df1.head(u)


# In[ ]:





# # Total pass percentage of the class
# 
# 

# In[11]:


failcount=0
for index, row in df1.iterrows():
    if(row["GRADE"]=='F'):
        failcount=failcount+1

Percent= ((len(df1)-failcount)/len(df1))*100
print("PASS Percentage: "+str(Percent))


# In[ ]:




