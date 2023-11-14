import subprocess
import sys
import os
import time


def mac_id_check():
    # Define the nrfjprog command you want to run
    command = "nrfjprog --memrd 0x10000060 --n 8 --family nrf52"
    mac_id = ""

    # Run the command and capture the return code
    try:
        result = subprocess.run(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        mac_id = "F4CE36" + \
            result.stdout.split(" ")[1][6:] + result.stdout.split(" ")[2]
    except Exception as e:
        print("Cant Read macID with jprog")
        print("An error occurred:", e)
    return mac_id


def power_on():
    jlink_process = subprocess.Popen(
        "jlink", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send the "power on" command
    command = "power on\n"  # Add '\n' to simulate pressing Enter
    jlink_process.stdin.write(command)
    jlink_process.stdin.flush()

    # Read the response from J-Link (if needed)
    output, error = jlink_process.communicate()

    # Close the subprocess
    jlink_process.stdin.close()
    jlink_process.stdout.close()
    jlink_process.stderr.close()
    jlink_process.wait()


def power_off():
    jlink_process = subprocess.Popen(
        "jlink", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Send the "power on" command
    command = "power off\n"  # Add '\n' to simulate pressing Enter
    jlink_process.stdin.write(command)
    jlink_process.stdin.flush()

    # Read the response from J-Link (if needed)
    output, error = jlink_process.communicate()

    # Close the subprocess
    jlink_process.stdin.close()
    jlink_process.stdout.close()
    jlink_process.stderr.close()
    jlink_process.wait()


def flash_program(hex_name):
    erase_command = 'nrfjprog -e'
    result = subprocess.run(
        erase_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Define the nrfjprog command you want to run
    command = f"nrfjprog -f nrf52 --program ./{hex_name} --verify --hardreset"

    is_ok = 0

    # Run the command and capture the return code
    try:
        result = subprocess.run(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
        if "Verify file - Done verifying" in result.stdout:
            is_ok = 1
        else:
            is_ok = 0

    except Exception as e:
        print("Cant Read macID with jprog")
        print("An error occurred:", e)
    return is_ok


if __name__ == "__main__":
    # JLink_Power_On()
    pass
