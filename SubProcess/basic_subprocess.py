# import subprocess

# # Run 'ls' command (on Linux/macOS)
# result = subprocess.run(['ls', '-l'])  

# print("Command finished with return code:", result.returncode)

import subprocess

result = subprocess.run(['echo', 'Hello subprocess!'], capture_output=True, text=True)

print("Output:", result.stdout)
print("Output:", result)