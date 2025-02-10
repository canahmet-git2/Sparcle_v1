from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QTimer, QPointF
import math
import random
from .presets.particle_presets import ParticlePreset, ParticleParams

class Particle:
    def __init__(self, x, y, params: ParticleParams):
        self.x = x
        self.y = y
        self.lifetime = random.uniform(*params.lifetime)
        self.age = 0
        self.scale = random.uniform(*params.start_scale)
        self.end_scale = random.uniform(*params.end_scale)
        
        angle = math.radians(random.uniform(*params.angle_range))
        speed = random.uniform(*params.velocity)
        self.vx = speed * math.cos(angle)
        self.vy = speed * math.sin(angle)
        
        self.rotation = 0
        self.rotation_speed = random.uniform(*params.rotation_speed)
        self.gravity = params.gravity
        self.path_type = params.path_type
        
        # Color interpolation
        self.start_color = params.start_color
        self.end_color = params.end_color
        
    def update(self, dt):
        self.age += dt
        if self.path_type == "physics":
            self.vy += self.gravity * dt
        
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.rotation += self.rotation_speed * dt
        
        # Calculate life progress
        progress = self.age / self.lifetime
        
        # Interpolate scale
        self.current_scale = self.scale + (self.end_scale - self.scale) * progress
        
        # Interpolate color
        self.current_color = tuple(
            int(self.start_color[i] + (self.end_color[i] - self.start_color[i]) * progress)
            for i in range(4)
        )
        
        return self.age < self.lifetime

class ParticlePreviewPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.background_opacity = 1.0
        self.setMinimumSize(400, 400)
        
        self.particles = []
        self.current_preset = None
        self.last_emission_time = 0
        
        # Setup update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_particles)
        self.timer.start(16)  # ~60 FPS
        
    def set_preset(self, preset: ParticlePreset):
        self.current_preset = preset
        self.particles.clear()
        
    def update_particles(self):
        if not self.current_preset:
            return
            
        current_time = self.timer.interval() / 1000.0
        
        # Emit new particles
        if self.current_preset:
            particles_to_emit = self.current_preset.params.emission_rate * current_time
            whole_particles = int(particles_to_emit)
            fractional_part = particles_to_emit - whole_particles
            
            if random.random() < fractional_part:
                whole_particles += 1
                
            for _ in range(whole_particles):
                self.particles.append(Particle(
                    self.width() / 2,
                    self.height() / 2,
                    self.current_preset.params
                ))
        
        # Update existing particles
        self.particles = [p for p in self.particles if p.update(current_time)]
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw background with grid
        background_color = QColor(40, 40, 40, int(255 * self.background_opacity))
        painter.fillRect(self.rect(), background_color)
        
        # Draw grid
        painter.setPen(QColor(60, 60, 60))
        grid_size = 20
        
        for x in range(0, self.width(), grid_size):
            painter.drawLine(x, 0, x, self.height())
        for y in range(0, self.height(), grid_size):
            painter.drawLine(0, y, self.width(), y)
            
        # Draw particles
        for particle in self.particles:
            color = QColor(*particle.current_color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(color)
            
            painter.save()
            painter.translate(particle.x, particle.y)
            painter.rotate(particle.rotation)
            
            size = particle.current_scale * grid_size
            painter.drawEllipse(QPointF(0, 0), size/2, size/2)
            
            painter.restore() 