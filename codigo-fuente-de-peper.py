# -*- coding: utf-8 -*-
import qi
import argparse
import sys
import almath
import math
import motion
import time
import webbrowser
import os

# Conectar sesión con Pepper
session = qi.Session()
session.connect("tcp://192.168.0.106:9559")

# Servicios de Pepper
navigation_service = session.service("ALNavigation")
motion_service = session.service("ALMotion")
posture_service = session.service("ALRobotPosture")
audio_service = session.service("ALAudioDevice")
system_service = session.service("ALSystem")
tablet_service = session.service("ALTabletService")
animation_player_service = session.service("ALAnimationPlayer")
animated_speech_service = session.service("ALAnimatedSpeech")
behavior_service = session.service("ALBehaviorManager")
audio_player_service = session.service("ALAudioPlayer")

a = 1
while a == 1:
    # Presentacion
    tablet_service.showImage("http://198.18.0.1/apps/usta/Logo.jpg")
    animated_speech_service.say("Hola a todos, soy Pepper, y quiero que todos conozcan diversos temas en tendencia que estan asociados a la ingenieria electronica")
    time.sleep(2)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Logo.jpg")
    animated_speech_service.say("En esta presentacion expondre acerca de 3 temas importantes, primero Agentes Autónomos de IA, segundo Fotonica Integrada en los sistemas digitales y por ultimo organos en Chip") 
    time.sleep(2)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen1.jpg")
    animated_speech_service.say("Introduccion, Un agente autonomo de IA es un sistema capaz de tomar decisiones y actuar por sí mismo para cumplir un objetivo, Funciona de manera independiente, percibiendo su entorno y respondiendo a cambios sin necesidad de intervención constante de un humano")
    time.sleep(2)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen1.jpg")
    animated_speech_service.say("Como funciona, Percepcion: Recibe informacion del entorno mediante sensores o datos digitales, Procesamiento, Analiza la informacion usando algoritmos de inteligencia artificial, aprendizaje automatico o reglas de decision, Accion, Realiza actividades que afectan al entorno, como mover un robot, enviar mensajes, controlar sistemas o tomar decisiones")
    time.sleep(2)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Logo.jpg")
    animated_speech_service.say("Caracteristicas principales, Autonomia, Puede operar sin supervision constante, Adaptabilidad, Aprende de experiencias pasadas y se ajusta a cambios en el entorno, Proactividad, No solo reacciona, sino que planifica y actua para alcanzar objetivos. Interactividad, Puede comunicarse con otros agentes o personas segun sea necesario")
    time.sleep(2)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Logo.jpg")
    animated_speech_service.say("Aplicaciones, Robotica, Robots de servicio, exploracion o fabricacion, Vehiculos autonomos, Coches que conducen solos y drones inteligentes, Asistentes virtuales, Sistemas como Alexa, Siri o Pepper, Gestion inteligente: Control de trafico, domotica y sistemas de logistica")  
    time.sleep(2)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen1.jpg")
    animated_speech_service.say("Ventajas, Aumentan la eficiencia y productividad, Reducen errores humanos, Permiten tomar decisiones rapidas en entornos complejos")
    time.sleep(2)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen1.jpg")
    animated_speech_service.say("Desafios, Seguridad y control etico de las decisiones autonomas, Limitaciones en entornos muy impredecibles, Integracion con sistemas existentes y humanos")
    time.sleep(4)

    # Presentacion: Fotonica Integrada
    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen4.jpg")
    animated_speech_service.say("Hola a todos. Mi cerebro es electronico pero el futuro de la tecnologia es la luz. Hoy les hablare de la Fotonica Integrada.")
    time.sleep(3)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen5.jpg")
    animated_speech_service.say("El problema es que los electrones en los chips son lentos y se calientan demasiado.")
    time.sleep(3)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen5.jpg")  
    animated_speech_service.say("La solucion es usar luz o fotones en lugar de electrones. Chips que guian la luz como si fueran cables microscopicos.")
    time.sleep(3)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen6.jpg")
    animated_speech_service.say("Las ventajas son enormes. Velocidad extrema se transmiten terabits de informacion por segundo. Eficiencia energetica consumen menos energia y se calientan mucho menos.")
    time.sleep(4)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen7.jpg")
    animated_speech_service.say("Donde se usa. Esta tecnologia es la heroina desconocida de internet. Hace posible que naveguemos en la nube veamos videos en streaming y que exista la inteligencia artificial. Conecta los servidores del mundo a velocidades increibles.")
    time.sleep(4)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen8.jpg")
    animated_speech_service.say("Y el futuro es aun mas brillante. La fotonica integrada sera crucial para la inteligencia artificial avanzada los vehiculos autonomos con sensores LIDAR y las redes de comunicacion seis G.")
    time.sleep(4)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen9.jpg")
    animated_speech_service.say("En resumen la fotonica integrada ilumina el camino hacia un mundo digital mas rapido eficiente y conectado. Gracias por su atencion.")
    time.sleep(3)

    # Presentacion: Organos en chip
    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen2.jpg")
    animated_speech_service.say("Los organos en chip representan una de las innovaciones mas importantes en la bioingenieria actual. Se trata de pequenos dispositivos del tamano de un USB que utilizan celulas humanas y sistemas microfluidicos para imitar funciones esenciales de organos como el pulmon el higado o el corazon.")
    time.sleep(3)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen2.jpg")
    animated_speech_service.say("Estos chips son el resultado de la bioingenieria de precision ya que permiten recrear condiciones muy similares a las del cuerpo humano. Desde el flujo de liquidos y nutrientes hasta estimulos mecanicos como la respiracion o los latidos del corazon.")
    time.sleep(3)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen3.jpg")
    animated_speech_service.say("Un ejemplo destacado es el pulmon en chip desarrollado en dos mil diez. Este dispositivo imita la interfaz entre el aire y la sangre en los alveolos reproduciendo la contraccion y expansion del tejido durante la respiracion. Ha permitido estudiar enfermedades pulmonares y probar tratamientos de manera mas realista que en modelos animales.")
    time.sleep(4)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen2.jpg")
    animated_speech_service.say("Por que son tan importantes? Porque ofrecen modelos mucho mas precisos que los cultivos celulares tradicionales o los ensayos con animales. Ayudan a predecir mejor la eficacia y toxicidad de los farmacos y abren la puerta a una medicina mas personalizada.")
    time.sleep(4)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen3.jpg")
    animated_speech_service.say("Hoy en dia sus principales aplicaciones estan en farmacologia para probar nuevos medicamentos en toxicologia para evaluar la seguridad de sustancias quimicas y en el modelado de enfermedades como el cancer la inflamacion o el edema pulmonar.")
    time.sleep(3)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen2.jpg")
    animated_speech_service.say("Sin embargo hay desafios. Los chips suelen enfocarse en un solo organo lo que no refleja la complejidad del cuerpo humano. Ademas la estandarizacion el costo y la integracion de sensores en tiempo real son retos por superar.")
    time.sleep(3)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen3.jpg")
    animated_speech_service.say("Entre los innovadores clave estan Dan Huh creador del pulmon en chip en la Universidad de Harvard y la argentina Solange Massa quien desarrollo un higado en chip para pruebas de toxicidad sin usar animales.")
    time.sleep(3)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen2.jpg")
    animated_speech_service.say("A futuro los organos en chip evolucionaran hacia sistemas complejos que integren varios organos con sensores avanzados orientados a medicina personalizada. Tambien tendran un rol central en regulacion de farmacos e investigacion reduciendo la experimentacion animal.")
    time.sleep(3)

    tablet_service.showImage("http://198.18.0.1/apps/usta/Imagen3.jpg")
    animated_speech_service.say("En conclusion los organos en chip son una revolucion en miniatura que combina biologia e ingenieria y promete transformar como entendemos y cuidamos la salud humana.")
    time.sleep(3)

    a = 0

