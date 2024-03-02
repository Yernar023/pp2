import os

path=r"C:\Users\User\Desktop\githowto\repositories\work\pp2\Lab6\\dir and files"
os.chdir(path)

copy_from="z_From.txt"
copy_to="z_To.txt"
with open(copy_from, 'r') as f:
    with open(copy_to, 'w') as t:
        for line in f:
            t.write(line)
        t.close()
    f.close()