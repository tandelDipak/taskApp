API_BASE_URL = 'http://0.0.0.0:5005/api/v1/resources/titanic'
AGE_DATA = API_BASE_URL + '/ageDistribution'
BAR_DATA = API_BASE_URL + '/fare/0-5/0'
SUMMARY = API_BASE_URL + '/summary'
TITLE_STYLE = {
    'text': '<b>Age Histogram<b>',
    'y': 0.85,
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
}
SUMMARY_TITLE = {
    'text': '<b>Survival Summary<b>',
    'y': 0.85,
    'x': 0.5,
    'xanchor': 'center',
    'yanchor': 'top'
}
FONT_STYLE = {
    'family': "Courier New, monospace",
    'size': 16,
}
