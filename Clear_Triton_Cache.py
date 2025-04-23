import os
import shutil
from pathlib import Path
import sys
import tempfile

def clear_triton_cache():
    # Get the user's home directory dynamically
    home_dir = Path.home()
    
    # Define the path to the .triton cache folder
    triton_cache_path = home_dir / ".triton"
    
    print(f"Attempting to clear Triton cache at: {triton_cache_path}")
    
    # Check if the directory exists
    if not triton_cache_path.exists():
        print("Triton cache directory not found!")
        return False
    
    try:
        # List all items in the directory before deletion
        items = list(triton_cache_path.glob('*'))
        if not items:
            print("Triton cache is already empty.")
            return True
        
        print(f"Found {len(items)} items in the Triton cache.")
        
        # Remove all contents of the directory
        for item in items:
            if item.is_file():
                item.unlink()
                print(f"Deleted file: {item.name}")
            elif item.is_dir():
                shutil.rmtree(item)
                print(f"Deleted directory: {item.name}")
        
        print("Triton cache cleared successfully!")
        return True
    
    except Exception as e:
        print(f"Error occurred while clearing the cache: {e}")
        return False

def clear_temp_folder():
    # Get the Windows temp folder dynamically
    temp_path = Path(tempfile.gettempdir())
    
    print(f"Attempting to clear Windows temp folder at: {temp_path}")
    
    # Check if the directory exists
    if not temp_path.exists():
        print("Windows temp directory not found!")
        return False
    
    try:
        # List all items in the directory before deletion
        items = list(temp_path.glob('*'))
        if not items:
            print("Windows temp folder is already empty.")
            return True
        
        print(f"Found {len(items)} items in the Windows temp folder.")
        
        # Skip count for files that couldn't be deleted (likely in use)
        skipped = 0
        
        # Remove all contents of the directory
        for item in items:
            try:
                if item.is_file():
                    item.unlink()
                    print(f"Deleted file: {item.name}")
                elif item.is_dir():
                    shutil.rmtree(item)
                    print(f"Deleted directory: {item.name}")
            except PermissionError:
                #print(f"Skipped (in use): {item.name}")
                skipped += 1
            except Exception as e:
                print(f"Error with {item.name}: {e}")
                skipped += 1
        
        if skipped:
            print(f"Windows temp folder partially cleared. Skipped {skipped} items that were in use.")
        else:
            print("Windows temp folder cleared successfully!")
        return True
    
    except Exception as e:
        print(f"Error occurred while clearing the temp folder: {e}")
        return False

if __name__ == "__main__":
    clear_triton_cache()
    clear_temp_folder()
    input("Press Enter to exit...")