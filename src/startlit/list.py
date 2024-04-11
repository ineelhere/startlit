import subprocess
import pandas as pd

def list_streamlit_apps(port_start="85"):
    """List running Streamlit apps on localhost.

    This function scans the current processes for apps that are using TCP ports
    on the localhost and identifies those with ports starting with the specified number.
    If no starting number is provided, it uses '85' as the default.

    The function prints the running apps, if any, with their App ID and App URL.

    Args:
        port_start (str): The starting number for the port. Defaults to '85'.
    
    Returns:
        pd.DataFrame: A DataFrame containing App ID and App URL of the running Streamlit apps.
    """
    try:
        # Run the netstat command to get a list of apps listening on TCP ports
        netstat_output = subprocess.check_output(
            "netstat -aon",
            shell=True,
            stderr=subprocess.STDOUT,
            text=True
        )
        
        # Convert netstat output to a DataFrame
        lines = netstat_output.splitlines()
        data = []
        
        # Parse each line of the output
        for line in lines:
            if "TCP" in line and "LISTENING" in line:
                parts = line.split()
                local_address = parts[1]
                pid = int(parts[-1])
                
                # Extract port number from local address
                port = local_address.split(":")[-1]
                
                # Check if the port starts with the specified number
                if port.startswith(port_start):
                    data.append({"App ID": pid, "App URL": f"http://localhost:{port}"})
        
        # Convert data to DataFrame
        df = pd.DataFrame(data)
        
        # Remove duplicate rows based on 'App ID' and 'App URL' columns
        df = df.drop_duplicates(subset=["App ID", "App URL"])
        
        # Handle output printing
        if df.empty:
            print(f"Found no app running on ports starting with '{port_start}'! 😔")
        else:
            print(f"Running Streamlit apps on ports starting with '{port_start}': 😊")
            print(df)

    except subprocess.CalledProcessError as e:
        # Handle errors when executing netstat
        print(f"An error occurred while executing netstat: {e} 😓")
        return pd.DataFrame()

