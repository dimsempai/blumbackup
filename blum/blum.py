# Made with ❤ by @adearman
# Join tele channel for update t.me/ghalibie
import argparse
import random
import requests
from requests.structures import CaseInsensitiveDict
import time
import datetime
from colorama import init, Fore, Style
init(autoreset=True)



start_time = datetime.datetime.now()  # Tentukan waktu mulai saat bot dijalankan

def parse_arguments():
    parser = argparse.ArgumentParser(description='Blum BOT')
    parser.add_argument('--task', type=str, choices=['y', 'n'], help='Cek and Claim Task (y/n)')
    args = parser.parse_args()

    if args.task is None:
        # Jika parameter --task tidak diberikan, minta input dari pengguna
        task_input = input("Apakah Anda ingin cek dan claim task? (y/n, default n): ").strip().lower()
        # Jika pengguna hanya menekan enter, gunakan 'n' sebagai default
        args.task = task_input if task_input in ['y', 'n'] else 'n'

    return args


def check_tasks(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
   
    try:
        response = requests.get('https://game-domain.blum.codes/api/v1/tasks', headers=headers)
        if response.status_code == 200:
            tasks = response.json()
            for task in tasks:
                titlenya = task['title']
                if task['status'] == 'CLAIMED':
                    print(f"{Fore.CYAN+Style.BRIGHT}Task {titlenya} claimed  | Status: {task['status']} | Reward: {task['reward']}")
                elif task['status'] == 'NOT_STARTED':
                    print(f"{Fore.YELLOW+Style.BRIGHT}Starting Task: {task['title']}")
                    start_task(token, task['id'],titlenya)
                    claim_task(token, task['id'],titlenya)
                else:
                    print(f"{Fore.CYAN+Style.BRIGHT}Task already started: {task['title']} | Status: {task['status']} | Reward: {task['reward']}")
        else:
            print(f"{Fore.RED+Style.BRIGHT}\nFailed to get tasks")
    except:
        print(f"{Fore.RED+Style.BRIGHT}\nFailed to get tasks {response.status_code} ")
def start_task(token, task_id,titlenya):
    url = f'https://game-domain.blum.codes/api/v1/tasks/{task_id}/start'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print(f"{Fore.GREEN+Style.BRIGHT}\nTask {titlenya} started")
        else:
            print(f"{Fore.RED+Style.BRIGHT}\nFailed to start task {titlenya}")
        return 
    except:
        print(f"{Fore.RED+Style.BRIGHT}\nFailed to start task {titlenya} {response.status_code} ")

def claim_task(token, task_id,titlenya):
    print(f"{Fore.YELLOW+Style.BRIGHT}\nClaiming task {titlenya}")
    url = f'https://game-domain.blum.codes/api/v1/tasks/{task_id}/claim'
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    try:
        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            print(f"{Fore.CYAN+Style.BRIGHT}\nTask {titlenya} claimed")
        else:
            print(f"{Fore.RED+Style.BRIGHT}\nFailed to claim task {titlenya}")
    except:
        print(f"{Fore.RED+Style.BRIGHT}\nFailed to claim task {titlenya} {response.status_code} ")

        
def get_new_token(query_id):
    import json
    # Header untuk permintaan HTTP
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json",
        "origin": "https://telegram.blum.codes",
        "priority": "u=1, i",
        "referer": "https://telegram.blum.codes/"
    }

    # Data yang akan dikirim dalam permintaan POST
    data = json.dumps({"query": query_id})

    # URL endpoint
    url = "https://gateway.blum.codes/v1/auth/provider/PROVIDER_TELEGRAM_MINI_APP"

    # Mencoba mendapatkan token hingga 3 kali
    for attempt in range(3):
        print(f"\r{Fore.YELLOW+Style.BRIGHT}Mendapatkan token...", end="", flush=True)
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print(f"\r{Fore.GREEN+Style.BRIGHT}Token berhasil dibuat", end="", flush=True)
            response_json = response.json()
            return response_json['token']['refresh']
        else:
            print(response.json())
            print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan token, percobaan {attempt + 1}", flush=True)
    # Jika semua percobaan gagal

    print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan token setelah 3 percobaan.", flush=True)
    return None

# Fungsi untuk mendapatkan informasi pengguna
def get_user_info(token):

    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.get('https://gateway.blum.codes/v1/user/me', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        hasil = response.json()
        if hasil['message'] == 'Token is invalid':
            print(f"{Fore.RED+Style.BRIGHT}Token salah, mendapatkan token baru...")
            # Mendapatkan token baru
            new_token = get_new_token()
            if new_token:
                print(f"{Fore.GREEN+Style.BRIGHT}Token baru diperoleh, mencoba lagi...")
                return get_user_info(new_token)  # Rekursif memanggil fungsi dengan token baru
            else:
                print(f"{Fore.RED+Style.BRIGHT}Gagal mendapatkan token baru.")
                return None
        else:
            print(f"{Fore.RED+Style.BRIGHT}Gagal mendapatkan informasi user")
            return None

# Fungsi untuk mendapatkan saldo
def get_balance(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    for attempt in range(3):
        try:
            response = requests.get('https://game-domain.blum.codes/api/v1/user/balance', headers=headers)
            # print(response.json())
            if response.status_code == 200:
                # print(f"{Fore.GREEN+Style.BRIGHT}Berhasil mendapatkan saldo")
                return response.json()
            else:
                print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan saldo, percobaan {attempt + 1}", flush=True)
        except:
            print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan saldo, mencoba lagi {attempt + 1}", flush=True)
    print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan saldo setelah 3 percobaan.", flush=True)
    return None

# Fungsi untuk memainkan game
def play_game(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://game-domain.blum.codes/api/v1/game/play', headers=headers)
    return response.json()


# Fungsi untuk mengklaim hadiah game
def claim_game(token, game_id, points):
    url = "https://game-domain.blum.codes/api/v1/game/claim"

    headers = CaseInsensitiveDict()
    headers["accept"] = "application/json, text/plain, */*"
    headers["accept-language"] = "en-US,en;q=0.9"
    headers["authorization"] = "Bearer "+token
    headers["content-type"] = "application/json"
    headers["origin"] = "https://telegram.blum.codes"

    headers["priority"] = "u=1, i"
    headers["user-agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
    data = '{"gameId":"'+game_id+'","points":'+str(points)+'}'

    resp = requests.post(url, headers=headers, data=data)
    return resp  # Kembalikan objek respons, bukan teksnya



def claim_balance(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://game-domain.blum.codes/api/v1/farming/claim', headers=headers)
    return response.json()

# Fungsi untuk memulai farming
def start_farming(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://game-domain.blum.codes/api/v1/farming/start', headers=headers)
    return response.json()

def refresh_token(old_refresh_token):
    url = 'https://gateway.blum.codes/v1/auth/refresh'
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'origin': 'https://telegram.blum.codes',
        'referer': 'https://telegram.blum.codes/'
    }
    data = {
        'refresh': old_refresh_token
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"{Fore.RED+Style.BRIGHT}Gagal refresh token untuk: {old_refresh_token}")
        return None  # atau kembalikan respons untuk penanganan lebih lanjut
# Membaca semua token dan menyimpannya dalam list

def check_balance_friend(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.get('https://gateway.blum.codes/v1/friends/balance', headers=headers)
    balance_info = response.json()
    return balance_info

# Fungsi untuk mengklaim saldo teman


def claim_balance_friend(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'origin': 'https://telegram.blum.codes',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }
    response = requests.post('https://gateway.blum.codes/v1/friends/claim', headers=headers)
    return response.json()

# cek daily 
import json
def check_daily_reward(token):
    headers = {
        'Authorization': f'Bearer {token}',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://telegram.blum.codes',
        'content-length': '0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site'
    }
    try:
        response = requests.post('https://game-domain.blum.codes/api/v1/daily-reward?offset=-420', headers=headers, timeout=10)
        if response.status_code == 400:
            try:
                return response.json()
            except json.JSONDecodeError:
                if response.text == "OK":
                    return response.text
                print(f"{Fore.RED+Style.BRIGHT}Json Error: {response.text}")
                return None
        else:
            try:
                return response.json()
            except json.JSONDecodeError:
                print(f"{Fore.RED+Style.BRIGHT}Json Error: {response.text}")
                return None
            # response.raise_for_status()  # Menangani status kode HTTP yang tidak sukses
            return None
    except requests.exceptions.Timeout:
        print(f"\r{Fore.RED+Style.BRIGHT}Gagal claim daily: Timeout")
    except requests.exceptions.RequestException as e:
        return response.json()
      
    return None

# while True:
#     cek_task_enable = input("Cek and Claim Task (default n) ? (y/n): ").strip().lower()
#     if cek_task_enable in ['y', 'n', '']:
#         cek_task_enable = cek_task_enable or 'n'
#         break
#     else:
#         print("Masukkan 'y' atau 'n'.")
def print_welcome_message():
    print(r"""
          
█▀▀ █░█ ▄▀█ █░░ █ █▄▄ █ █▀▀
█▄█ █▀█ █▀█ █▄▄ █ █▄█ █ ██▄
          """)
    print(Fore.GREEN + Style.BRIGHT + "Blum BOT")
    print(Fore.GREEN + Style.BRIGHT + "Update Link: https://github.com/adearman/blum")
    print(Fore.YELLOW + Style.BRIGHT + "Free Konsultasi Join Telegram Channel: https://t.me/ghalibie")
    print(Fore.BLUE + Style.BRIGHT + "Buy me a coffee :) 0823 2367 3487 GOPAY / DANA")
    print(Fore.RED + Style.BRIGHT + "NOT FOR SALE ! Ngotak dikit bang. Ngoding susah2 kau tinggal rename :)\n\n")
    current_time = datetime.datetime.now()
    up_time = current_time - start_time
    days, remainder = divmod(up_time.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    print(Fore.CYAN + Style.BRIGHT + f"Up time bot: {int(days)} hari, {int(hours)} jam, {int(minutes)} menit, {int(seconds)} detik")

    
checked_tasks = {}

args = parse_arguments()
cek_task_enable = args.task
with open('tgwebapp.txt', 'r') as file:
    query_ids = file.read().splitlines()
while True:
 
    print_welcome_message()
    

    for query_id in query_ids:
        
      
        token = get_new_token(query_id)  # Mendapatkan token baru
        user_info = get_user_info(token)
        if user_info is None:
            continue
        print(f"{Fore.BLUE+Style.BRIGHT}\r\n==================[{Fore.WHITE+Style.BRIGHT}{user_info['username']}{Fore.BLUE+Style.BRIGHT}]==================")  
        print(f"\r{Fore.YELLOW+Style.BRIGHT}Getting Info....", end="", flush=True)
        balance_info = get_balance(token)
        # print(balance_info)
        if balance_info is None:
            print(f"\r{Fore.RED+Style.BRIGHT}Gagal mendapatkan informasi balance", flush=True)
            continue
        else:
            available_balance_before = balance_info['availableBalance']  # asumsikan ini mengambil nilai dari JSON

            balance_before = f"{float(available_balance_before):,.0f}".replace(",", ".")

            print(f"\r{Fore.YELLOW+Style.BRIGHT}[Balance]: {balance_before}", flush=True)
            print(f"{Fore.MAGENTA+Style.BRIGHT}[Tiket Game]: {balance_info['playPasses']}")
            # Periksa apakah 'farming' ada dalam balance_info sebelum mengaksesnya
            farming_info = balance_info.get('farming')
      
            if farming_info:

                end_time_ms = farming_info['endTime']
                end_time_s = end_time_ms / 1000.0
                end_utc_date_time = datetime.datetime.fromtimestamp(end_time_s, datetime.timezone.utc)
                current_utc_time = datetime.datetime.now(datetime.timezone.utc)
                time_difference = end_utc_date_time - current_utc_time
                hours_remaining = int(time_difference.total_seconds() // 3600)
                minutes_remaining = int((time_difference.total_seconds() % 3600) // 60)
                farming_balance = farming_info['balance']
                farming_balance_formated = f"{float(farming_balance):,.0f}".replace(",", ".")
                print(f"{Fore.RED+Style.BRIGHT}[ Claim Balance ] : {hours_remaining} jam {minutes_remaining} menit | Balance: {farming_balance_formated}")

                if hours_remaining < 0:
                    print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Claiming balance...", end="", flush=True)
                    claim_response = claim_balance(token)
                    if claim_response:
                        print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Claimed: {claim_response['availableBalance']}                ", flush=True)
                        print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Starting farming...", end="", flush=True)
                        start_response = start_farming(token)
                        if start_response:
                            print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Farming started.", flush=True)
                        else:
                            print(f"\r{Fore.RED+Style.BRIGHT}[ Claim Balance ] : Gagal start farming", start_response.status_code, flush=True)
                    else:
                        print(f"\r{Fore.RED+Style.BRIGHT}[ Claim Balance ] : Gagal claim", claim_response.status_code, flush=True)
            else:
                print(f"\n{Fore.RED+Style.BRIGHT}[ Claim Balance ] : Gagal mendapatkan informasi farming", flush=True)
                print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Claiming balance...", end="", flush=True)
                claim_response = claim_balance(token)
                if claim_response:
                    print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Claimed               ", flush=True)
                    print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Starting farming...", end="", flush=True)
                    start_response = start_farming(token)
                    if start_response:
                        print(f"\r{Fore.GREEN+Style.BRIGHT}[ Claim Balance ] : Farming started.", flush=True)
                    else:
                        print(f"\r{Fore.RED+Style.BRIGHT}[ Claim Balance ] : Gagal start farming", start_response.status_code, flush=True)
                else:
                    print(f"\r{Fore.RED+Style.BRIGHT}[ Claim Balance ] : Gagal claim", claim_response.status_code, flush=True)

        # cek daily 
        print(f"\r{Fore.CYAN+Style.BRIGHT}[ Daily Reward ] : Checking daily reward...", end="", flush=True)
        daily_reward_response = check_daily_reward(token)
        # print(daily_reward_response)
        if daily_reward_response is None:
            print(f"\r{Fore.RED+Style.BRIGHT}[ Daily Reward ] : Gagal cek hadiah harian", flush=True)
        else:
        
            if daily_reward_response.get('message') == 'same day':
                print(f"\r{Fore.CYAN+Style.BRIGHT}[ Daily Reward ] : Hadiah harian sudah diklaim hari ini", flush=True)
            elif daily_reward_response.get('message') == 'OK':
                print(f"\r{Fore.CYAN+Style.BRIGHT}[ Daily Reward ] : Hadiah harian berhasil diklaim!", flush=True)
            else:
                print(f"\r{Fore.RED+Style.BRIGHT}[ Daily Reward ] : Gagal cek hadiah harian. {daily_reward_response}", flush=True)
        # print(daily_reward_response)
        # cek task 
        if cek_task_enable == 'y':
            if query_id not in checked_tasks or not checked_tasks[query_id]:
                print(f"\r{Fore.YELLOW+Style.BRIGHT}Checking tasks...\n", end="", flush=True)
                check_tasks(token)
                checked_tasks[query_id] = True

        
        print(f"\r{Fore.YELLOW+Style.BRIGHT}[ Reff Balance ] : Checking reff balance...", end="", flush=True)
        friend_balance = check_balance_friend(token)
        if friend_balance:
            if friend_balance['canClaim']:
                print(f"\r{Fore.GREEN+Style.BRIGHT}Reff Balance: {friend_balance['amountForClaim']}", flush=True)
                print(f"\n\r{Fore.GREEN+Style.BRIGHT}Claiming Ref balance.....", flush=True)
                claim_friend_balance = claim_balance_friend(token)
                if claim_friend_balance:
                    claimed_amount = claim_friend_balance['claimBalance']
                    print(f"\r{Fore.GREEN+Style.BRIGHT}[ Reff Balance ] : Sukses claim total: {claimed_amount}", flush=True)
                else:
                    print(f"\r{Fore.RED+Style.BRIGHT}[ Reff Balance ] : Gagal mengklaim saldo ref", flush=True)
            else:
                # Periksa apakah 'canClaimAt' ada sebelum mengaksesnya
                can_claim_at = friend_balance.get('canClaimAt')
                if can_claim_at:
                    claim_time = datetime.datetime.fromtimestamp(int(can_claim_at) / 1000)
                    current_time = datetime.datetime.now()
                    time_diff = claim_time - current_time
                    hours, remainder = divmod(int(time_diff.total_seconds()), 3600)
                    minutes, seconds = divmod(remainder, 60)
                    print(f"{Fore.RED+Style.BRIGHT}\r[ Reff Balance ] : Klaim pada {hours} jam {minutes} menit lagi", flush=True)
                else:
                    print(f"{Fore.RED+Style.BRIGHT}\r[ Reff Balance ] : False                                 ", flush=True)
        else:
            print(f"{Fore.RED+Style.BRIGHT}\r[ Reff Balance ] : Gagal cek reff balance", flush=True)
        available_colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]

        while balance_info['playPasses'] > 0:
            print(f"{Fore.CYAN+Style.BRIGHT}[ Play Game ] : Playing game...")
            game_response = play_game(token)
            print(f"\r{Fore.CYAN+Style.BRIGHT}[ Play Game ] : Checking game...", end="", flush=True)
            time.sleep(1)
            claim_response = claim_game(token, game_response['gameId'], 2000)
            if claim_response is None:
                print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] : Gagal mengklaim game, mencoba lagi...", flush=True)
            while True:
                if claim_response.text == '{"message":"game session not finished"}':
                    time.sleep(1)  # Tunggu sebentar sebelum mencoba lagi
                    random_color = random.choice(available_colors)
                    print(f"\r{random_color+Style.BRIGHT}[ Play Game ] : Game belum selesai.. mencoba lagi", flush=True)
                    claim_response = claim_game(token, game_response['gameId'], 2000)
                    if claim_response is None:
                        print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] : Gagal mengklaim game, mencoba lagi...", flush=True)
                elif claim_response.text == '{"message":"game session not found"}':
                    print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] : Game sudah berakhir", flush=True)
                    break
                elif 'message' in claim_response and claim_response['message'] == 'Token is invalid':
                    print(f"{Fore.RED+Style.BRIGHT}[ Play Game ] : Token tidak valid, mendapatkan token baru...")
                    token = get_new_token(query_id)  # Asumsi query_id tersedia di scope ini
                    continue  # Kembali ke awal loop untuk mencoba lagi dengan token baru
                else:
                    print(f"\r{Fore.YELLOW+Style.BRIGHT}[ Play Game ] : Game selesai: {claim_response.text}", flush=True)
                    break
            # Setelah klaim game, cek lagi jumlah tiket
            balance_info = get_balance(token) 
            if balance_info is None: # Refresh informasi saldo untuk mendapatkan tiket terbaru
                print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] Gagal mendapatkan informasi tiket", flush=True)
            else:
                available_balance_after = balance_info['availableBalance']  # asumsikan ini mengambil nilai dari JSON
                before = float(available_balance_before) 
                after =  float(available_balance_after)
                # balance_after = f"{float(available_balance):,.0f}".replace(",", ".")
                total_balance = after - before  # asumsikan ini mengambil
                print(f"\r{Fore.YELLOW+Style.BRIGHT}[ Play Game ]: You Got Total {total_balance} From Playing Game", flush=True)
                if balance_info['playPasses'] > 0:
                    print(f"\r{Fore.GREEN+Style.BRIGHT}[ Play Game ] : Tiket masih tersedia, memainkan game lagi...", flush=True)
                    continue  # Lanjutkan loop untuk memainkan game lagi
                else:
                    print(f"\r{Fore.RED+Style.BRIGHT}[ Play Game ] : Tidak ada tiket tersisa.", flush=True)
                    break

        
    print(f"\n{Fore.GREEN+Style.BRIGHT}========={Fore.WHITE+Style.BRIGHT}Semua akun berhasil di proses{Fore.GREEN+Style.BRIGHT}=========", end="", flush=True)
    print(f"\r\n\n{Fore.GREEN+Style.BRIGHT}Refreshing token...", end="", flush=True)
    import sys
    waktu_tunggu = 300  # 5 menit dalam detik
    for detik in range(waktu_tunggu, 0, -1):
        sys.stdout.write(f"\r{Fore.CYAN}Menunggu waktu claim berikutnya dalam {Fore.CYAN}{Fore.WHITE}{detik // 60} menit {Fore.WHITE}{detik % 60} detik")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\rWaktu claim berikutnya telah tiba!                                                          \n")


