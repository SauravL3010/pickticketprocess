from datetime import date
import os

def paths(root_path):
    '''
    root_path = takes in path where email_attachments are saved (must be r'str')
    
    all_paths = {} is a dictionary to all required directories 
    '''
    # today = date.today()

    pick_ticket_path = root_path + '\\master_pick_tickets'
    email_archive = root_path + '\\email_archive'

    all_paths = {
        'root_path' : root_path,
        'pick_ticket_path' : pick_ticket_path,
        'email_archive' : email_archive,
    }
    return all_paths



def create_directory(path):
    '''
    path = directory to create (must be r'str')
    '''
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s failed" % path)
        


def enter_directory(path):
    '''
    path = directory to enter(must be r'str')
    '''
    try: 
        os.chdir(path)
    except OSError:       
        print("Entering the directory %s failed" % path)
        
        
        
def verify_directory(path):
    '''
    path = directory to verify (must be r'str')
    '''
    return os.path.exists(path)



def move_files(src, dst):
    '''
    src = path to file (.pdf)
    dst = new path to file (.pdf)
    '''
    try:
        os.replace(src, dst)
    except:
        os.rename(src, dst)