# Py Physics Engine

<div class="result-streaming markdown prose w-full break-words dark:prose-invert dark"><p>I apologize for the confusion. Here is an updated README for the physics engine:</p><h1>Physics Engine</h1><p>This is a physics engine designed to simulate the movement of balls in a 2D space. It uses the Python Turtle library to create a visual representation of the balls and their movement.</p><h2>Features</h2><ul><li>Allows customization of the ground height, screen width, screen height, and maximum height a ball can reach</li><li>Simulates the effects of gravity on the movement of the balls</li><li>Detects collisions between balls and the ground, reflecting their velocities accordingly</li><li>Detects collisions between balls, reflecting their velocities accordingly</li></ul><h2>Usage</h2><p>To use the physics engine, import the required libraries and create a ground and ball object. You can customize the parameters of the ground and ball objects as needed. Then, in a loop, call the <code>move</code> method of each ball object to update its position based on the laws of physics.</p><p>Example usage:</p><pre><div class="bg-black mb-4 rounded-md"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans"><span class="">ruby</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-ruby">import turtle as tr
import math

<span class="hljs-comment"># Create screen and ground objects</span>
tr.colormode(<span class="hljs-number">255</span>)
wn = tr.<span class="hljs-title class_">Screen</span>()
wn.tracer(<span class="hljs-number">0</span>)

<span class="hljs-variable constant_">GROUND_Y</span> = -<span class="hljs-number">200</span>
<span class="hljs-variable constant_">SCREEN_WIDTH</span> = <span class="hljs-number">800</span>
<span class="hljs-variable constant_">SCREEN_HEIGHT</span> = <span class="hljs-number">600</span>
<span class="hljs-variable constant_">MAX_HEIGHT</span> = <span class="hljs-number">400</span>

<span class="hljs-keyword">class</span> <span class="hljs-title class_">Ground</span>:
    <span class="hljs-keyword">def</span> <span class="hljs-title function_">__init__</span>(<span class="hljs-params"><span class="hljs-variable language_">self</span>, x, y</span>):
        ...

<span class="hljs-keyword">class</span> <span class="hljs-title class_">Ball</span>:
    <span class="hljs-keyword">def</span> <span class="hljs-title function_">__init__</span>(<span class="hljs-params"><span class="hljs-variable language_">self</span>, x, y, radius, color, dx, dy</span>):
        ...

    <span class="hljs-keyword">def</span> <span class="hljs-title function_">move</span>(<span class="hljs-params"><span class="hljs-variable language_">self</span>, gravity, dt</span>):
        ...

<span class="hljs-comment"># Create ball objects</span>
ball1 = <span class="hljs-title class_">Ball</span>(-<span class="hljs-number">50</span>, <span class="hljs-number">100</span>, <span class="hljs-number">2</span>, <span class="hljs-string">'blue'</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)
ball2 = <span class="hljs-title class_">Ball</span>(<span class="hljs-number">50</span>, <span class="hljs-number">0</span>, <span class="hljs-number">3</span>, <span class="hljs-string">'red'</span>, <span class="hljs-number">0</span>, <span class="hljs-number">0</span>)

<span class="hljs-comment"># Physics simulation loop</span>
<span class="hljs-keyword">while</span> <span class="hljs-title class_">True</span>:
    ball1.move(<span class="hljs-number">9.81</span>, <span class="hljs-number">0.1</span>)
    ball2.move(<span class="hljs-number">9.81</span>, <span class="hljs-number">0.1</span>)
    <span class="hljs-comment"># Update screen</span>
</code></div></div></pre></div>

