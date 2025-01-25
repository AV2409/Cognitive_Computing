import pandas as pd

iris = pd.read_csv("/Users/akshanshvij/Desktop/GitHub/Cognitive_Computing/Assignment_3/Iris.csv")

iris.drop(index=4, inplace=True)
iris.drop(columns=iris.columns[3], inplace=True)
print(iris)