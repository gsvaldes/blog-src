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

Una de las características de Vue que me gusta es que, aunque permite la compilación y organización de código complejo, para empezar, se puede utilizarlo colocando un enlance a la red de distribución de contenidos (CDN) en la cabeza de su archivo ``html`` y conectar su instancia Vue a un elemento de html a traves del atributo ``el``.

.. code-block:: html

    <!DOCTYPE html>
    <html lang="es">
        <head>
        <meta charset="utf-8">
        <title>título</title>
        <script src="https://unpkg.com/vue"></script>
        <script src="vue-canvas.js"></script>
    </head>
    <body>
        <div id='app'>
        </div>
    </body>
    </html>

Y en el archivo vue-canvas.js

.. code-block:: javascript

    var vm = new Vue({
        el: '#app',
    });


Por supuesto, este código no hace nada todavía.  Hagamos una bola rebotante.

Primero, agregue un elemento canvas al archivo html dentro de la div controlada por VueJS.

.. code-block:: html

    <div id="app">
        <canvas id="canvas"></canvas>
    </div>

Y actualizar vue-canvas.js

.. code-block:: javascript

    var vm = new Vue({
        el: '#app',
        data: {
            ctx: null,
            width: 0,
            height: 0,
        },
        mounted: function(){
            var canvas = document.getElementById('canvas');
            this.ctx = canvas.getContext('2d');
            this.width = canvas.width;
            this.height = canvas.height;
        }
    });

Según la `documentación de VueJS <https://vuejs.org/v2/api/#mounted>`_, se llama al método ``mounted`` después de que ``el``, que es en nuestro caso el ``div`` with ``id="app"``, ha sido reemplazado por ``vm.$el``  de la instancia de Vue.



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