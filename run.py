import os
import sys
import subprocess
import urllib.request
import zipfile
import tarfile
import shutil
import platform

NODE_VERSION = "v20.12.2" # Current LTS Version

def get_node_info():
    system = platform.system().lower()
    machine = platform.machine().lower()
    
    if system == "windows":
        ext = "zip"
        os_name = "win"
        arch = "x64" if "64" in machine else "x86"
    elif system == "darwin":
        ext = "tar.gz"
        os_name = "darwin"
        arch = "arm64" if machine == "arm64" else "x64"
    else: # linux
        ext = "tar.gz"
        os_name = "linux"
        if "arm" in machine or "aarch" in machine:
            arch = "arm64" if "64" in machine else "armv7l"
        else:
            arch = "x64"
            
    url = f"https://nodejs.org/dist/{NODE_VERSION}/node-{NODE_VERSION}-{os_name}-{arch}.{ext}"
    folder_name = f"node-{NODE_VERSION}-{os_name}-{arch}"
    return url, folder_name, ext

def check_system_node():
    npm_cmd = "npm.cmd" if platform.system().lower() == "windows" else "npm"
    try:
        subprocess.run(["node", "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        subprocess.run([npm_cmd, "--version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def download_and_extract_node(local_node_dir):
    url, folder_name, ext = get_node_info()
    download_path = os.path.join(local_node_dir, f"node_archive.{ext}")
    
    print(f"Node.js not found on system. Downloading portable Node.js {NODE_VERSION} locally from {url}...")
    
    # Download
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response, open(download_path, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    print("Download complete. Extracting...")
    
    # Extract
    if ext == "zip":
        with zipfile.ZipFile(download_path, 'r') as zip_ref:
            zip_ref.extractall(local_node_dir)
    else:
        with tarfile.open(download_path, 'r:gz') as tar_ref:
            tar_ref.extractall(local_node_dir)
            
    os.remove(download_path)
    
    # Move files from the nested folder to local_node_dir
    extracted_folder = os.path.join(local_node_dir, folder_name)
    for item in os.listdir(extracted_folder):
        s = os.path.join(extracted_folder, item)
        d = os.path.join(local_node_dir, item)
        shutil.move(s, d)
    
    os.rmdir(extracted_folder)
    print("Node.js setup complete in local project directory.")

def get_local_node_paths(local_node_dir):
    system = platform.system().lower()
    if system == "windows":
        node_exe = os.path.join(local_node_dir, "node.exe")
        npm_cmd = os.path.join(local_node_dir, "npm.cmd")
    else:
        node_exe = os.path.join(local_node_dir, "bin", "node")
        npm_cmd = os.path.join(local_node_dir, "bin", "npm")
        
        # Make them executable on unix Systems
        for p in [node_exe, npm_cmd]:
            if os.path.exists(p):
                os.chmod(p, 0o755)
                
    return node_exe, npm_cmd

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root_dir)
    
    local_node_dir = os.path.join(root_dir, ".local_node")
    
    # Check for system node
    if check_system_node():
        print("System Node.js found. Using it globally.")
        npm_cmd = "npm.cmd" if platform.system().lower() == "windows" else "npm"
    else:
        if not os.path.exists(local_node_dir):
            os.makedirs(local_node_dir)
            
        try:
            node_cmd, npm_cmd = get_local_node_paths(local_node_dir)
            if not os.path.exists(node_cmd):
                download_and_extract_node(local_node_dir)
        except Exception as e:
            print(f"Error setting up local Node.js: {e}")
            sys.exit(1)
        
        # Add local node to PATH for subprocesses
        bin_dir = local_node_dir if platform.system().lower() == "windows" else os.path.join(local_node_dir, "bin")
        os.environ["PATH"] = bin_dir + os.pathsep + os.environ.get("PATH", "")
        print("Using portable local Node.js.")

    # Ignore .local_node in git
    gitignore_path = os.path.join(root_dir, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as f:
            if ".local_node" not in f.read():
                with open(gitignore_path, "a") as fw:
                    fw.write("\n.local_node\n")

    # Install dependencies
    print("\n--- Installing Project Dependencies ---")
    try:
        subprocess.run([npm_cmd, "install"], check=True)
    except Exception as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)
    
    # Run the project
    print("\n--- Starting the Application ---")
    print("Once it says 'Ready in ... ms', open the indicated URL (usually http://localhost:5173/) in your web browser.")
    try:
        subprocess.run([npm_cmd, "run", "dev"])
    except KeyboardInterrupt:
        print("\nApplication stopped by user.")

if __name__ == "__main__":
    main()
