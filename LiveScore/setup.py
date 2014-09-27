from distutils.core import setup
import py2exe

setup(name="LiveScore Futbol",
version="0.1",
description="Obtencion de los resultatos de los partidos de futbol de las ligas en el mundo",
author="Jose Andres Hernandez Bustio",
author_email="jose@icrt.cu",
license="GPL",
scripts=["main.py"],
windows=['main.py'], 
options={"py2exe": {"includes": ["sip", "PyQt4.QtGui"]}}
)