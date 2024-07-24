#learning pandas session in leet
#1. create dataframe from a list
#link - https://leetcode.com/problems/create-a-dataframe-from-list/description/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata
import pandas as pd
student_data= [[1,15],[2,11],[3,11],[4,20]]

def createDataframe(list):
    return pd.DataFrame(list,columns=['student_id','age'])

print(createDataframe(student_data))

#2.Get the size of a dataframe
import pandas as pd


def getDataframeSize(players: pd.DataFrame) -> List[int]:
    x=len(players.columns)
    y=len(players)
    return [y,x]

#or- Best solution
def getDataframeSize_best(players: pd.DataFrame) -> List[int]:
    row,col = players.shape
    return [row,col]

#3.get the first 3 rows
from pandas import DataFrame
def selectFirstRows(employees: DataFrame) -> DataFrame:
    return employees.head(3)
