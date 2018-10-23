import json
import csv
import sys
import ijson


class Parse_Json :
    data = {}
    def __init__(self , filename):
        with open(filename) as jsonfile:
            self.data = json.load(jsonfile)

    def get_alldata(self):
        filename = "C:\\Users\\sde11\\Documents\\ProductEngg\\use-case-1.json"
        with open(filename, 'r') as f:
            objects = ijson.items(f, 'meta.view.item')
            columns = list(objects)
            print(columns)




    def get_data_byID(self,  ID):
        value = {}
        for key , val in self.data.items():
            if (str(key) == str(ID)):
                value['EmployeeID'] = key
                value.update(val)
                return value
        return

    def get_data_byIDRange(self,  fromID, toID):
        val_from_to = {}
        for key , val in self.data.items():
            if (int(key) >= int(fromID) and int(key) <= int(toID) ):
                val_from_to.update(val)
        return val_from_to

class Write_CSV:
    inputfiletype = ''

    def __init__(self , filetype):
        self.inputfiletype = filetype

    def WritetoCSV(self):
        if (self.inputfiletype == 'JSON'):
            JSONtoCSV(data, tofile)

    def JSONtoCSV(self, data, tofile):
        with open(tofile, 'w') as csv_file:
            writer = csv.DictWriter(csv_file,data.keys() )
            writer.writeheader()
            writer.writerow(data)



if __name__ == "__main__":



    json_data = Parse_Json('C:\\Users\\sde11\\Documents\\ProductEngg\\use-case-1.json')
    json_data.get_alldata()
    '''
    write_data = json_data.get_data_byID(1)
    print(write_data)

    output_csv = Write_CSV('JSON')

    output_csv.JSONtoCSV(write_data , 'C:\\Users\\sde11\\Documents\\ProductEngg\\output.csv')

    json_data.get_data_byIDRange(1,2)
    
    '''