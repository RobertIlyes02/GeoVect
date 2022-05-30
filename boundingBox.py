import json

def boundingBox(vector):
    vector['coordinates'] = json.loads(vector['coordinates'])
    print(vector['coordinates'])
    minx = None
    miny = None 
    maxx = None
    maxy = None
    for idx, point in enumerate(vector['coordinates']):
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
            
