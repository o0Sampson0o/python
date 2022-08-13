import pandas as pd
import builtins
import os
import sys

prefix = "~~"


######################################## reading activities from csv


file = "task.csv"
df = pd.read_csv(file)
df = df.dropna(how='all')
df.to_csv(file, mode='w', index=False, header=True)


############################################### function definition


def reformat(Date):
    if "/" in Date:
        pass

def list_task():
    global df
    print(df.to_string())

def add():
    global df
    Title = input(f"{prefix}Title: ")
    Description = input(f"{prefix}Description: ")
    Location = input(f"{prefix}Location: ")
    Date = input(f"{prefix}Date: ")
    Time = input(f"{prefix}Time: ")
    data = {
        'Title': [Title],
        'Description': [Description],
        'Location': [Location],
        'Date' : [reformat(Date)],
        'Time': [Time]
    }
    sub_df = pd.DataFrame(data)
    sub_df.to_csv(file, mode='a', index=False, header=False)
    df = pd.read_csv(file)
    df.reindex()

def remove():
    global df
    id = input("id: ") 
    df.drop(index = id, axis = 0, inplace = True)
    df.to_csv(file, mode='w', index=False)
    df = pd.read_csv(file)
    df.reindex()

def edit():
    index = int(input("id: "))
    print(df.loc[index])
    head = input("Select which to change: ")
    value = input("CHange to: ")
    df.loc[index, head] = value;
    df.to_csv(file, mode='w', index=False)


def help():
    print(
'''
help
exit
list
add
remove
cls
edit
'''
    )



print(
'''    
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

░██████╗░█████╗░███████╗██████╗░██╗░░░██╗██╗░░░░░███████╗  ███████╗██████╗░██╗████████╗░█████╗░██████╗░
██╔════╝██╔══██╗██╔════╝██╔══██╗██║░░░██║██║░░░░░██╔════╝  ██╔════╝██╔══██╗██║╚══██╔══╝██╔══██╗██╔══██╗
╚█████╗░██║░░╚═╝█████╗░░██║░░██║██║░░░██║██║░░░░░█████╗░░  █████╗░░██║░░██║██║░░░██║░░░██║░░██║██████╔╝
░╚═══██╗██║░░██╗██╔══╝░░██║░░██║██║░░░██║██║░░░░░██╔══╝░░  ██╔══╝░░██║░░██║██║░░░██║░░░██║░░██║██╔══██╗
██████╔╝╚█████╔╝███████╗██████╔╝╚██████╔╝███████╗███████╗  ███████╗██████╔╝██║░░░██║░░░╚█████╔╝██║░░██║
╚═════╝░░╚════╝░╚══════╝╚═════╝░░╚═════╝░╚══════╝╚══════╝  ╚══════╝╚═════╝░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
'''
)


######################################################################


while True:
    command = input(prefix)
    if command == "list":
        list_task()
    elif command == "exit":
        sys.exit(0)
    elif command == "add":
        add()
    elif command == "del":
        remove()
    elif command == 'edit':
        edit()
    else:
        try:
            os.system(command)
        except:
            pass
