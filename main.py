import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 18 for SQL Server};"
    "Server=172.30.164.234,1433;" 
    "Database=PierwszaTestowa;"
    "UID=sa;"
    "PWD=Karate1!xpdFFaida;"
    "TrustServerCertificate=yes;"
)

## Sprawdzamy na docelowym połączenie
## Test-NetConnection -ComputerName 172.130.164.234 -Port 1433

## sprawdzamy na serwerze czy sam udostępnia port:
## netstat -an | findstr :1433
##


cursor = conn.cursor()
cursor.execute("SELECT TOP 5 * FROM [dbo].[Osoby]")
for row in cursor:
    print(row)