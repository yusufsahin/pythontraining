import subprocess

def run_command_and_capture_output():
    result=subprocess.run(['echo', 'Hello, World!'], capture_output=True, text=True,shell=True)
    print(f"Çıkış Kodu: {result.returncode} ")
    print(result.stdout.strip())
    if result.stderr:
        print(f"Hata: {result.stderr.strip()}")
if __name__ == '__main__':
    run_command_and_capture_output()