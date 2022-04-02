CONSIDERACIONES

Descomprimir el archivo turtle_bot_9.zip.
Guardar la carpeta descargada (turtle_bot_9) en - /home -.
Se debe escribir el comando - sudo pip install pynput - dentro del terimanl de Ubuntu. Con este comando se instalan las librerías de pynput.

------------------------------------------------------------------------------------------------

SERIAL NODE

Se hace uso de las siguientes librerías en Python:

#include <ros.h>
#include <std_msgs/Int8.h>
#include <geometry_msgs/Vector3.h>

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

PRIMER PUNTO

Se hace uso de las siguientes librerías en Python:

from argparse import _VersionAction
from glob import glob
from tkinter.tix import TEXT
from turtle import end_fill
import rospy
import sys
import os.path
from pynput import keyboard
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
from tkinter.filedialog import asksaveasfile
from tkinter import BOTTOM, Tk,Frame,Button,Label, mainloop,ttk

Procedimiento a seguir para correr el nodo turtle_bot_teleop.py del primer punto:

1. Abrir una terminal nueva (CTRL+ATL+T) y ejecutar roscore; escribir - roscore -.
2. Abir otra terminal y escribir - cd -. Luego, ejecutar los siguientes comandos:
   2.1 - cd (workspace)/ -.
   2.2 - source devel/setup.bash -.
3. Otorgar permisos al archivo turtle_bot_teleop.py. Escribir en la terminal:
   3.1 - cd src/turtle_bot_9/scripts/ -.
   3.2 - chmod +x turtle_bot_teleop.py -.
4. Otorgar permisos al puerto USB.
   4.1 - ls -l /dev/ttyACM0 -.
   4.2 - sudo chmod +x /dev/ttyACM0 -.
5. Ejecutar el nodo de Arduino escribiendo - rosrun rosserial_python serial_node.py /dev/ttyACM0 -.
6. Ejecutar el nodo escribiendo - rosrun turtle_bot_9 turtle_bot_teleop.py -.
7. Ingresar un valor numérico para la velocidad lineal.
8. Ingresar un valor numérico para la velocidad angular.
9. Presionar las flechas Arriba, Abajo, Izquierda y Derecha en el teclado para mover el robot.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

SEGUNDO PUNTO

Se hace uso de las siguientes librerías en Python:

from turtle import width
from matplotlib.backends.backend_tkagg import(FigureCanvasTkAgg, NavigationToolbar2Tk)
from cgitb import text
from doctest import master
from fileinput import close
import threading
import rospy
from geometry_msgs.msg import Vector3
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *

Procedimiento a seguir para correr el nodo turtle_bot_interface.py del segundo punto:

1. Tener ejecutado roscore 
2. Abir otra terminal y escribir - cd -. Luego, ejecutar los siguientes comandos:
   2.1 - cd (workspace)/ -.
   2.2 - source devel/setup.bash -.
3. Otorgar permisos al archivo turtle_bot_interface.py. Escribir en la terminal:
   3.1 - cd src/turtle_bot_9/scripts/ -.
   3.2 - chmod +x turtle_bot_interface.py -.
4. Ejecutar el nodo de Arduino escribiendo - rosrun rosserial_python serial_node.py /dev/ttyACM0 -.
5. Ejecutar el nodo escribiendo - rosrun turtle_bot_9 turtle_bot_interface.py -.
6. Tener ejecutado el nodo turtle_bot_teleop.py y mover el robot.
7. En la gráfica emergente se observará en tiempo real la posición del robot y el camino recorrido por el mismo.
8. Si se desea guardar la gráfica, dar click al botón de guardar que se encuentra en la parte inferior de la interfaz. Seleccionar ruta donde se quiere guardar el archivo e, igualmente, escribir un nombre.

----------------------------------------------------------------------------------------------------------------------------------------------------------------

TERCER PUNTO

Se hace uso de las siguientes librerías en Python (las mismas del primer punto):

from argparse import _VersionAction
from glob import glob
from tkinter.tix import TEXT
from turtle import end_fill
import rospy
import sys
import os.path
from pynput import keyboard
from geometry_msgs.msg import Vector3
from std_msgs.msg import String
from tkinter.filedialog import asksaveasfile
from tkinter import BOTTOM, Tk,Frame,Button,Label, mainloop,ttk

Procedimiento a seguir para guardar el recorrido del robot:

1. Tener ejecutado el nodo turtle_bot_teleop.py.
2. Si no ha realizado movimientos con el robot, presionar las flechas Arriba, Abajo, Izquierda y Derecha en el teclado para mover el robot.
3. Presionar la tecla ESC en el teclado.
4. En la ventana emergente, dar click en el botón Click to Save y otorgarle un nombre al archivo .txt.
   4.1 Este archivo se guardará en la ruta elegida por el usuario.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

CUARTO PUNTO

Se hace uso de las siguientes librerías en Python:

from tkinter import filedialog, ttk
from unicodedata import name
from turtle_bot_9.srv import cargar_partida, cargar_partidaResponse
from queue import Empty
from turtle import end_fill
import rospy
import sys
import os.path
from pynput import keyboard
from geometry_msgs.msg import Vector3
from tkinter import*

Procedimiento a seguir para correr el nodo turtle_bot_player.py del cuarto punto:

1. Tener ejecutado roscore
2. Abir otra terminal y escribir - cd -. Luego, ejecutar los siguientes comandos:
   2.1 - cd (workspace)/ -.
   2.2 - source devel/setup.bash -.
3. Otorgar permisos al archivo turtle_bot_player.py. Escribir en la terminal:
   3.1 - cd src/turtle_bot_9/scripts/ -.
   3.2 - chmod +x turtle_bot_teleop.py -.
4. Ejecutar el nodo de Arduino escribiendo - rosrun rosserial_python serial_node.py /dev/ttyACM0 -.
5. Ejecutar el nodo escribiendo - rosrun turtle_bot_9 turtle_bot_player.py -.
6. En la ventana emergente, dar Click en el botón Open y seleccionar el archivo .txt previamente guardado (tercer punto).