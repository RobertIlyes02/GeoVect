# GeoVect
A simple HTTP API built entirely on cloud computing services that allows for simple storing, manipulation and analysis of vector data.

**Attention**
Due to a low budget, the services may be offline. All the documentation for the processes are available here.

## API Functionality Reference

### postPoly
https://9eplbc3aqh.execute-api.us-east-2.amazonaws.com/postPoly
Takes input and stores it in our database. You will be given an access key in return.
**Input**
  - geometry (string): vector geometry type.
     - one of ['point', 'line', 'polygon']
  - coordinates (list): list of coordinate pairs [[X, Y]]
 
**Examples:**

https://9eplbc3aqh.execute-api.us-east-2.amazonaws.com/postPoly?geometry=line&coordinates=[[-45.2,12], [23.3342,-24.1241], [1.0234,-21.23], [23.11,11.234]]

https://9eplbc3aqh.execute-api.us-east-2.amazonaws.com/postPoly?geometry=point&coordinates=[3,1]

https://9eplbc3aqh.execute-api.us-east-2.amazonaws.com/postPoly?geometry=polygon&coordinates=[[0,1],[0,0],[1,0],[1,1],[0,1]]



![image](https://user-images.githubusercontent.com/66189148/167224359-c1067499-1fa4-40af-a396-a559ee080b8c.png)
