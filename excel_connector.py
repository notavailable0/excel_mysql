import pylightxl as xl

def get_data_from_csv(csv_filename):
    db = xl.readcsv(fn=csv_filename, delimiter=',', ws='sh2')
    #db.ws('sh2').rows.pop(0)
    return [(row[0], row[1], row[2], row[3]) for row in db.ws('sh2').rows]
