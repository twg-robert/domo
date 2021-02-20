from qbutils import qbtocsv

"""
Date - 02/16/2021
Developer - Robert Sutton
Email - robert@teamworksgroup.com

NOTE - This was put together to get around an issue with Domo Workbench unable to connect to Quickbooks 2019+
My first goal is to get some financial reports quick and dirty to meet immediate needs.
I will be initially creating 4 reports: P&L Detail, AR/AP Summaries & Balance Sheet.
Later I will work on this to make it more modular and push directly to domo using pydomo.
"""

"""
Refactor goals:
Add datetime for current date.
Delete previous files and/or archive
""""


file_path = "C:\\data\\qbexport\\"
dsn = "DSN=QuickBooks Data;"


# Balance Sheet Standard - This Year To Date
file_name = "balshtstdthsytd.csv"
qb_query = """
sp_report
BalanceSheetStandard
show
AccountFullName,AccountListID,AccountName,AccountNumber,AccountSpecialType,AccountType, Amount,
Label,NestedText1,NestedText2,
NestedText3,NestedText4,NestedText5,NestedText6,NestedText7,NestedText8,
NestedText9, RowData,RowDataType, RowNumber,RowType,Text
parameters DateMacro = 'ThisYearToDate',
SummarizeColumnsBy = 'TotalOnly'
"""
qbtocsv(dsn, file_path + file_name, qb_query)


# Profit and Loss Detail - This Year To Date
file_name = "prflssstdthsytd.csv"
qb_query = """
sp_report
ProfitAndLossDetail
show
Account, Account_Title, AccountFullName, AccountListID,
AccountName, AccountNumber, AccountSpecialType, AccountType, Aging, Aging_Title, Amount,
Amount_Title, BilledDate, BilledDate_Title, Blank, Class, Class_Title, ClearedStatus,
ClearedStatus_Title, Credit, Credit_Title, Date, Date_Title, Debit, Debit_Title, DeliveryDate,
DeliveryDate_Title, DueDate, DueDate_Title, EstimateActive, EstimateActive_Title, FOB,
FOB_Title, LastModifiedBy, LastModifiedBy_Title, Memo, Memo_Title, ModifiedTime, ModifiedTime_Title,
Name, Name_Title,  NumColumns, NumRows, PaidStatus, PaidStatus_Title, PaidThroughDate,
PaidThroughDate_Title, PaymentMethod, PaymentMethod_Title, PONumber, PONumber_Title, PrintStatus,
PrintStatus_Title, RefNumber, RefNumber_Title, ReportBasis, ReportSubtitle, ReportTitle, RowData,
RowDataType, RowNumber, RowType, RunningBalance, RunningBalance_Title, ShipDate, ShipDate_Title,
SourceName, SourceName_Title, SplitAccount, SplitAccount_Title, TaxLine, TaxLine_Title, Terms,
Terms_Title, Text, TxnID, TxnID_Title, TxnNumber, TxnNumber_Title, TxnType, TxnType_Title
parameters
DateMacro = 'ThisYearToDate'
"""
qbtocsv(dsn, file_path + file_name, qb_query)

# AP Aging Summary - Last Year To Date
file_name = "apagnsumlstytd.csv"
qb_query = """
sp_report
APAgingSummary
show
Amount,Current,Label,NumColTitleRows,NumColumns,NumRows,ReportBasis,ReportSubtitle,ReportTitle,
RowData,RowDataType,RowNumber,RowType
parameters DateMacro = 'LastYearToDate'
"""
qbtocsv(dsn, file_path + file_name, qb_query)

# AR Aging Summary - Last Year To Date
file_name = "aragnsumlstytd.csv"
qb_query = """
sp_report
ARAgingSummary
show
Amount,Current,Label,NumColTitleRows,NumColumns,NumRows,ReportBasis,ReportSubtitle,ReportTitle,
RowData,RowDataType,RowNumber,RowType,Text

parameters DateMacro = 'LastYearToDate'
"""
qbtocsv(dsn, file_path + file_name, qb_query)
