﻿Bienvenido al recoendador de carreras!


Este es un programa sencillo que recomienda carreras a personas que aun no se han desidido, basado en cuatro simples preguntas.

El codigo está escrito en Python y usa Neo4J para crear enlaces con todo.

Hay dos cosas necesarias que debes tener para correr el programa.

1. PyCharm  Puedes descargarlo aquí: https://www.jetbrains.com/pycharm/download/#section=windows
2. Neo4J Puedes descargarlo aquí:https://neo4j.com/download/


Escribe Python en el buscador de Windows y al darle click derecho nos aparecera "Go to folder"  

3. Haga clic en la ruta del archivo en la parte superior de la ventana y cópiel
4. Siga este tutorial: https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/
5. En el último paso, pegue la dirección que obtuvimos en el paso número 3
6. Presione Windows + R en su teclado, escriba "cmd" y presione enter
7. Escriba "python -m pip install Tkinter", presione Entrar y espere a que finalice la instalación
8. Escribe "python -m pip install neo4j", presiona Enter y espera a que finalice la instalación
9. Cerrar el cmd, hemos terminado con él.
Ahora, en Neo4J
1. Haga clic en "Agregar gráfico" y seleccione "Crear gráfico local"
2. Espere a que se cree y haga clic en "Inicio"
3. Haga clic en "Administrar" y "Abrir en el navegador"
4. Escribe ": server connect" en la parte superior de la ventana
5. Asegúrese de que la URL sea: // localhost: 7687
6. Si es así, salta a la línea 11.
7. Si no, vamos a tomar un pequeño desvío.
8. Ir a la carpeta: AED_Proyecto
9. Abra el archivo DBMain.py con su editor de texto favorito (le recomendamos el Bloc de notas ++)
10. Cambie la línea 7 para que coincida con la URL de la línea 5
11. presiona enter
12. Copia los contenidos del archivo DataBase.txt.
13. Pégalos en la línea en la parte superior de la ventana
14. Haga clic en ejecutar
15. Espera a que se termine y minimiza Neo4J.
Ahora, vamos a ejecutar el programa!
1. Abra su PyCharm y abra los programas DBMain.py, Database.py y Career.py 
2. Ahora agregaremos los interpretes nesesarios para que pueda correr el programa, primero nos vamos a file en la esquina superior izquierda
3. Buscamos Settings y ahí agregamos los packages con el + que está alapar del last version
4. Agregaremos neo4j,neobolt,neotime,pip, pytz,setuptools y six y le damos aplicar.
5. luego de eso si no ha pasado nada guarde el proyecto y reinicie PyCharm.
6. A este punto solo queda correr el programa y contestar la encuesta en ella.