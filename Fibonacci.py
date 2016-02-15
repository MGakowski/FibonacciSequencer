@@ -0,0 +1,37 @@
__author__ = 'Cyph3r (Matthew Gakowski)'
__copyright__ = "Copyright 2016, FibonacciSequencer"
__credits__ = ["Matthew Gakowski"]
__license__ = "GPL v3.0"
__version__ = "1.0"
__maintainer__ = "Matthew Gakowski"
__email__ = "mgakowski@gmail.com"
__status__ = "Production"

a = 0
b = 1
c = 0

while True:
    save = str(input("Save to text file? "))

    if save in ('y', 'yes', 'Yes', 'Y', 'YES'):
        name = str(input("Filename: "))
        text_file = open(name+".txt", "w")
        limit = int(input("Fibonacci #limit? "))

        while a <= limit:
            text_file.write(str(a)+"\n")
            c = a+b
            a = b
            b = c
        text_file.close()

    else:
        limit = int(input("Fibonacci #limit? "))

        while a <= limit:
            print(a)
            c = a+b
            a = b
            b = c
