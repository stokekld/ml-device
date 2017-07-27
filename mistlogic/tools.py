import subprocess, os, signal

def commandExe(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        return output
    except Exception as e:
        print e.message
        return False

def killProcess(name):
    try:
        pid = int(commandExe("pidof %s" % name))
    except:
        return False

    if pid == 0:
        return False

    try:
        os.kill(pid, signal.SIGKILL)
        return True
    except:
        return False
