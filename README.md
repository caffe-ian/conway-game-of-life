# Conway's Game of Life
_A simple Python implementation of John Conway’s legendary zero-player game — built for self-learning and algorithmic exploration._

[![Python](https://img.shields.io/badge/Python-3.10%2B-informational)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---

## 🧠 About the Project
This project is a minimal, educational implementation of **Conway’s Game of Life**, a classic cellular automaton devised by mathematician **John Horton Conway**.  
It demonstrates how simple rules can generate complex, emergent behaviors over time.

This version was built as a **self-learning exercise** to practice:
- Python fundamentals  
- Simulation logic and grid-based updates  
- Clean code structure and modular design  
- Visualization of algorithmic evolution  

---

## 🎮 Game Rules
Each cell on a 2D grid can be **alive** or **dead**.  
On each iteration (“tick”), the next state of the grid is determined by these simple rules:

1. Any live cell with **2 or 3** live neighbors survives.  
2. Any dead cell with **exactly 3** live neighbors becomes alive.  
3. All other live cells die in the next generation, and all other dead cells stay dead.

---

## 🗂️ Project Structure
```
conway-game-of-life/
├─ main.py # Entry point / main simulation loop
├─ game.py # Core Game of Life logic (grid, updates, etc.)
├─ display.py # Optional visualization / terminal output
├─ utils.py # Helper functions (optional)
└─ README.md
```

---

## 🚀 How to Run

### 1) Clone the repository
```bash
git clone https://github.com/caffe-ian/conway-game-of-life.git
cd conway-game-of-life
```

### 2) (Optional) Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate     # macOS/Linux
# or
.venv\Scripts\activate        # Windows
```

### 3) Run the program
```bash
python main.py [grid_width] [grid_height] # Defaults to 30 * 30
```
Depending on your version, it may:
- Print grid updates directly in the console
- Or open a simple GUI / visualization window (if implemented)

---

## ⚙️ Possible Improvements
This project is meant for learning and experimentation, so feel free to extend it with:
- 🟩 Graphical visualization (e.g. Pygame, Tkinter, or Matplotlib)
- ⏱️ Adjustable simulation speed
- 💾 Saving/loading patterns (gliders, pulsars, etc.)
- 🌐 Infinite grid / wrap-around mode
- 🧩 Interactive cell editing

---

## 📸 Example Output

---

## 📄 License
This project is licensed under the MIT License.
See [LICENSE](LICENSE) for full details.

> You are free to use, modify, and distribute this code for educational or commercial purposes — just include the original license and credit @caffe-ian.

---

## 🙌 Credits
Created by @caffe-ian for self-learning and algorithmic exploration.
Inspired by John Conway’s Game of Life and the beauty of emergent systems.
