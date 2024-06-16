from subprocess import Popen,PIPE


def strPopen(args):
    return Popen(args, shell=True,stdout=PIPE,text=True).stdout.read()

def nonstrPopen(args):
    return Popen(args, stdout=PIPE,stderr=PIPE)

