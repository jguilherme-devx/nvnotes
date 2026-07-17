import subprocess as sp
import sys

sp.run(["pkg", "install", "neovim" , "-y"], check=True)

sp.run([sys.executable, "-m", "pip", "install", "rich"], check=True)

print("successfully downloaded")
