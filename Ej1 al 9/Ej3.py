jupyter_info = """ JupyterLab is a web-based interactive development
environment for Jupyter notebooks, code, and data. JupyterLab is
flexible: configure and arrange the user interface to support a wide
range of workflows in data science, scientific computing, and machine
learning. JupyterLab is extensible and modular: write plugins that add
new components and integrate with existing ones. """

letter = input('Ingrese letra: ')
if not letter.isalpha():
    print ('Caracter incorrecto.')
else:
    words = jupyter_info.split(' ')

    for word in words:
        if (letter in word):
            print (word)
    
