import os #operation systems
def  check(pat):
    all_ob = os.listdir(pat)
    files = []
    dirs = []
    for i in all_ob:
        new_path = os.path.join(pat, i)
        if os.path.isfile(new_path):
            files.append(i)
        elif os.path.isdir(new_path):
             dirs.append(i)
    
    print(f"All files in the {pat}: {files}")
    print(f"All directories in the {pat}: {dirs}")
    print(f"All content: {all_ob}")
    
pat = input("Please input a path: ")
check(pat)
