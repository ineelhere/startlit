import subprocess
def kill_streamlit_apps(pid_string):
    """Kill the Streamlit apps based on their process IDs.

    Args:
        pid_string (str): A string containing process IDs (PIDs) separated by spaces.
    """
    try:
        # Use the taskkill command to kill all processes in the provided string of PIDs
        subprocess.run(["taskkill", "/F", "/PID", pid_string], check=True)
        print(f"Successfully killed processes with PIDs: {pid_string} 🔪")
    except subprocess.CalledProcessError:
        print(f"Failed to kill processes with PIDs: {pid_string} 😓")
