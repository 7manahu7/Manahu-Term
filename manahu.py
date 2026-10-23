import curses
from curses import wrapper
import subprocess
import os


def clear_kitty_images():
    """Clears all currently rendered images in Kitty."""
    subprocess.run(["kitty", "+kitten", "icat", "--clear"])
    

def draw_kitty_image(path):
  """Renders an image at a specific terminal grid position (columns/rows)."""
  cmd = [
      "kitty",
      "+kitten",
      "icat",
      "--silent",
      f"--place={60}x{48}@{30}x{8}",
      path,
  ]
  subprocess.run(cmd)



def manahuTerm(stdscr):

    curses.curs_set(0)


    ourList = ["CyberPunk", "CityScape", "Evening", "Monochrome", "Space", "Nature"]
    selected = 0

    while True: 

        stdscr.erase()
        stdscr.addstr(3, 5, "Select Your Rice!!")


        for idx, option in enumerate(ourList):
            if idx == selected:
                stdscr.addstr(idx + 5, 5, f"> {option}", curses.A_REVERSE)
            else:
                stdscr.addstr(idx + 5, 5, f" {option}")
        stdscr.refresh()

        key = stdscr.getch()

           
        if key == curses.KEY_UP:
            selected = max(0, selected -1)
        elif key == curses.KEY_DOWN:
            selected = min(len(ourList) -1, selected + 1)

        elif key == ord("\n"):
            return ourList[selected].lower()
            break

        if selected == 0:
            path = "/home/manahu/Projects/Python/terminal-project/cyberpunk.png"
            clear_kitty_images()
            draw_kitty_image(path)
        elif selected == 1:
            path = "/home/manahu/Projects/Python/terminal-project/cityscape.png"
            clear_kitty_images()
            draw_kitty_image(path)
        elif selected == 2:
            path = "/home/manahu/Projects/Python/terminal-project/evening.png"
            clear_kitty_images()
            draw_kitty_image(path)

        elif selected == 4:
            path = "/home/manahu/Projects/Python/terminal-project/space.png"
            clear_kitty_images()
            draw_kitty_image(path)
        elif selected == 3:
            path = "/home/manahu/Projects/Python/terminal-project/monochrome.png"
            clear_kitty_images()
            draw_kitty_image(path)
        elif selected == 5:
            path = "/home/manahu/Projects/Python/terminal-project/nature.png"
            clear_kitty_images()
            draw_kitty_image(path)





def main():
    chosenTheme = wrapper(manahuTerm)
    
    if chosenTheme:
        themeDir = os.path.expanduser("~/.config/themes2")
        script_path = os.path.join(themeDir, f"{chosenTheme}.sh")

        if os.path.exists(script_path):
            subprocess.run([script_path], cwd=themeDir)
        else:
            print(f"Error: Script not found at {script_path}")

if __name__ == "__main__":
    main()

