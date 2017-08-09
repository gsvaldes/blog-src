Usando VueJS con Canvas
#######################

:date: 2017-6-26 6:05
:modified: 2017-6-26 6:05
:tags: random
:category: vuejs
:slug: vue-canvas
:lang: es
:authors: Geoffrey Valdes
:summary: Using VueJS with Canvas
:javascripts: https://npmcdn.com/vue/dist/vue.js, vue-canvas.js

Recientemente, he estado disfrutando de la lectura de `The Nature of Code <http://natureofcode.com/book/>`_ (La Naturaleza de Código) de Daniel Schiffman.  El libro explica cómo programar animaciones que reflejan los procesos naturales.  Los ejemplos utilizan una biblioteca Java llamada `Processing <https://processing.org/>`_.   Existe una adaptación de Processing a JavaScript, `Processing.js <http://processingjs.org/>`_, sin embargo, quería ver si podía recrear algunos de los ejemplos de The Nature of Code desde cero, usando `VueJS <https://vuejs.org/>`_ y el elemento HTML ``<canvas>`` 



.. raw:: html 

  <div id='app'>
    <canvas id="canvas"></canvas>
    <div>
      <button @click="drawBall">Dibujar Pelota</button>
      <button @click="moveBall">Empezar</button>
      <button @click="stopBall">Detener</button>
      <button @click="clearCanvas">Borrar</button>
    </div>
  </div>