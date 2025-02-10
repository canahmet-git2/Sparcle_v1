from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                           QListWidget, QLabel, QPushButton, QSlider)
from PyQt6.QtCore import Qt
from .preview_panel import ParticlePreviewPanel
from .preset_manager import PresetManager

class SparcleMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sparcle - Spine Particle VFX Tool")
        self.setMinimumSize(800, 600)
        
        # Initialize managers
        self.preset_manager = PresetManager()
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QHBoxLayout(main_widget)
        
        # Left panel - Preset list and controls
        left_panel = QWidget()
        left_layout = QVBoxLayout(left_panel)
        
        # Preset list
        self.preset_list = QListWidget()
        left_layout.addWidget(QLabel("Particle Presets"))
        left_layout.addWidget(self.preset_list)
        
        # Controls
        controls_layout = QVBoxLayout()
        self.export_button = QPushButton("Export to Spine")
        self.save_preset_button = QPushButton("Save Preset")
        controls_layout.addWidget(self.export_button)
        controls_layout.addWidget(self.save_preset_button)
        left_layout.addLayout(controls_layout)
        
        # Right panel - Preview
        self.preview_panel = ParticlePreviewPanel()
        
        # Transparency control
        transparency_layout = QHBoxLayout()
        transparency_layout.addWidget(QLabel("Background Transparency:"))
        self.transparency_slider = QSlider(Qt.Orientation.Horizontal)
        self.transparency_slider.setRange(0, 100)
        self.transparency_slider.setValue(100)
        self.transparency_slider.valueChanged.connect(self.update_transparency)
        transparency_layout.addWidget(self.transparency_slider)
        
        right_layout = QVBoxLayout()
        right_layout.addWidget(self.preview_panel)
        right_layout.addLayout(transparency_layout)
        
        # Add panels to main layout
        layout.addWidget(left_panel, 1)
        layout.addLayout(right_layout, 2)
        
        # Connect signals
        self.export_button.clicked.connect(self.export_to_spine)
        self.save_preset_button.clicked.connect(self.save_preset)
        self.preset_list.itemClicked.connect(self.load_preset)
        
    def update_transparency(self, value):
        opacity = value / 100.0
        self.preview_panel.set_background_opacity(opacity)
        
    def export_to_spine(self):
        # TODO: Implement export functionality
        pass
        
    def save_preset(self):
        # TODO: Implement preset saving
        pass
        
    def load_preset(self, item):
        # TODO: Implement preset loading
        pass 