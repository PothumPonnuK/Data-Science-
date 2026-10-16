class Univariate():

  def quanqual(dataset):
        qual=[]
        quan=[]
        for columnName in dataset.columns:
                    #print(columnName)
                    if (dataset[columnName].dtype=='O'):
                        #print("qual")
                        qual.append(columnName)
                    else:
                        #print("quan")
                        quan.append(columnName)
        return quan,qual  


  def frequetable(columnName,dataset):
        freqtable["Uniquevalue"]=dataset[columnName].value_counts().index
        freqtable["Frequency"]=dataset[columnName].value_counts().values
        freqtable["RelativeFrequency"]=(freqtable["Frequency"]/103)
        freqtable["cumsum"]=freqtable["RelativeFrequency"].cumsum()
        return freqtable    


   def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["Mean","Median","mode","Q1:25%","Q2:50%","Q3:75%","Q4:100%","IQR","1.5rule","Lesser","Greater","Min","Max"],columns=quan)
        for columnName in quan:
            descriptive[columnName]["Mean"]=dataset[columnName].mean()
            descriptive[columnName]["Median"]=dataset[columnName].median()
            descriptive[columnName]["mode"]=dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descriptive[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"]=descriptive[columnName]["Q3:75%"]- descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"]=1.5* descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"]=descriptive[columnName]["Q1:25%"]- descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Greater"]=descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Min"]=dataset[columnName].min()
            descriptive[columnName]["Max"]=dataset[columnName].max()
        return descriptive



     def outliers_columnName():
        lesser=[]
        greater=[]
        for columnName in quan:
            if descriptive[columnName]["Min"]<descriptive[columnName]["Lesser"]:
                lesser.append(columnName)
            if descriptive[columnName]["Max"]>descriptive[columnName]["Greater"]:
                greater.append(columnName)
        return lesser,greater        
    
          