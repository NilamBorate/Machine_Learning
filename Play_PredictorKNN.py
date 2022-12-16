import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def MarvellousKNeighborsClassifier():
    Dataset = pd.read_csv("C:\\Users\\Admin\\Downloads\\PlayPredictor.csv")     #Load the data

    Dataset= Dataset.drop(columns="Unnamed: 0")     #Data Cleaning

    lst=[]
    for i in Dataset.columns:
        if Dataset[i].dtype=="O":
            lst.append(i)
        
    lst 

    lb=LabelEncoder()                #Data Encoding
    for i in lst:
        Dataset[i]=lb.fit_transform(Dataset[i])


    Data = Dataset.drop(["Play"],axis = 1)        
    Target = Dataset.Play   

    Data_train,Data_test,Target_train,Target_test = train_test_split(Data,Target,test_size=0.3)   #Manipulate Data

    classifier = KNeighborsClassifier(n_neighbors=3)    

    classifier.fit(Data_train ,Target_train)     #Build the model

    Predictions = classifier.predict(Data_test)  #Test the model

    Accuracy = accuracy_score(Target_test,Predictions)
    return Accuracy

   
def main():

    print("------------------------Play Predictor Case Study-----------------------")

    Ret = MarvellousKNeighborsClassifier()

    print("Accuracy of Play Predictor dataset with KNN is : ",Ret*100)


if __name__=="__main__":
    main()    