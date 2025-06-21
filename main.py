# main.py
from implementations import * # This imports all functions and fishosys
import pygame

# Flag to track if music was successfully initialized
music_initialized = False

# --- Initialize Pygame and Music ---
try:
    pygame.init()
    music_initialized = True
except Exception as e:
    print(f"Error initializing Pygame: {e}")
    print("Music playback disabled for this session.")

if music_initialized:
    try:
        pygame.mixer.music.load("atc.ogg")
        pygame.mixer.music.play(-1) # Loop indefinitely
        print("Background music started. Enjoy the simulation!")
    except pygame.error as e:
        print(f"Could not load or play music 'atc.ogg': {e}")
        print("Please check 'atc.ogg' file path, format, or integrity.")
        music_initialized = False 
        time.sleep(2)

# --- Initial Setup ---

if __name__ == "__main__":
    pygame.time.Clock().tick(10)

    print("\n--- Starting Fish-Shark Simulation ---")

    # --- Main Simulation Loop ---
    while state(): 
        time.sleep(0.5) 

        # Optional: Check if music unexpectedly stopped (unlikely with play(-1))
        if music_initialized and not pygame.mixer.music.get_busy():
            print("Music unexpectedly stopped! Attempting to restart...")
            try:
                pygame.mixer.music.play(-1)
            except pygame.error as e:
                print(f"Failed to restart music: {e}")
                music_initialized = False # Give up on music if restart fails

        # Calculate current counts BEFORE any moves
        fishes = sum(row.count('>') for row in fishosys)
        sharks = sum(row.count('#') for row in fishosys)
        print(f"\n--- Current state: {fishes} fishes, {sharks} sharks ---")
        
        [print(" ".join(row)) for row in fishosys]
        fish_move()
        [print(" ".join(row)) for row in fishosys]
        shark_move() 

        fishes_after_turn = sum(row.count('>') for row in fishosys)
        sharks_after_turn = sum(row.count('#') for row in fishosys)
        print(f"After this turn: {fishes_after_turn} fishes, {sharks_after_turn} sharks\n")
        

    # --- Cleanup ---
    print("Simulation has ended.")
    if music_initialized:
        pygame.mixer.music.stop()
        print("Music stopped.")
    if pygame.get_init():
        pygame.quit()
        print("Pygame uninitialized.")
    
    import sys
    sys.exit()