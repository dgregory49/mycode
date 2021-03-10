#!/usr/bin/python3

# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 # counter for fails
loginfailindex = 1
loginfailip = ""
loginsuccess = 0
# open the file for reading
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

    # loop over the file
    for line in kfile:
        # if this 'fail pattern' appears in the line...
        if "- - - - -] Authorization failed" in line:
            loginfail += 1 # this is the same as loginfail = loginfail + 1
            loginfailip += f"\t{loginfailindex}: {line.split(' ')[-1]}"
            loginfailindex += 1
        if "- - - - -] Loaded" in line:
            loginsuccess += 1

print("The number of successful logins is", loginsuccess)
print(f"The number of failed log in attempts is {loginfail}:\n"+loginfailip)
