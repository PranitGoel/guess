
import time
import os



 
dir = "D:/Pranit/clue guess/"

files = os.listdir(dir)

for i in files:
    count = 0
    print('Let us begin the quiz.')
    for line in open(dir+i,'r'):
        if line[0] == ' ':
            break;
        
        else:
            count+=1
                    
            if count > 1:
                print('clue:', line)
                t = time.time() + 10
                while time.time() < t: 
                    
                    guess = input('please take a guess.  ')
                
                if answer == guess :
                    print('Correct answer!Nice work, you won.') 
                    break;
                
                else:
                    print('Sorry, wrong guess.')
            else:
                answer = line.split()
                answer = answer[0]
            print('\n')
            
    print('The word I had in mind was ',answer)
    print('\n')
    contin = input('Press x to exit otherwise anything else to continue ')
    if contin == 'x':
        break;
    
            
            

