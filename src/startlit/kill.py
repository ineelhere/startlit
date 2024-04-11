import subprocess
def kill_streamlit_apps(pids_string):
    """Kill the Streamlit apps based on their process IDs.

    Args:
        pids_string (str): A string containing process IDs (PIDs) separated by spaces.
    """
    try:
        # Use the taskkill command to kill all processes in the provided string of PIDs
        subprocess.run(["taskkill", "/F", "/PID", pids_string], check=True)
        print(f"Successfully killed processes with PIDs: {pids_string} 🔪")
    except subprocess.CalledProcessError:
        print(f"Failed to kill processes with PIDs: {pids_string} 😓")

# Example usage
if __name__ == "__main__":
    # Get the list of running Streamlit apps
    running_apps = list_streamlit_apps()
    
    if not running_apps.empty:
        # Extract PIDs of the running Streamlit apps
        pids = running_apps["PID"].tolist()
        
        # Convert the list of PIDs to a string, separated by spaces
        pids_string = " ".join(map(str, pids))
        
        # Kill the Streamlit apps
        kill_streamlit_apps(pids_string)
