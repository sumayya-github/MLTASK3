programfile= open("/t3/model.py",'r')
code = programfile.read()

if 'keras' or 'tensorflow' in code:
       if 'Conv2D' in code:
            print("ALREADY EXISTS")
       else:
            print("NOT A CNN")
else:
     print("NOT A NEURAL NETWORK")
