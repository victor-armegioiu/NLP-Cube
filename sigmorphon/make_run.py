import sys

input_folder = sys.argv[1]
output_folder = sys.argv[2]

from os import listdir
from os.path import isfile, join

allfiles = [f for f in listdir(input_folder) if isfile(join(input_folder, f)) and f.endswith('-covered-test')]

index = 0
total = len(allfiles)
for file in allfiles:
    model = file.replace('-covered-test', '')
    output_file = join(output_folder, model + '-high-out')
    input_file = join(input_folder, file)
    s = str(index + 1) + "/" + str(total)
    print("echo \"" + s+"\"")
    index+=1
    print("python NLP-Cube/sigmorphon/main.py --run " + input_file + " " + output_file + " models/" + model)
