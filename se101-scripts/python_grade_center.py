import os
import re
import getpass
course_name = "se101"

dir_txts = "./txts"
dir_repos = "./repos"

def start():
    pswd = getpass.getpass("Enter password: ")
    #gather the list of git repositories
    regex = re.compile(r"(https://[^\s]*[@]?)(bitbucket.org/[^\s]*)")
    list_of_git_strings = []
    for sub_root, sub_dir, sub_files in os.walk(dir_txts):
        for leaf_file in sub_files:
            with open( "%s/%s" % (dir_txts, leaf_file) ) as f:
                for line in f:
                    result = regex.search(line)
                    if result != None:
                        list_of_git_strings.append(r"https://nppotdar:%s@"%pswd + result.groups()[1])

    #obtained a list of git repos, now need to pull em
    os.chdir( dir_repos )
    for git_repo in list_of_git_strings:
        regex = re.compile(r"https://nppotdar:" + pswd+ "@bitbucket.org/([^/]*)/[^\s]*")
        print git_repo
        user_string = regex.search(git_repo).groups()[0]
        os.system( "mkdir %s" % (user_string) )
        os.chdir(user_string)
        os.system( "git init" )
        os.system( "git remote add origin %s" % git_repo )
        os.system( "git fetch" )
        os.system( "git pull origin master" )
        os.chdir( ".." )

    os.chdir("..")

    #cloned all repos, now go through the dirs, open each .java file
    #generate a dictionary mapping the user to the .java files
    dict_user_to_files = {}
    for sub_root, sub_dir, sub_files in os.walk(dir_repos):
        for sub_sub_dir in sub_dir:
            list_of_files_for_user = []
            iterate_dirs(sub_root, sub_sub_dir, list_of_files_for_user)
            dict_user_to_files[sub_sub_dir] = list_of_files_for_user
        break
    print dict_user_to_files
    
    #use case program for selecting which user to assess
    while True:
        os.system("clear")
        for username in dict_user_to_files:
            print username + ( " [%s]" % len(dict_user_to_files[username]) )
            
        print "\nChoose Amigos!:"
        choice = raw_input()
        if choice == "exit":
            break
        if choice == "commit":
            for username in dict_user_to_files:
                os.chdir(r"%s/%s" % (dir_repos, username) )
                os.system(r"git add ." )
                os.system(r"git commit -m 'Nagesh reviewed your code'")
                os.system(r"git push origin master")
                print ("push success: %s" % username)
                os.chdir(r"../..")
            os.system("pause")
        
        if not choice in dict_user_to_files:
            print "here"
            continue
        for file_loc in dict_user_to_files[choice]: 
            os.system( r"xdg-open %s &" % file_loc )
        


def iterate_dirs(root, dir_name, list_of_files):
    if dir_name == ".git":
        return
    for sub_root, sub_dirs, sub_files in os.walk(root + "/" +dir_name):        
        if len(sub_dirs) == 0:
            return
        for sub_file in sub_files:
            if ".java" in sub_file:
                list_of_files.append(sub_root + "/" + sub_file)
        for sub_dir in sub_dirs:
            iterate_dirs(root + "/" + sub_root, sub_dir, list_of_files)
                        
start()
