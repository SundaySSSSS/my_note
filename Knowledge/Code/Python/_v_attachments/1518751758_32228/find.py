
in_file = "2017_07_08.log"
f_read = open(in_file, 'r')
lines = f_read.readlines()
isFoundUp = False
isFoundDown = False
for line in lines:
    if (line.strip().find(r"CheckCollisionInput: collision Loop Up") >= 0):
        isFoundUp = True
        continue
    if (line.strip().find(r"CheckCollisionInput: collision Loop Down") >= 0):
        isFoundDown = True
        continue
    if (line.strip().find(r"ProcessColiLoop: In") >= 0):
        if (isFoundUp == True or isFoundDown == True):
            pass;   #right
        else:
            print line
    if (line.strip().find(r"ProcessColiLoop: Out") >= 0):
        isFoundUp = False
        isFoundDown = False
        
    
f_read.close()
