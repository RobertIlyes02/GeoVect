import json

def boundingBox(vector):
    vector['vector']['coordinates'] = json.loads(vector['vector']['coordinates'])
    print(vector['vector']['coordinates'])
    minx = None
    miny = None 
    maxx = None
    maxy = None
    for idx, point in enumerate(vector['vector']['coordinates']):
        if idx == 0:
            minx = point[0]
            maxx = point[0]
            miny = point[1]
            maxy = point[1]
            continue
        if point[0] < minx:
            minx = point[0]
        if point[0] > maxx:
            maxx = point[0]
        if point[1] < miny:
            miny = point[1]
        if point[1] > maxy:
            maxy = point[1]
    return {"type": "polygon", "coordinates": [[minx, miny], [maxx, miny], [maxx, maxy], [minx, maxy], [minx, miny]]}
            
            
print(boundingBox({'type': 'vector', 'vector': {'geometry': 'polygon', 'coordinates': '[[0, 0], [1,0], [1, 1], [0, 1], [0, 0]]'}}))
print(boundingBox({'type': 'vector', 'vector': {'geometry': 'Polygon', 'coordinates': '[[0, 0], [1,2], [2, 0], [0, 0]]'}}))
print(boundingBox({'type': 'vector', 'vector': {'geometry': 'line', 'coordinates': '[[0, 10], [20, 50]]'}}))
print(boundingBox({'type': 'vector', 'vector': {'geometry': 'line', 'coordinates': '[[0, 0], [1, 1], [2,2], [3,3], [4,4]]'}}))
print(boundingBox({'type': 'vector', 'vector': {'geometry': 'point', 'coordinates': '[[10, 10]]'}}))
print(boundingBox({'type': 'vector', 'vector': {'geometry': 'Line', 'coordinates': '[[-0.342, 1.9234], [12.04, -50.123], [2, 1]]'}}))
