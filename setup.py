import os

print("""[0] pip\n[1] pip3\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("pip install slowloris")
    os.system("git pull")
elif c == "1":
    os.system("pip3 install slowloris")
    os.system("git pull")
    print("Done.")

