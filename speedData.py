import subprocess
main = "speedtest.py --json"
rc,out= subprocess.getstatusoutput(main)
print (rc)
print (out)