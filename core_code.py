from script import *
from tabulate import tabulate
from colored import fg



def show(cur):
    print("***************************")
    color = fg('blue')
    print (color + 'Show Variables:')
    cur.execute("show variables;")
    first = cur.fetchall()
    new_key=list(first)
    test=dict(new_key)
    variable_list=["read_only","max_connections"]
    for variable in variable_list:
        print(f"{variable} = {test.get(variable)}")

def uptime (cur):
    of_variables=["Uptime","Threads_connected"]
    for Uptime_conn in of_variables:
        cur.execute(f"SHOW STATUS WHERE `variable_name` = '{Uptime_conn}';")
        Uptime_connection = cur.fetchall()
        second=list(Uptime_connection)
        test=dict(second)
        for counter in test:
            print(f"{counter} = {test.get(counter)}")
    print("***************************")


def master(cur):
    color = fg('red')
    print (color + 'Show master status:')
    cur.execute("show master status;")
    masterstatus = cur.fetchall()
    Third=list(masterstatus)
    print(tabulate(Third, headers=["File", "Position", "Binlog_Do_DB","Binlog_Ignore_DB","Executed_Gtid_Set"]))

def slave(cur):
    try:
        print("***************************")
        color = fg('blue')
        print (color + 'Show Slave status:')
        cur.execute("show slave status;")
        first = cur.fetchmany()
        new_key=list(first)
        second=(new_key[0])
        list_of_key=["Show_Io_state","Master_Host","Master_user","Master_port","Master_Log_File","Read_Master_Log_Pos","Relay_Log_File","Relay_Log_Pos","Relay_Master_Log_File","Slave_IO_Running","Slave_SQL_Running","Master_Server_Id","Master_UUID","Slave_SQL_Running_state"]
        list_of_values=[0,1,2,3,5,6,7,8,9,10,11,39,40,44]
        for (all_key,all_value)in zip(list_of_key,list_of_values):
            print(f"{all_key}  :{second[all_value]}")
    except:
        print("It's Not Replica")
        

def top(cur):
    print("***************************")
    color = fg('white')
    print (color + 'Top 10 running list queries:')
    cur.execute("select id,USER,HOST,DB,COMMAND,TIME,STATE,SUBSTRING(INFO,1,1000000) as INFO from information_schema.processlist where COMMAND not in ('Binlog Dump', 'Sleep') order by Time desc limit 10")
    Top_processlist = cur.fetchall()
    fourth=list(Top_processlist)
    print(tabulate(fourth, headers=["id", "USER", "DB","COMMAND","TIME","INFO"]))
    print("***************************")

        
    
    


