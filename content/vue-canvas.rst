Using VueJS with Canvas
#######################

:date: 2017-6-26 6:05
:modified: 2017-6-26 6:05
:tags: random
:category: vuejs
:slug: vue-canvas
:lang: en
:authors: Geoffrey Valdes
:summary: Using VueJS with Canvas
:javascripts: https://npmcdn.com/vue/dist/vue.js, vue-canvas.js


Recently, I've been enjoying  `The Nature of Code <http://natureofcode.com/book/>`_ by Daniel Schiffman.  The book explains how to code animations that mirror natural processes.  The examples use a Java library called `Processing <https://processing.org/>`_.  There is a port of Processing to JavaScript, `Processing.js <http://processingjs.org/>`_, however, I wanted to see if I could recreate some of the examples from The Nature of Code from scratch, using `VueJS <https://vuejs.org/>`_ and the HTML canvas element.

One of the biggest features of Vue that I like is that, while it allows for complex code organization and build processes, to get started, you can just drop in a link to the Vue CDN in the head of your ``html`` file, and connect your Vue javascript instance to an html element via the ``el`` attribute.

.. code-block:: html

    <!DOCTYPE html>
    <html lang="en">
        <head>
        <meta charset="utf-8">
        <title>title</title>
        <script src="https://unpkg.com/vue"></script>
        <script src="vue-canvas.js"></script>
    </head>
    <body>
        <div id='app'>
        </div>
    </body>
    </html>

And in your vue-canvas.js file

.. code-block:: javascript

    var vm = new Vue({
        el: '#app',
    });

Of course, this code doesn't do anything yet.  Let's make a bouncing ball.

First, add a canvas element to our html file inside of the div controlled by VueJS

.. code-block:: html

    <div id='app'>
        <canvas id="canvas"></canvas>
    </div>

And update vue-canvas.js

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

.. raw:: html 

  <div id='app'>
    <canvas id="canvas"></canvas>
    <div>
      <button @click="drawBall">Draw Ball</button>
      <button @click="moveBall">Start Ball</button>
      <button @click="stopBall">Stop Ball</button>
      <button @click="clearCanvas">Clear</button>
    </div>
  </div>