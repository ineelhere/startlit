import subprocess
import shutil
import os
import tempfile

# Reference dictionary mapping keywords to folder names
def get_folder_description(key):
    folder_mapping = {
        'chat_app': 'Chat app using Snowflake Cortex',
        'email_generator': 'LLM Email Generator',
        'ci_demo': 'Continuous Integration - Summit Demo',
        'customer_engagement': 'Customer Engagement App',
        'rag': 'Retrieval Augmented Generation (RAG)',
        'external_access_chat_app': 'External Access: Chat app using 3rd party LLM',
        'github_insights': 'Github Popularity Insights',
        'h3_mapping': 'H3 Mapping and Timeseries Visualization',
        'sql_optimizer': 'SQL Query Optimizer App using Snowflake Cortex',
        'inventory_tracker': 'Inventory Tracker',
        'usage_monitoring': 'Streamlit in Snowflake Usage Monitoring',
        'metrics_app': 'Key Metrics App',
        'retention_analytics': 'User Retention Analytics App',
        'language_insights': 'Language Usage Insights',
        'data_io': 'Writing and reading data back to Snowflake'
    }
    return folder_mapping.get(key, "Key not found in folder_mapping")

def snowflake_demo_app(keyword, dest_dir):
    repo_url = "https://github.com/Snowflake-Labs/snowflake-demo-streamlit.git"
    branch_name = 'main'
    # Look up the full folder name from the mapping
    folder_name = get_folder_description(keyword)
    if folder_name is None:
        print(f"Keyword '{keyword}' not found in the reference dictionary. ❌")
        return

    print(f"Cloning from {repo_url} 📦")
    print(f"Using the {branch_name} branch 🌿")

    with tempfile.TemporaryDirectory() as temp_dir:
        # Clone the repository into a temporary directory
        subprocess.run(['git', 'clone', '--branch', branch_name, '--single-branch', '--depth', '1', repo_url, temp_dir], check=True)

        # Ensure the clone directory exists
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
            print(f"Target directory created: {dest_dir} 🛠️")

        # Define the paths for the folder, LICENSE, and README.md
        folder_path = os.path.join(temp_dir, folder_name)
        license_path = os.path.join(temp_dir, 'LICENSE')
        readme_path = os.path.join(temp_dir, 'README.md')

        # Copy the specified folder
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            shutil.copytree(folder_path, os.path.join(dest_dir, folder_name), dirs_exist_ok=True)
            print(f"Fetched folder: {folder_name} 📁")
        else:
            print(f"Folder {folder_name} not found in the repository. ❌")

        # Copy LICENSE if it exists
        if os.path.exists(license_path):
            shutil.copy2(license_path, os.path.join(dest_dir, 'LICENSE'))
            print("Fetched LICENSE file 📜")

        # Copy README.md if it exists
        if os.path.exists(readme_path):
            shutil.copy2(readme_path, os.path.join(dest_dir, 'README.md'))
            print("Fetched README.md file 📖")

    print(f"Demo app files fetched successfully to {os.path.abspath(dest_dir)} 🎉🎊")
    print("Please make sure to read the README.md 📖 and LICENSE 📜 files for important information.")

