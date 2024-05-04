from array import array
from ROOT import TSQLServer
from treeReader import treeReader

input_filename = "PROCESS"+".root"
input_treename = "eetc"

tr = treeReader(input_filename, input_treename)
print(tr.nEvents())
tr.getDATA()

SQLFile = open("table.sql", "r")
SQLQuery = SQLFile.read()
SQLFile.close()

user = ""
password = ""
db = TSQLServer.Connect("mysql://localhost/test", user, password)
db.Query("DROP TABLE IF EXISTS PROCESS")
db.Query(SQLQuery)

for i in range(tr.nEvents()):
    tr.tree.GetEntry(i)
    query = f"INSERT INTO PROCESS VALUES (" \
        f"{tr.njets[0]}, {tr.ptj1[0]}, {tr.ptj2[0]}, {tr.enerj1[0]}, {tr.enerj2[0]}, " \
        f"{tr.mjj[0]}, {tr.mj1[0]}, {tr.mj2[0]}, {tr.hb[0]}, {tr.lb[0]}" \
        f")"
    db.Query(query)
    if i%1000 == 0:
        print("Processing "+str(i)+" events" )
    # print(ts.njets[0], ts.mj1[0], ts.mj2[0])
