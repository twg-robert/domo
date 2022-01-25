# Domo Python Quickbook ODBC Workbench - VERSION 1.0

Using QODBC, pypyodbc and QODBC we can easily pull reports and tables from Quickbooks.

Pre-requisites
QODBC (read-only) driver (Quickbooks Enterprise 20 includes free QODBC READ-ONLY driver).
Python 3.9 32 bit
pip3 install pypyodbc 
(tried pyodbc which I could not install due to issue with C++ 14 compiler)
pip3 install pydomo

QODBC Driver -
https://qodbc.com/qodbc-downloads/

QuickBooks Enterprise Editions are allowed to use the QODBC Desktop Read-Only version for free.

You can buy 1 license for $149 (time of this writing) or ask for oem licensing for significant discount (15 or more licenses).

The following link will give you all the reports you can add to the python reports script (copy and paste then adjust).
https://doc.qodbc.com/qodbc/20/reports/sp_report_detail.html

Since this is a 32 bit driver you must use Python 32 bit.
https://stackoverflow.com/questions/21393558/32-bit-pyodbc-reading-64-bit-access-accdb

You must check option for SQL server support.
https://support.flexquarters.com/esupport/index.php?/Knowledgebase/Article/View/2738/0/qodbc-desktop-how-to-connect-to-qodbc-using-python

After successful setup of QODBC, Python and 
Dump Quickbooks financial reports to CSV file that Domo Workbench can push to Domo instance.

pypyodbc notes 

This link shows how to connect to MsSQL DSN which I used to create the Quickbooks DSN connection 
https://code.google.com/archive/p/pypyodbc/wikis/A_HelloWorld_sample_to_access_mssql_with_python.wiki

MISC

Intuit SDK
https://developer.intuit.com/app/developer/qbdesktop/docs/get-started/download-and-install-the-sdk
