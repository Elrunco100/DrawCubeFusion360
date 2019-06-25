#Author-Rubén Jordan
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

#Dimension of the edges in the cube, units in cm
edges = .2

#Definir los objetos de costruccion de aplicacion
app = adsk.core.Application.get()
ui  = app.userInterface

#Definir la fucnion de construccion
def buildCube():
    ui.messageBox('Success')

#Definir la funcion de inicio al correr la aplicacion
def run(context):
    try:
        buildCube()
    except:
        if ui:
            ui.messageBox('Failed')
