import os
import optparse
import subprocess
from subprocess import STDOUT

parser = optparse.OptionParser()
parser.add_option('-p', '--package', dest='packagename', help='Enter the package name you want to install')

(options, args) = parser.parse_args()

if options.packagename is None:
    options.packagename = raw_input('Please enter the package name you want to install:')


try:
    subprocess.check_call('sudo apt-get install -y ' + options.packagename, stderr=STDOUT, shell=True)
except subprocess.CalledProcessError:
    print "No package named",options.packagename,"found"
