from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt

class ParticlePreviewPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.background_opacity = 1.0
        self.setMinimumSize(400, 400)
        
    def set_background_opacity(self, opacity):
        self.background_opacity = opacity
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Draw background with grid
        background_color = QColor(40, 40, 40, int(255 * self.background_opacity))
        painter.fillRect(self.rect(), background_color)
        
        # Draw grid
        painter.setPen(QColor(60, 60, 60))
        grid_size = 20
        
        # Vertical lines
        for x in range(0, self.width(), grid_size):
            painter.drawLine(x, 0, x, self.height())
            
        # Horizontal lines
        for y in range(0, self.height(), grid_size):
            painter.drawLine(0, y, self.width(), y) 