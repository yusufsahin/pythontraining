import subprocess
def run_command_with_pipe():
    p1 = subprocess.Popen('echo Hello, World!', stdout=subprocess.PIPE, shell=True)
    p2 = subprocess.Popen('findstr Hello', stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

    p1.stdout.close()

    output,error=p2.communicate()
    print(f"Çıktı:\n{output.strip()}")
    if error:
        print(f"Hata: {error.strip()}")

if __name__ == '__main__':
    run_command_with_pipe()