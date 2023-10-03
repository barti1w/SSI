import pandas as pd


class DatabaseReader:

    def __init__(self, type_file, data_file):
        self.file_type = type_file
        self.file_data = data_file

    file_type = 'iris-type.txt'
    data_type = pd.read_csv(file_type, sep='\t', header=None)
    types = data_type[0].tolist()

    file_data = 'iris.txt'
    data = pd.read_csv(file_data, sep='\t', header=None)
    data.columns = types

    def is_attribute(self, index):
        if self.data_type.iloc[index][1] == 's':
            return True
        else:
            return False

    def name_attribute(self, index):
        return self.data_type.iloc[index][0]

    print(data.iloc[0][2])
    print(data.iloc[1][4])


database = DatabaseReader('iris.txt', 'iris-type.txt')

for i in range(5):
    print(database.is_attribute(i))
    print(database.name_attribute(i))
