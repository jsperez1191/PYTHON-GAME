# Bulls-I 🎯

A simple arcade-style shooting game built with **Pygame**. Blocks fall from the top of the screen — shoot them before they reach the bottom!

## Gameplay

You control a triangle-shaped ship at the bottom of the screen. Green blocks spawn randomly at the top and fall downward. Shoot them with bullets to score points before they reach the bottom of the screen.

- **+1 point** for every block you destroy
- **−1 point** for every block that reaches the bottom
- Score never drops below 0
- The game runs indefinitely — see how high you can score

## Controls

| Key | Action |
|---|---|
| `←` / `→` | Move left / right |
| `Space` | Shoot a bullet |
| Window close button | Quit the game |

## Requirements

- Python 3
- [Pygame](https://www.pygame.org/)

## Installation & Running

```bash
pip install pygame
python game.py
```

## How It Works

The game runs on a single loop (`while running`) capped at 60 FPS via `pygame.time.Clock()`. Each frame:

1. **Input** — arrow keys move the player (clamped to stay on-screen); `Space` fires a bullet from the player's position
2. **Bullets** — travel upward each frame and are checked against every enemy's bounding box for a collision
3. **Enemies** — spawn at a random x-position with roughly a 1-in-60 chance per frame, then move downward at a constant speed
4. **Collisions** — a hit removes the enemy, increments the score, and spawns an explosion effect
5. **Explosions** — drawn as an expanding orange circle that grows each frame until it's removed at radius 40
6. **Scoring** — rendered top-left each frame using Pygame's font module

All game entities (bullets, enemies, explosions) are tracked as plain Python lists of `[x, y, ...]` coordinates, rebuilt each frame to drop anything off-screen or resolved.

## Project Structure

```
game.py    # Entire game: setup, main loop, rendering, and game logic
```

## Possible Improvements

- Add a game-over/restart state instead of running forever
- Increase enemy speed or spawn rate as score climbs, for difficulty scaling
- Add sound effects for shooting and explosions
- Track and display a high score across sessions
