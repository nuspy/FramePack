import os
from huggingface_hub import snapshot_download

def main():
    print("Downloading pretrained_TripoSFVAE_256i1024o.safetensors from VAST-AI/TripoSF...")
    
    try:
        # Create the base directory structure first
        os.makedirs("TripoSF/ckpts", exist_ok=True)
        
        # Download directly into the TripoSF directory
        snapshot_download(
            repo_id="VAST-AI/TripoSF",
            allow_patterns=["vae/pretrained_TripoSFVAE_256i1024o.safetensors"],
            local_dir="TripoSF",
            local_dir_use_symlinks=False
        )
        
        # Move the file from TripoSF/vae/ to TripoSF/ckpts/
        source_path = "TripoSF/vae/pretrained_TripoSFVAE_256i1024o.safetensors"
        target_path = "TripoSF/ckpts/pretrained_TripoSFVAE_256i1024o.safetensors"
        
        if os.path.exists(source_path):
            # Make sure target directory exists
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            
            # Move the file
            os.rename(source_path, target_path)
            print(f"Successfully moved file to {target_path}")
            
            # Remove the now-empty vae directory
            if os.path.exists("TripoSF/vae") and not os.listdir("TripoSF/vae"):
                os.rmdir("TripoSF/vae")
        else:
            print(f"Warning: Expected file not found at {source_path}")
        
        print("Download complete.")
    
    except Exception as e:
        print(f"Error downloading file: {e}")
        
if __name__ == "__main__":
    main()