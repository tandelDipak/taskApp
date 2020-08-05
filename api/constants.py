AGE_RANGE = 5
FILE_PATH = '../data/titanic.csv'
S_LABELS = ['Total', 'Male', 'Female', 'M Died',
            'M Survived', 'F Died', 'F Survived'],
S_PARENTS = ['', 'Total', 'Total', 'Male', 'Male', 'Female', 'Female']
C_LABELS = ['First Class', 'Economy Class', 'General Class']
POINTS = [{'3': {'Sex': 'male', 'Survived': 0},
           '4': {'Sex': 'male', 'Survived': 1},
           '5': {'Sex': 'female', 'Survived': 0},
           '6': {'Sex': 'female', 'Survived': 1}}]
PORT = 5005
HOST = '0.0.0.0'
