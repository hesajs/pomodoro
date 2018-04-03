import time
import os

print('Study for 25 min')

#Current time 
start = time.time()

#End time, that is 25 min
end_time = (start+1500)
    

while True:
    if(end_time <= start):
        
        #just a notification for the completion of study
        os.system('vlc  /home/youxin/Music/pomo-iron-man.mp3')
        
        #cleanig the terminal screen
        os.system('clear')

        print('Break Time!')
        
        #asking user to continue
        user_input = input('Do you want to continue? (Y/n)')
        #changing the input to lowercase
        user_input = user_input.lower()
    
        if (user_input=='y' or user_input=='yes'):
            start = time.time()
            end_time = (start+1500)
        else:
            print('Program terminated!')
            break
    start = time.time()
        
