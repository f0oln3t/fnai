#                    -RULES-                        #
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

# Warna ANSI
CYAN = "\033[96m"
RED = "\033[91m"
LIGHT_GREEN = "\033[92m"
BRIGHT_WHITE = "\033[97m"
RESET = "\033[0m"

PASSWORD = base64.b64decode("cHdueWFnYWFkYWppcg==").decode()

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
        print(f"{CYAN}FNAI: Dadahh!{RESET}")
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
                print(f"{CYAN}ai@FNAi: {cmd_response}{RESET}\n")
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