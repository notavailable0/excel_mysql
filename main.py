import connect_db 
import excel_connector 

data = excel_connector.get_data_from_csv('test.csv') 
data.pop(0)

DBM = connect_db.DatabaseM() 
DBM.show_all_db()
DBM.insert_data_into_table1(data) 
DBM.show_all_data() 
DBM.close_connection()
