from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum
import random
import math

class PresetCategory(Enum):
    WIN_CELEBRATIONS = "Win Celebrations"
    AMBIENT_EFFECTS = "Ambient Effects"
    SPECIAL_FEATURES = "Special Features"

@dataclass
class ParticleParams:
    emission_rate: float  # particles per second
    lifetime: tuple[float, float]  # (min, max) seconds
    start_scale: tuple[float, float]  # (min, max) initial scale
    end_scale: tuple[float, float]  # (min, max) final scale
    start_color: tuple[int, int, int, int]  # RGBA
    end_color: tuple[int, int, int, int]  # RGBA
    velocity: tuple[float, float]  # (min, max) initial velocity
    angle_range: tuple[float, float]  # (min, max) emission angle in degrees
    rotation_speed: tuple[float, float]  # (min, max) degrees per second
    gravity: float = 0.0
    path_type: str = "linear"  # "linear", "curved", "spiral", "physics"

@dataclass
class ParticlePreset:
    name: str
    category: PresetCategory
    description: str
    params: ParticleParams

# Predefined presets
PARTICLE_PRESETS = {
    # Win Celebrations
    "coin_burst": ParticlePreset(
        name="Coin Burst",
        category=PresetCategory.WIN_CELEBRATIONS,
        description="Gold coins exploding outward with physics-based motion",
        params=ParticleParams(
            emission_rate=100,
            lifetime=(1.0, 2.0),
            start_scale=(0.8, 1.2),
            end_scale=(0.6, 0.8),
            start_color=(255, 215, 0, 255),  # Gold
            end_color=(255, 215, 0, 0),
            velocity=(200, 400),
            angle_range=(0, 360),
            rotation_speed=(90, 180),
            gravity=500,
            path_type="physics"
        )
    ),
    
    "spiral_upward": ParticlePreset(
        name="Spiral Upward",
        category=PresetCategory.WIN_CELEBRATIONS,
        description="Shimmering particles that spiral upward in a double helix",
        params=ParticleParams(
            emission_rate=50,
            lifetime=(1.5, 2.0),
            start_scale=(0.3, 0.5),
            end_scale=(0.1, 0.2),
            start_color=(255, 255, 255, 255),
            end_color=(180, 180, 255, 0),
            velocity=(100, 150),
            angle_range=(80, 100),
            rotation_speed=(0, 0),
            path_type="spiral"
        )
    ),

    # Ambient Effects
    "floating_elements": ParticlePreset(
        name="Floating Elements",
        category=PresetCategory.AMBIENT_EFFECTS,
        description="Theme-specific particles that float naturally",
        params=ParticleParams(
            emission_rate=20,
            lifetime=(3.0, 5.0),
            start_scale=(0.4, 0.6),
            end_scale=(0.3, 0.5),
            start_color=(255, 255, 255, 200),
            end_color=(255, 255, 255, 0),
            velocity=(30, 50),
            angle_range=(60, 120),
            rotation_speed=(-30, 30),
            path_type="curved"
        )
    ),

    # Special Features
    "power_up": ParticlePreset(
        name="Power-Up Effect",
        category=PresetCategory.SPECIAL_FEATURES,
        description="Converging energy particles that form symbols",
        params=ParticleParams(
            emission_rate=80,
            lifetime=(0.8, 1.2),
            start_scale=(0.2, 0.4),
            end_scale=(0.1, 0.2),
            start_color=(0, 255, 255, 255),
            end_color=(0, 128, 255, 0),
            velocity=(150, 200),
            angle_range=(0, 360),
            rotation_speed=(0, 0),
            path_type="converge"
        )
    ),
}

def get_preset_by_name(name: str) -> Optional[ParticlePreset]:
    return PARTICLE_PRESETS.get(name)

def get_presets_by_category(category: PresetCategory) -> List[ParticlePreset]:
    return [preset for preset in PARTICLE_PRESETS.values() if preset.category == category]

def get_all_presets() -> Dict[str, ParticlePreset]:
    return PARTICLE_PRESETS 