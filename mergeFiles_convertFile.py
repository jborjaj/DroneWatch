import pandas as pd
import os

#use 'listdir()' method to return the list of entries in the specified directory
#put 'r' in front of the path file name to convert normal string to raw string 
listOfFiles = os.listdir(r"C:\Users\joelb\Desktop\CS235 Project\DAVIDE_S RFID FILES\xlxs files")

df = pd.DataFrame()

#loop through list of files and read each excel file
for i in listOfFiles:
    data = pd.read_excel(r"C:\Users\joelb\Desktop\CS235 Project\DAVIDE_S RFID FILES\xlxs files\\"+i, 'Sheet1')
    df = df.append(data)

#write all of the workbooks into one master workbook in .xlsx
df.to_excel(r"C:\Users\joelb\Desktop\CS235 Project\DAVIDE_S RFID FILES\xlxs files\rawMasterRFIDFile.xlsx", index=False)

#convert the .xlsx file into .csv
master_xlsx = pd.read_excel(r"C:\Users\joelb\Desktop\CS235 Project\DAVIDE_S RFID FILES\xlxs files\rawMasterRFIDFile.xlsx", 'Sheet1', index_col=None)
master_xlsx.to_csv(r"C:\Users\joelb\Desktop\CS235 Project\DAVIDE_S RFID FILES\xlxs files\rawMasterRFIDFile.csv", encoding='utf-8', index=False)








