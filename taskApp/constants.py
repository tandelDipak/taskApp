API_BASE_URL = 'http://0.0.0.0:5005/api/v1/resources/titanic'
AGE_DATA = API_BASE_URL + '/ageDistribution/0'
BAR_DATA = API_BASE_URL + '/fare/0-5/0/0'
SUMMARY = API_BASE_URL + '/summary'
DIED_DATA = API_BASE_URL + '/ageDistribution/3'
SURVIVED_DATA = API_BASE_URL + '/ageDistribution/4'
YAXIS_TITLE = [{'0': "<b>Passanger Count<b>",
                '1': "<b>Died Passanger Count<b>", '2': "<b>Survived Passanger Count<b>"}]
TITLE_STYLE = {
    'text': '<b>Age vs Count<b>',
    'y': 0.85,
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
}
SUMMARY_TITLE = {
    'text': '<b>Titanic Survival Summary<b>',
    'y': 0.85,
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
}
FONT_STYLE = {
    'family': "Courier New, monospace",
    'size': 16,
}
