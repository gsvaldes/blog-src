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


Recently, I've been enjoying  `The Nature of Code <http://natureofcode.com/book/>`_ by Daniel Schiffman.  The book explains how to code animations that mirror natural processes.  The examples use a Java library called `Processing <https://processing.org/>`_.  There is a port of Processing to JavaScript, `Processing.js <http://processingjs.org/>`_, however, I wanted to see if I could recreate some of the examples from The Nature of Code from scratch, using `VueJS <https://vuejs.org/>`_ and the HTML ``<canvas>`` element.

One of the features of Vue that I like is that, while it allows for complex code organization and build processes, to get started, you can just drop in a link to the Vue CDN in the head of your ``html`` file, and connect your Vue instance to an html element via the ``el`` attribute.

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

First, add a canvas element to the html file inside of the div controlled by VueJS.

.. code-block:: html

    <div id="app">
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


According to the `VueJS documentation <https://vuejs.org/v2/api/#mounted>`_, the ``mounted`` method is called after the ``el``, in our case the ``div`` with ``id="app"``, has been replaced by the Vue instance ``vm.$el``.  We can't set ``this.ctx`` equal to ``canvas.getContext('2d')`` until after mount, because until then the ``canvas`` element does not yet exist on the page, as the section of our html file within the app div serves as a template for what VueJS will eventually render during the mount.  In the ``mounted`` method, we are assigning the width and height of the canvas element to the width and height that we created in the data attribute so that we can access them later.

Now that we can control the canvas context, ctx, from vue, let's add a method to draw a ball.

Add a methods object to our VueJS instance and a drawBall method within it, and also add x and y attributes for the ball within our data object.

.. code-block:: javascript

    var vm = new Vue({
        el: '#app',
        data: {
            ctx: null,
            width: 0,
            height: 0,
            x: 25,
            y: 25,
        },
        methods: {
            drawBall: function(){
                var radius = 15;
                this.ctx.beginPath();
                this.ctx.arc(this.x, this.y, radius, 0, 2 * Math.PI, false);
                this.ctx.fillStyle = 'red';
                this.ctx.fill();
                this.ctx.lineWidth = 5;
                this.ctx.strokeStyle = '#003300';
                this.ctx.stroke();
            },
        },
        mounted: function(){
          var canvas = document.getElementById('canvas');
          this.ctx = canvas.getContext('2d');
          this.width = canvas.width;   
          this.height = canvas.height;
        }
    }); 


Within the html, we can also add a button to call the drawBall method

.. code-block:: html

    <div id="app">
        <canvas id="canvas"></canvas>
        <div>
            <button @click="drawBall">Draw Ball</button>
        </div>
    </div>

Clicking on the Draw Ball button will draw a ball centered 25 px down and 25 px to the right of the upper left corner of the canvas element.

Before we add code to move the ball, let's create a method to clear the ball from it's old location.

.. code-block:: javascript

        methods: {
        ...

        clearCanvas: function(){
            this.ctx.clearRect(0,0, this.width, this.height);
        },

Now we can add our drawBall method.  Update the  ``data`` element

.. code-block:: javascript

    data: {
        ctx: null,
        width: 0,
        height: 0,
        x: 25,
        y: 25,
        xSpeed: .5,
        ySpeed: 1.5,
        ballTimer: null

    },

And add two new methods, the formula to move and change the direction of the ball comes from ``The Nature of Code``

.. code-block:: javascript

        moveBall: function(){
            this.stopBall();  // stop the previous ballTimer if already running
            vm = this;
            this.ballTimer = setInterval(function(){
                vm.x += vm.xSpeed;
                vm.y += vm.ySpeed;
                if ((vm.x > vm.width) || (vm.x < 0)) {
                  vm.xSpeed = vm.xSpeed * -1;
                }
                if ((vm.y  > vm.height) || (vm.y  < 0)) {
                  vm.ySpeed  = vm.ySpeed  * -1;
                }
                vm.clearCanvas();
                vm.drawBall();
            }, 10)
        },
        stopBall: function(){
            clearInterval( this.ballTimer );
        }

Finally, add a couple more buttons in the ``app`` element of the html

.. code-block:: html

  <div id='app'>
    <canvas id="canvas"></canvas>
    <div>
      <button @click="drawBall">Draw Ball</button>
      <button @click="moveBall">Start Ball</button>
      <button @click="stopBall">Stop Ball</button>
      <button @click="clearCanvas">Clear</button>
    </div>
  </div>


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