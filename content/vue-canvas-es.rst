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