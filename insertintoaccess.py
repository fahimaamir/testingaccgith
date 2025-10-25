import streamlit as st
import pyodbc
import pandas as pd
#r'DBQ=C:\iqra\mfa.accdb;'
# Define the connection string for MS Access
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ= mdn/mfa.accdb;'
)

# Connect to the database
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# Fetch data from the MS Access table
query = "SELECT * FROM Payments"
dataf = pd.read_sql(query, conn)
#dataf1 = dataf['Payment_ID']+11



#df = pd.DataFrame(data)
st.write(dataf)
i_want_to_multiply = 20
#dataf['Payment_ID'] = dataf['Payment_ID'] * i_want_to_multiply

#print("Updated DataFrame:")
#print(dataf)

# Prepare the DataFrame rows for insertion
#rows = [tuple(x) for x in dataf.values]

# Prepare an INSERT query with placeholders for each column
# Assuming Payments table has 4 columns as an example
#insert_query = "INSERT INTO Payments (Payment_ID , Entity_ID , Gross_Pay ,Payment_Date) VALUES (?, ?, ?, ?)"

insert_query = "INSERT INTO Payments (Gross_Pay ) VALUES (2000)"

# Insert each row into the table
#for row in rows:
#    cursor.execute(insert_query, row)
cursor.execute(insert_query)

# Commit the transaction
conn.commit()
st.header("Muhammad is the Best in all over the universes")
# Close the connection
cursor.close()
conn.close()