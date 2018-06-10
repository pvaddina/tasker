from multiprocessing import Process
from subprocess import call
import subprocess
import sys
import os
import shutil

def ct_compare_to_zero_version(file_path):
    console_op = subprocess.run("cleartool describe -short " + file_path, stdout=subprocess.PIPE)
    latest_version = console_op.stdout.decode('utf-8')
    print("Got version:" + latest_version)

    index_of_ver = latest_version.rfind("\\")
    index_of_filename = latest_version.rfind("@@")

    file_branch = latest_version[0:index_of_ver]
    file_name = latest_version[0:index_of_filename]

    zero_ver = (file_branch + "\\0")

    command = "cleartool.exe diff -graphical " + zero_ver + " " + file_name
    command = command.strip()
    print_command(command)
    call(command)
    #subprocess.run(command, stdout=subprocess.PIPE)
    #do_fork(command)
    #return
    #subprocess.Popen(command, stdout=subprocess.PIPE)

def process_def(command):
    subprocess.Popen(command, stdout=subprocess.PIPE)

def do_fork(process_args):
    p = Process(target=process_def, args=(process_args,))
    p.start() 

def ct_set_cs(view_path, cs_file_location):
    foundcs = 0
    cs_path = sys.argv[3]
    for root, dirs, files in os.walk(cs_file_location):
        print("Found the followng config spec files at: " + root)
        for f in files:
            print(str(foundcs + 1) + ". " + f)
            foundcs = foundcs+1
        break;

    if foundcs >= 1:
        quitthis = ''
        while(quitthis != '-'):
            userchoicestr = input("\nPlease enter your choice:")
            try:
                userchoice = int(userchoicestr)
                if (userchoice >= 1 and userchoice <= foundcs):
                    cs = files[userchoice - 1]
                    print("You entered:" + cs)
                    setcs = get_user_input("You are about to set the configspec file: \'%s\' in the view \'%s\'. 'y'-->OK,'n'-->NOT-OK ?" % (cs, view_path[0]), ['y','n'])
                    if setcs == 'y':
                        cs_file_path = cs_file_location.strip()
                        command = "cleartool.exe setcs " + cs_file_location + "\\" + cs
                        print("Executing the command:" + command)
                        call(command)
                        input("DONE ....")
                    quitthis = '-'
                else:
                    print("Please enter numerical value in the range of (1-" + str(foundcs) + "). Or \'-\' to quit")

            except:
                if (userchoicestr == '-'):
                    quitthis = userchoicestr
                else:
                    print("Please enter numerical value in the range of (1-" + str(foundcs) + "). Or \'-\' to quit")
    else:
        input("Error!!! No config spec files found at " + cs_path)


def ct_view_files_in_branch():
    toolname = "cleartool.exe "
    branchname = input("Please enter a branch name:")
    arguments = toolname + "find . -branch \"brtype(" + branchname + ")\" -print"
    
    print_command(arguments)
    call(arguments)
    
    input ("\n\nPress enter to continue ...")

def ct_exec_command(command):
    toolname = "cleartool.exe "
    arguments = toolname + " " + command;
    
    print_command(arguments)
    call(arguments)
    
    input ("\n\nPress enter to continue ...")

def cmw_restore_backup():
    baseSwInstallPath = r"c:\Program Files (x86)\Rohde-Schwarz\CMW\3.7"
    backupRootPath = r"d:\CMW-Backup"

    resInstallations = os.listdir(backupRootPath);
    if len(resInstallations) > 0:
        print("The following backups are available at %s. Please choose one." % (backupRootPath))
        idx = 1
        for item in resInstallations:
            print("%d. %s" % (idx, item))
            idx = idx + 1

        userInput = int(get_user_int_input("Please choose one:", len(resInstallations)))

        srcRoot = backupRootPath + "\\" + resInstallations[userInput-1]
        input("\nNOTE: \"%s\" is being replaced with \"%s\". Press Enter to continue.\n" % (baseSwInstallPath, srcRoot))
        chosenBackupDirs = os.listdir(srcRoot);
        if len(chosenBackupDirs) > 1:
            for item in chosenBackupDirs:
                src = srcRoot + "\\" + item;
                dst = baseSwInstallPath + "\\" + item;
                print("%70s ==> %s" % (src, dst))
                shutil.rmtree(dst)
                shutil.copytree(src, dst, False, None)            
            input("Restore complete !!!")
        else:
            input("ERROR !! Nothing in the chosen backup. Doing nothing.")
    else:
        input("ERROR !! No backups avaialble. Doing nothing.")

def cmw_backup():
    baseSwInstallPath = r"c:\Program Files (x86)\Rohde-Schwarz\CMW\3.7"
    backupRootPath = r"d:\CMW-Backup"
    subdir = input("Enter a subdirectory (under " + backupRootPath + ") for the backup:");
    bkupDst = backupRootPath + "\\" + subdir;

    if os.path.exists(bkupDst):
        if len(os.listdir(bkupDst)) > 0:
            delDir = get_user_input("The directory is not empty. Deleting everything under " + bkupDst + ". OK ? ('y'-->Yes, 'n'-->No)", ['y','n'])
            if delDir:
                shutil.rmtree(bkupDst)
    else:
        print("Directory does not existing. Creating one ... ")
        os.makedirs(bkupDst)
    
    dirIgnoreList = ["PDB", "RS.selftest", "RS.cmwbase", "RS.3rd_Party.Debug", "Trolltech.Qt.Debug", "Docu"]
    for item in os.listdir(baseSwInstallPath):
        bkupSrc = baseSwInstallPath + "\\" + item
        dst = bkupDst + "\\" + item
        if item not in dirIgnoreList and os.path.isdir(bkupSrc):
            print("%70s ==> %s" % (bkupSrc, dst))
            shutil.copytree(bkupSrc, dst, False, None)


#######################################################################
################# HELPER Functions 
#######################################################################

def get_user_input(iStr, listAcceptableItems):
    while(True):
        userIp = input(iStr)
        if userIp in listAcceptableItems:
            return userIp

def get_user_int_input(iStr, maxitems):
    while(True):
        userInput = input(iStr)
        try:
            userInputValue = int(userInput)
            if userInputValue <= maxitems:
                return userInput;
            else:
                print("You entered an invalid value. Please a value between 1-%d" % (maxitems))
        except:
            print("You entered an invalid value. Please re-try.")


def get_dir_path(path):
    if os.path.isdir(path):
        return path
    else:
        return os.path.dirname(os.path.abspath(path))


def accept_args():
    numargs = len(sys.argv)
    isAllOK = True
    command = sys.argv[1]
    num_required_args = 3
    changeDir = True
    if command == "ct_exec_command" or command == "ct_set_cs":
        num_required_args = 4
    elif command == "cmw_backup" or command == "cmw_restore_backup":
        num_required_args = 2
        changeDir = False

    # Change to working directory to the passed argument
    if changeDir:
        workdir = get_dir_path(sys.argv[2])
        os.chdir(workdir)

    if numargs != num_required_args:
        isAllOK = False

    return isAllOK 

def do_work():
    if accept_args():
        # Execute the command as per the passed string
        command = sys.argv[1]

        if command == "ct_view_files_in_branch":
            ct_view_files_in_branch()
        elif command == "ct_exec_command":
            ct_exec_command(sys.argv[3])
        elif command == "ct_compare_to_zero_version":
            ct_compare_to_zero_version(sys.argv[2])
        elif command == "ct_set_cs":
            ct_set_cs(sys.argv[2], sys.argv[3])
        elif command == "cmw_backup":
            cmw_backup()
        elif command == "cmw_restore_backup":
            cmw_restore_backup()
        else:
            input("Wrong input. Nothing done.")
    else:
        input("Error !! Invalid number of arguments passed. Exiting ... ")

def print_command(command):
    print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print (command)
    print ("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n")
    
    
def test1():
    path = r"y:\1cm_fsw_base_wm\drivers\plugin_suu_mqtpcietest"

    for root, dirs, files in os.walk(path):
        print("\n++++++++++++++++++++++++++++++++++++++++++++++")
        print(root)
        for d in dirs:
            print("d-->" + d)

        for f in files:
            print("f-->" + f)

        break;


    
    
if __name__ == '__main__':
    try:
        do_work()
    except:
        input("UNHANDLED EXCEPTION. SOMETHING WENT WRONG.")
    #test1()

