import flask
from flask import request, jsonify
import pandas as pd
import numpy as np
import math
import constants as C


titanicData = pd.read_csv(C.FILE_PATH)
upperLimit = math.ceil(titanicData['Age'].max()/C.AGE_RANGE)*C.AGE_RANGE
maleData = titanicData[titanicData['Sex'] == 'male']
femaleData = titanicData[titanicData['Sex'] == 'female']
maleCounts, bins = np.histogram(
    maleData.Age, bins=range(0, upperLimit + C.AGE_RANGE, C.AGE_RANGE))
femaleCounts, bins = np.histogram(
    femaleData.Age, bins=range(0, upperLimit + C.AGE_RANGE, C.AGE_RANGE))


def binsValue(x): return f'{x}-{x+5}'


binsArray = []
for value in bins:
    y = binsValue(value)
    binsArray.append(y)


colorCoding = {}
for index, value in enumerate(titanicData['Embarked'].unique()):
    colorCoding[value] = index


def graph2(ageRange, isFemale):
    lowerAge = int(ageRange.split('-')[0])
    upperAge = int(ageRange.split('-')[1])
    if isFemale:
        data = femaleData[(femaleData['Age'] >= lowerAge) &
                          (femaleData['Age'] < upperAge)]
    else:
        data = maleData[(maleData['Age'] >= lowerAge) &
                        (maleData['Age'] < upperAge)]
    classCount = data.Pclass.value_counts()
    classCount = classCount.sort_index()
    return data, classCount


app = flask.Flask(__name__)
#app.config["DEBUG"] = True


@app.route('/api/v1/resources/graph1', methods=['GET'])
def getGraph1Data():
    # return jsonify({})
    data = {'male': {'x': binsArray, 'y': maleCounts.tolist()}, 'female': {
        'x': binsArray, 'y': femaleCounts.tolist()}}
    return jsonify(data)


@app.route('/api/v1/resources/graph2/<string:ageRange>/<string:isFemale>', methods=['GET'])
def getGraph2Data(ageRange, isFemale):
    print(ageRange, isFemale)
    data, data1 = graph2(ageRange, isFemale)
    colorArray = map(lambda x: colorCoding[x], data['Embarked'].tolist())
    g2 = {'y': data['Fare'].tolist(), 'x': data['PassengerId'].tolist(), 'color': list(
        colorArray), 'labels': ['First Class', 'Economy Class', 'General Class'], 'values': data1.tolist()}
    return jsonify(g2)


app.run(host='0.0.0.0', port=5005, debug=True, use_reloader=False)
