import pypyodbc as pyodbc
import csv

cn = pyodbc.connect('DSN=QuickBooks Data;')

"""
NOTE - This was put together to get around an issue with Domo Workbench unable to connect to Quickbooks 2019+
My first goal is to get some financial reports quick and dirty to meet immediate needs.
Later I will work on this to make it more modular and possibly replace the Domo Workbench.
Python once again saves the day!

"""

# PROFIT AND LOSS DETAIL - THIS YEAR TO DATE
cursor = cn.cursor()
cursor.execute("""
sp_report ProfitAndLossDetail show Account, Account_Title, AccountFullName, AccountListID,
AccountName, AccountNumber, AccountSpecialType, AccountType, Aging, Aging_Title, Amount,
Amount_Title, BilledDate, BilledDate_Title, Blank, Class, Class_Title, ClearedStatus,
ClearedStatus_Title, Credit, Credit_Title,  Date, Date_Title, Debit, Debit_Title, DeliveryDate,
DeliveryDate_Title, DueDate, DueDate_Title, EstimateActive, EstimateActive_Title, FOB,
FOB_Title, LastModifiedBy, LastModifiedBy_Title, Memo, Memo_Title, ModifiedTime, ModifiedTime_Title,
Name, Name_Title,  NumColumns, NumRows, PaidStatus, PaidStatus_Title, PaidThroughDate,
PaidThroughDate_Title, PaymentMethod, PaymentMethod_Title, PONumber, PONumber_Title, PrintStatus,
PrintStatus_Title, RefNumber, RefNumber_Title, ReportBasis, ReportSubtitle, ReportTitle, RowData,
RowDataType, RowNumber, RowType, RunningBalance, RunningBalance_Title, ShipDate, ShipDate_Title,
SourceName, SourceName_Title, SplitAccount, SplitAccount_Title, TaxLine, TaxLine_Title, Terms,
Terms_Title, Text, TxnID, TxnID_Title, TxnNumber, TxnNumber_Title, TxnType, TxnType_Title parameters
DateMacro = 'ThisYearToDate'""")

# FOR TESTING
#for row in cursor.fetchall():
    #print (row)
#results = cursor.fetchall()

with open(r'C:\Users\myusername\Desktop\mypldtl.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow([x[0] for x in cursor.description])  # column headings
    wr.writerows(cursor.fetchall())
cursor.close()
cn.close()
