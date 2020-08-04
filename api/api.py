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


binsArray = []
for value in bins:
    y = (lambda x: f'{x}-{x+5}')(value)
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


@app.route('/api/v1/resources/titanic/summary', methods=['GET'])
def getSummary():
    fSummary = femaleData['Survived'].value_counts()
    fSummary = fSummary.sort_index()
    mSummary = maleData['Survived'].value_counts()
    mSummary = mSummary.sort_index()
    summaryData = [fSummary.sum() + mSummary.sum(), mSummary.sum(),
                   fSummary.sum(), mSummary[0], mSummary[1], fSummary[0], fSummary[1]]
    summary = [int(value) for value in summaryData]
    labels = list(C.S_LABELS)
    parents = list(C.S_PARENTS)
    parents[0] = ''
    print(type(summaryData), type(labels), type(parents))
    return jsonify({'values': summary, 'labels': labels, 'parents': parents})


@app.route('/api/v1/resources/titanic/ageDistribution', methods=['GET'])
def getGraph1Data():
    data = {'male': {'x': binsArray, 'y': maleCounts.tolist()}, 'female': {
        'x': binsArray, 'y': femaleCounts.tolist()}}
    return jsonify(data)


@app.route('/api/v1/resources/titanic/fare/<string:ageRange>/<string:isFemale>', methods=['GET'])
def getGraph2Data(ageRange, isFemale):
    print(ageRange, isFemale)
    data, data1 = graph2(ageRange, isFemale)
    colorArray = map(lambda x: colorCoding[x], data['Embarked'].tolist())
    g2 = {'y': data['Fare'].tolist(), 'x': data['PassengerId'].tolist(), 'color': list(
        colorArray), 'labels': C.C_LABELS, 'values': data1.tolist()}
    return jsonify(g2)


app.run(host=C.HOST, port=C.PORT, debug=True, use_reloader=False)
