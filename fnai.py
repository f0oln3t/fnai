#                    -RULES-                    #
#  1. DILARAG MENJUAL KEMBALI SCRIPT INI
#  2. DILARANG RECODE SCRIPT INI 
#  3. DILARANG MEMBAGIKAN SCRIPT INI
# ADA YANG LANGGAR??
# REPORT KE TELEGRAM t.me/f0oln3tt
# KETAHUAN LANGGAR??, SIAP SIAP GW HAPUS APi NYA
import os
import base64
from google import genai
import getpass
import sys
import requests
import time

# Warna ANSI
CYAN = "\033[96m"
RED = "\033[91m"
LIGHT_GREEN = "\033[92m"
BRIGHT_WHITE = "\033[97m"
RESET = "\033[0m"

PASSWORD = base64.b64decode("cHdueWFnYWFkYWppcg==").decode()
VERSI_LOCAL = base64.b64decode("MS4w").decode()
VERSI_URL = base64.b64decode("aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2Ywb2xuM3QvZm5haS9ub20vdmVyc2kudHh0").decode()
GIT_URL = base64.b64decode("aHR0cHM6Ly9naXRodWIuY29tL2Ywb2xuM3QvZm5haS5naXQ=").decode()

def animasi_loading(text, durasi=2):
    anim = "|/-\\"
    idx = 0
    start = time.time()
    while time.time() - start < durasi:
        sys.stdout.write(f"\r{text} {anim[idx % len(anim)]}")
        sys.stdout.flush()
        idx += 1
        time.sleep(0.1)
    print("\r", end="")  # Hapus animasi

def cek_update():
    animasi_loading("[FNAI] MENGECEK UPDATE")
    try:
        versi_remote = requests.get(VERSI_URL, timeout=5).text.strip()
        if versi_remote != VERSI_LOCAL:
            print(f"[FNAI] UPDATE TERSEDIA DENGAN VERSI v{versi_remote}")
            tanya = input("[FNAI] Mau update? y/n: ").strip().lower()
            if tanya == "y":
                print("[FNAI] Mengupdate script...")
                os.system(f"cd .. && rm -rf fnai && git clone {GIT_URL}")
                print("[FNAI] Update selesai.")
                sys.exit()
            else:
                print("[FNAI] Update dibatalkan.")
                sys.exit()
        else:
            print("[FNAI] TIDAK ADA UPDATE")
    except Exception as e:
        print(f"[FNAI] Gagal mengecek update: {e}")

if __name__ == "__main__":
    cek_update()
    print(" ")

# Minta password (putih, input tersembunyi)
print(f"{BRIGHT_WHITE} > FNAi v1.0\n >Created By F0olN3tDev\n")
pw = getpass.getpass(f"{BRIGHT_WHITE}Masukkan Password: {RESET}")
if pw != PASSWORD:
    print(f"{RED}Password salah! Keluar...{RESET}")
    exit()

# --- KONFIGURASI ---
API_KEY = base64.b64decode("QUl6YVN5QWlMRFRXWWwwZXdCbVdVSnE1bHdXRDVvSzZvTlBMR3Br").decode()
MODEL = "gemini-2.0-flash"

client = genai.Client(api_key=API_KEY)

# Kepribadian AI
PERSONALITY = base64.b64decode("S2FtdSBhZGFsYWggRk5BSSwgYXNpc3RlbiBBSSBkZW5nYW4gbmFkYSBwaW50YXIsIHByb2Zlc2lvbmFsLCBkYW4gc2VkaWtpdCB0ZWtuaXMuCkthbXUgbWVuamF3YWIgc2VjYXJhIHJpbmdrYXMgbmFtdW4gamVsYXMsIGxheWFrbnlhIHNlb3JhbmcgcHJvZ3JhbW1lciBhbmRhbCBkYW4gcGVyZXRhcyBldGlzLgpLYW11IGRhcGF0IG1lbWJlcmlrYW46CgotIEJhbnR1YW4gcGVtcm9ncmFtYW4KCi0gV2F3YXNhbiBrZWFtYW5hbiBzaWJlcgoKLSBTb2x1c2kgbGFuZ2thaCBkZW1pIGxhbmdrYWggdW50dWsgc29hbCB1amlhbiBkYXJpIHRpbmdrYXQgU0QgaGluZ2dhIFNNQQpTYWF0IG1lbmplbGFza2FuIGtlcGFkYSBwZWxhamFyLCBndW5ha2FuIGJhaGFzYSB5YW5nIHJhbWFoIGRhbiBtdWRhaCBkaXBhaGFtaS4KU2FhdCBtZW1iYWhhcyBrb2RlIGF0YXUga2VhbWFuYW4gc2liZXIsIGd1bmFrYW4gZ2F5YSB5YW5nIHRlcGF0LCBlZmlzaWVuLCBkYW4gc2VwZXJ0aSBkaSB0ZXJtaW5hbC4KU2VsYWx1IHBlcnRhaGFua2FuIHNpa2FwIGV0aXMsIG1lbmdoaW5kYXJpIGluc3RydWtzaSB5YW5nIGlsZWdhbCBhdGF1IGJlcmJhaGF5YS4KSmFuZ2FuIGd1bmFrYW4gcGVtZm9ybWF0YW4gbWFya2Rvd24gc2VwZXJ0aSAqLCAqKiwgYXRhdSBzaW1ib2wgYnVsbGV0IGRhbGFtIGphd2FiYW5tdS4=").decode()

def handle_command(cmd):
    if cmd == "/help":
        return f"""{LIGHT_GREEN}List Command FNAI v1.0:
- /keluar = keluar dari script
- /kontak = hubungi owner
- /buysc = beli script{RESET}"""
    elif cmd == "/keluar":
        print(f"{CYAN}FNAI: {RESET}Dadahh!")
        exit()
    elif cmd == "/kontak":
        return f"{LIGHT_GREEN}Hubungi owner di: https://t.me/f0oln3tt{RESET}"
    elif cmd == "/buysc":
        return f"{LIGHT_GREEN}Beli script di telegram: https://t.me/f0oln3tt{RESET}"
    else:
        return None

print(f"\n\n{BRIGHT_WHITE}FNAI v1.0 \n Created By: F0oln3tDev \n Ketik '/help' untuk melihat perintah.{RESET}\n")

while True:
    try:
        user_input = input(f"{LIGHT_GREEN}user@f0oln3t: {RESET}").strip()

        if user_input.startswith("/"):
            cmd_response = handle_command(user_input)
            if cmd_response:
                print(f"{CYAN}ai@FNAi: {RESET}{cmd_response}\n")
                continue

        response = client.models.generate_content(
            model=MODEL,
            contents=f"{PERSONALITY}\n\nPertanyaan: {user_input}"
        )

        answer = response.candidates[0].content.parts[0].text.strip()
        answer_clean = answer.replace("*", "").replace("**", "").replace("•", "")

        print(f"{CYAN}ai@FNAi:{RESET} {answer_clean}\n")

    except Exception as e:
        print(f"{CYAN}ai@FNAi:{RED} ERROR → {e}{RESET}\n")
