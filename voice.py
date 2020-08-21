import os
import time

pc = "Voice:"
print("#Use 'open App-name' for open application , 'exit ' for Exit\n")
time.sleep(.5)
print(pc,"Hello ") 
time.sleep(1.5) 
print(pc,"What Can I Open For You\n")



while 'True':
    time.sleep(1)
    you = input("\nUser: ")
    you = you.split()
    

    if ('open' or 'run') in you:
        time.sleep(2)
        app_name = "Start "+you[1] 
        
        rt = os.system(app_name)
        time.sleep(1)
        if rt == 0:
            
            print(pc,"Opening ",you[1], "....")
            time.sleep(1)
            print(pc,"Opened successfully",you[1]," :-)\n")

        else:
            
            print(pc,"Failed to open",you[1],":-(\n")




    elif ('exit' or 'quit') in you:
        time.sleep(1)
        print(pc,"Closing...")
        time.sleep(1)
        print(pc,"Byee! Thank You For Choosing Me, Have A Good Day :-)")
        break;
        

    else:
        time.sleep(.5)
        print(pc,"Unknown command")


# In[ ]:




