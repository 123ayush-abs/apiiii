import pandas as pd
import numpy as np

from flask import Flask , request, jsonify
df=pd.read_csv("new_dataset.csv")
final_input_list=[]
class KNN_Classifier():
   def __init__(self, distance_metric='euclidean'):
     self.distance_metric = distance_metric    
   def get_distance_metric(self,training_data_point, test_data_point,new_length):
     dist=0
     for i in range(new_length): 
       dist = dist + (training_data_point[i] - test_data_point[i])**2
     euclidean_dist = np.sqrt(dist)
     return euclidean_dist
   def k_nearest_neighbour(self,X_train, test_data, k,new_length): 
    distance_list = []  
    for training_data in X_train: 
      distance = self.get_distance_metric(training_data, test_data,new_length)
      distance_list.append((training_data, distance)) 
    distance_list.sort(key=lambda x: x[1]) 
    neighbors_list = []
    for j in range(k): #k nearest neighbour
      neighbors_list.append(distance_list[j][0])
    return neighbors_list   
def ff(city,diss=None):
      df=pd.read_csv("new_dataset.csv")
      df= df[df['city']== city]
      df.drop(df.columns[[0,5,6,8]], axis=1, inplace=True)
      if(diss is not None):
        final_input_list.append(diss)
      else:
            final_input_list.append(15)
      len_new=1
      arr=df.to_numpy()
      classifier=KNN_Classifier()
      res=classifier.k_nearest_neighbour(arr,final_input_list, 30,len_new)
      fin=[]
      for i in range(len(res)):
            d={}
            d["price"]=res[i][0]
            d["Distance"]=res[i][1]
            d["summaryscore"]=res[i][2]
            d["ratingband"]=res[i][3]
            d["animal_allowance"]=res[i][4]
            d["valueformoney"]=res[i][5]
            d["room_status"]=res[i][6]
            d["area"]=res[i][7]
            d["city"]=res[i][8]
            d["mobile"]=res[i][9]
           # d["PGNAME"]=res[i][10]
            fin.append(d)
      return fin


  # p1=request.args["query"]
app=Flask(__name__)
@app.route('/api',methods=["GET"])
def method_name():
    distance=15
    final_dict={}
    query=request.args.to_dict()
    print(query)
    city=query["query"]
    try:
      distance=int(query["dis"])
    except:
      distance=15
    ress=ff(city,distance)
    final_dict["data"]=ress
    return final_dict
        
 
  
if __name__=="__main__":
    app.run(debug=true)