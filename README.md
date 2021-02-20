# Domo Python Quickbook ODBC Workbench - VERSION 1.0

Using QODBC, pypyodbc and QODBC we can easily pull reports and tables from Quickbooks.

Pre-requisites
QODBC driver (Quickbooks Enterprise 20 includes free QODBC READ-ONLY driver).
Python 3.9 32 bit
pypyodbc (tried pyodbc which I could not install due to issue with C++ 14 compiler)

QODBC Driver notes

QuickBooks Enterprise Edition 2020 includes a free copy of the QODBC Desktop Read-Only Edition in the package. 

If you wish to use the advanced features of the QODBC Read/Write Edition to save data into QuickBooks, or our Server Edition for use on Web Servers and Data Servers fees may apply.

To install in QuickBooks Enterprise, here's how:
Go to the File menu.
Choose Utilities.
Select Setup ODBC, then click download and install the ODBC driver.

The following link will give you all the reports you can add to the reports script.
https://doc.qodbc.com/qodbc/20/reports/sp_report_detail.html

Since this is a 32 bit driver you must use Python 32 bit.
https://stackoverflow.com/questions/21393558/32-bit-pyodbc-reading-64-bit-access-accdb

You must check option for SQL server support.
https://support.flexquarters.com/esupport/index.php?/Knowledgebase/Article/View/2738/0/qodbc-desktop-how-to-connect-to-qodbc-using-python

Objectives
Dump Quickbooks financial reports to CSV file that Domo Workbench can push to Domo instance.

pypyodbc notes 

This link shows how to connect to MsSQL DSN which I used to create the Quickbooks DSN connection 
https://code.google.com/archive/p/pypyodbc/wikis/A_HelloWorld_sample_to_access_mssql_with_python.wiki


MISC

Intuit SDK
https://developer.intuit.com/app/developer/qbdesktop/docs/get-started/download-and-install-the-sdk
