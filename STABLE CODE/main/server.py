from main import main 
import os
from excelMod import lst_unupdated_exl, excel
from pathMod import enter_directory

# import threading

# def printit():
#     threading.Timer(5.0, printit).start()
#     main()

#     excel()

# printit()


import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(sc):
    try: 
        main()
        excel()
    except Exception as e:
        print(f"Sorry, some other error has occured {e}") 
    s.enter(5, 1, do_something, (sc,))

s.enter(5, 1, do_something, (s,))
s.run()