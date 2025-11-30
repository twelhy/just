# -*- coding: utf-8 -*-

def setup():
    size(600, 400)
    colorMode(HSB, 360, 100, 100)
    frameRate(30)

    global particles
    particles = []
    global mountainColor
    mountainColor = color(200, 50, 50)

def draw():
    # Sunset Gradient Background
    # Map the frame count to HSB values
    hue = map(frameCount % 360, 0, 360, 20, 60)  # Orange/Pink hues
    saturation = map(frameCount % 360, 0, 360, 60, 80)
    brightness = map(frameCount % 360, 0, 360, 80, 100)
    
    # Create a dynamic background color
    backgroundColor = color(hue, saturation, brightness)
    background(backgroundColor)


    # Draw Mountain (Centered, bottom half)
    fill(mountainColor)
    noStroke()
    triangle(width * 0.2, height * 0.8, width * 0.5, height * 0.4, width * 0.8, height * 0.8)

    # Draw Trees (approximations, simple shapes)
    fill(30, 50, 50) # Dark brown/grey
    ellipse(width * 0.15, height * 0.3, 50, 80) # Left tree
    ellipse(width * 0.85, height * 0.3, 50, 80) # Right tree

    # Particle system (falling leaves/petals)
    num_particles = int(map(mouseX, 0, width, 0, 200)) # MouseX controls density
    for i in range(num_particles - len(particles)):
      particles.append(Particle(random(width), random(height * 0.3)))


    for p in particles:
        p.update()
        p.display()

    # Horizon line (Foreground)
    stroke(20, 50, 80) # Dark line
    line(0, height * 0.7, width, height * 0.7)


class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = random(2, 5)
        self.speedY = random(1, 3)
        self.alpha = 255

    def update():  # Changed to static method
        pass

    def update(self):
        self.y += self.speedY
        self.alpha -= 2
        if self.y > height or self.alpha <= 0:
            self.respawn()

    def display(self):
        noStroke()
        fill(10, 80, 100, self.alpha)
        ellipse(self.x, self.y, self.size, self.size)

    def respawn(self):
        self.x = random(width)
        self.y = random(height * 0.3)
        self.size = random(2, 5)
        self.speedY = random(1, 3)
        self.alpha = 255