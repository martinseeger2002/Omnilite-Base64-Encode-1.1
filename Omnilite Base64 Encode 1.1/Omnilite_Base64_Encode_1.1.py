print("Omnilite Base64 Encode 1.1")
print("Instruction:")
print("Create a folder called Omnilite Base64 Encode. Move this EXE and the file you wish to encode ")
print("into the same folder. Create and open a blank.txt file to test the command output. Run EXE")
print("follow prompts and select file to encode. Click cursor into blank.txt to test the output and time")
print("how long it takes to complete. In the folder open data.txt and omnicommands.txt compare the")
print("last command to make sure all the data is there if not manually create a token command with")
print("the remaining data and save as separate file. Open omnilite console and unlock wallet for the")
print("time it took to run the output. Make sure you have LTC to cover fees. Run exe again this time ")
print("click cursor in the console command line. enjoy\n\n")
print("If you like this program consider sending a LTC donation to the following address. \nMDUHFa18kKuCaGB3RdEHZ2GMbAAHVhgFCM\n\n\n")



token_name = input('Enter the name of new tokens to create.\n')
sending_address = input('Enter your sending address.\n')
token_url = input('Enter your url or leave blank.\n')



def base64encoding():

    from tkinter import Tk     # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename
    import base64

    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)

    with open(filename, "rb") as image2string:
        converted_string = base64.b64encode(image2string.read())
    print(converted_string)
    data = str(converted_string)[2:][:-1]
    with open('data.txt', "w+") as file:
        file.write(data)

def token_create():   
    import numpy as np
    import keyboard
    import time

    
    
    
    array_number = 0
    serial_number = 100001
    
    print('You have five second to click in the Omni console command line.')


    def base64_txt_to_array():
        global data_packet
        base64data = open('data.txt', "r")
        data = base64data.read()
        base64data.close()
        string = (data)
        n = 255
        list = [string[index : index + n] for index in range(0, len(string), n)]
        array = np.array(list)
        data_packet = (array[int(array_number)])

    def create_omni_txt():
        f = open('omnicommands.txt', 'w+')
        f.write('copy the folloing to omni console' + '\n')
        f.close()

    def add_to_omni_txt():
        f = open('omnicommands.txt', 'a+')
        f.write(omni_command)
        f.write("\n")
        f.close()

    def create_omni_command_d1():
        global omni_command_d1
        omni_command_d1 = "omni_sendissuancefixed " + '"' + sending_address + '" ' + "1 1 0 " + '"' + data_packet

    def create_omni_command_d2():
        global omni_command_d2
        omni_command_d2 = '" "' + data_packet

    def create_omni_command_d3():
        global omni_command_d3
        omni_command_d3 = '" "' + token_name + str(serial_number)[1:] + '" "' + token_url + '" "' + data_packet + '" "1"'


    create_omni_txt()

    while array_number<=9000:
        base64_txt_to_array()
        create_omni_command_d1()
        array_number=array_number+1    
        base64_txt_to_array()
        create_omni_command_d2()
        array_number=array_number+1  
        base64_txt_to_array()
        create_omni_command_d3()
        array_number=array_number+1
        serial_number=serial_number+1
        omni_command = omni_command_d1 + omni_command_d2 + omni_command_d3
        add_to_omni_txt()
        time.sleep(7)
        keyboard.write(omni_command)
        keyboard.send('enter')
    
base64encoding()
token_create()