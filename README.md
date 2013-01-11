SupermileageBench
=================

Installation
==============
Pour être en mesure de faire rouler l'application, il faut d'abord installer certains outils. La liste complète est disponible à https://www.dropbox.com/sh/93dek7jtaclbs02/72MSP9SUMW. Il est aussi important de les installer dans le bon ordre : 
  - Python 2.7.3
  - SetupTools 0.6C11
  - Phidgets x64
  - PhidgetsPython
  - Numpy 1.7.0
  - Scipy 0.11.0
  - MatPlotLib 1.2.0
  - wxPython 2.8
  - Dropbox Python API

Utilisation
===============
Après avoir installé les outils, il est possible d'utiliser l'application.
  - Connecter le capteur Phidgets à l'ordinateur
  - Démarrer l'application avec la ligne en terminal :
      <code>python supermileage_bench_app.py<code>

Développement
===============
Pour le développement, on peut utiliser le <code>fake_supermileage_bench_app.py</code> pour éviter d'avoir à connecter le capteur puisque celui-ci se charge d'envoyer des fausses données dans l'application.
