# root2sql
This program can convert data in ROOT file to a SQL table. 
You has to install 
* ROOT ([https://root.cern/](https://root.cern/))
* MySQL ([https://www.mysql.com/](https://www.mysql.com/))
in your system.

**run.sh** is the script to run this program. Usage is
```
run.sh PROCESS
```
It will find a ROOT file with **PROCESS.root** and write data to a table called **PROCESS** in database with name **test**.

It can only read data that were used in [https://arxiv.org/abs/2302.01143](https://arxiv.org/abs/2302.01143).
