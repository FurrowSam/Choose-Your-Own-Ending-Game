# Samurai and Cowboy: A Dark Tale

A narrative-driven choice-based adventure game built with Pygame, where a samurai and cowboy must unite to take down an evil corporation in a dystopian world.

## 📖 Story

In a world torn apart by greed, two unlikely heroes emerge from the shadows. A samurai from the East seeks vengeance, while a cowboy from the West searches for justice. Their destinies intertwined, they must work together to face a powerful corporation threatening their world.

Your choices determine their path—will they infiltrate the city or attack the corporation directly? Will they fight or use stealth? The fate of their world rests in your hands.

## 🎮 Features

- **Branching Narrative**: Multiple story paths based on player choices
- **Character-Driven Story**: Follow the journey of two distinct protagonists
- **Visual Storytelling**: Custom backgrounds and character sprites
- **Choice-Based Gameplay**: Navigate critical decisions that shape the outcome
- **Multiple Endings**: Different paths lead to different conclusions

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Pygame 2.0+

### Setup

1. Clone the repository:
```bash
git clone https://github.com/FurrowSam/Choose-Your-Own-Ending-Game.git
cd Choose-Your-Own-Ending-Game
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the game:
```bash
python main.py
```

## 🎯 How to Play

- **Arrow Keys (↑/↓)**: Navigate menu choices
- **Enter**: Confirm selection
- **ESC**: Quit game (when implemented)

The game will automatically advance through story scenes. When presented with choices, use the arrow keys to select your option and press Enter to proceed.

## 📁 Project Structure

```
Choose-Your-Own-Ending-Game/
├── main.py                 # Entry point for the game
├── assets/                 # Game assets
│   ├── images/            # Backgrounds and character sprites
│   └── fonts/             # Custom fonts (if any)
├── scenes/                # Game scenes/chapters
│   ├── intro.py          # Opening scene
│   ├── choice_one.py     # First major decision point
│   ├── go_to_the_city.py # City path scene
│   ├── city_exploration.py
│   ├── attack_corporation.py
│   ├── corporation_infiltration.py
│   └── ending.py         # Game endings
├── utils/                 # Utility modules
│   ├── scene_manager.py  # Handles scene transitions
│   └── ui_elements.py    # Reusable UI components (buttons, health bars, etc.)
└── requirements.txt       # Python dependencies
```

## 🛠️ Development

### Adding New Scenes

1. Create a new scene file in the `scenes/` directory
2. Implement the scene class with `__init__`, `update()`, and `draw()` methods
3. Import and reference the scene in relevant choice points

Example scene structure:
```python
import pygame

class YourScene:
    def __init__(self, screen):
        self.screen = screen
        self.next_scene = None
        # Initialize your scene elements
    
    def update(self):
        # Handle logic and input
        pass
    
    def draw(self):
        # Render the scene
        pass
```

### Scene Manager

The `SceneManager` class handles automatic scene transitions. When a scene sets `self.next_scene` to a new scene instance, the manager switches to it on the next update cycle.

## 🐛 Known Issues

- Some scenes may need additional content implementation
- Timer variables need initialization in certain scenes
- Save/load functionality not yet implemented

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the game:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is available for personal and educational use.

## 👤 Author

**FurrowSam**

- GitHub: [@FurrowSam](https://github.com/FurrowSam)

## 🙏 Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Inspired by classic choose-your-own-adventure games

---

*Embark on a dark journey where honor meets justice, and every choice matters.*
