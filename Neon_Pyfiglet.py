import time
import os
from pyfiglet import figlet_format
from colorama import Fore, Style, init

init(autoreset=True)

# =====================================
# JUDUL
# =====================================
JUDUL = """Lampu Merah
           The Lantis
"""

# =====================================
# LIRIK
# =====================================
lirik = [
    ("Tapi ku berada di", Fore.CYAN),
    ("Lampu merah....", Fore.RED),
    ("Ku harap", Fore.MAGENTA),
    ("Kau sabar", Fore.BLUE),
    ("Untuk menunggu aku", Fore.YELLOW),
    ("Disana....", Fore.CYAN),
    ("Walau ku berada", Fore.MAGENTA),
    ("di lampu merah....", Fore.RED),
    ("Ku yakin semua ini", Fore.BLUE),
    ("Hanyalah hambatan", Fore.YELLOW),
    ("Sementara....", Fore.CYAN)
]

# =====================================
# CLEAR TERMINAL
# =====================================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# =====================================
# FRAME KOMPUTER
# Smooth karena perubahan kecil
# =====================================

frame_1 = Fore.CYAN + r"""
    ___________________         @@@
   |  _______________  |       @@@@@
   | |   ^      ^    | |        |||
   | |      --       | |       \|||/
   | |_______________| |        \|/
   |___________________|         |
       /___________\            / \
"""

frame_2 = Fore.CYAN + r"""
    ___________________         @@@
   |  _______________  |       @@@@@
   | |   o      o    | |        |||
   | |      __       | |       \|||/
   | |_______________| |        \|/
   |___________________|         |
       /___________\            / \
"""

# =====================================
# HEADER
# =====================================
def tampilkan_header():

    title = figlet_format(JUDUL, font="small")

    print(Fore.CYAN + Style.BRIGHT + title)

    print(Fore.YELLOW + "=" * 65)
    print(
        Fore.GREEN
        + Style.BRIGHT
        + "         ♪ MUSIC TERMINAL LYRIC PLAYER ♪"
    )
    print(Fore.YELLOW + "=" * 65)
    print()

# =====================================
# ANIMASI
# =====================================
def neon_gerak(teks, warna):

    ascii_teks = figlet_format(teks, font="big")

    for geser in range(0, 10):

        clear()

        tampilkan_header()

        # Smooth blinking
        if geser % 10 < 8:
            print(frame_1)
        else:
            print(frame_2)

        padding = " " * geser

        # Neon utama
        print(warna + Style.BRIGHT + padding + ascii_teks)

        time.sleep(0.07)

# =====================================
# MAIN
# =====================================
for teks, warna in lirik:

    neon_gerak(teks, warna)

    time.sleep(1.1)

    clear()
