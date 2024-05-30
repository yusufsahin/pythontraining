import subprocess

def run_dir_command_and_capture_output():
    result = subprocess.run(['dir'],shell=True,capture_output=True,text=True)
    print(f"Çıkış Kodu: {result.returncode}")

    # Komutun standart çıktısını yazdır
    print(f"Çıktı:\n{result.stdout.strip()}")

    # Komutun standart hatasını yazdır (varsa)
    if result.stderr:
        print(f"Hata: {result.stderr.strip()}")

if __name__ == '__main__':
    run_dir_command_and_capture_output()