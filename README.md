# Domo Python Quickbook ODBC Workbench - VERSION 0.1

Using pypyodbc and QODBC we can easily pull reports and tables from Quickbooks.

Pre-requisites
QODBC driver (Quickbooks Enterprise 20 includes free QODBC READ-ONLY driver).
Python 3.9 32 bit
pypyodbc

QODBC Driver notes

The following link will give you all the reports you can add to the reports script.
https://doc.qodbc.com/qodbc/20/reports/sp_report_detail.html

Since this is a 32 bit driver you must use Python 32 bit.
You must check option for SQL server support.

Objectives
Dump Quickbooks financial reports to CSV file that Domo Workbench can push to Domo instance.

