

import sys
import subprocess
import os
import platform
import shutil
from huggingface_hub import snapshot_download
import hf_transfer



snapshot_download(
            repo_id="MonsterMMORPG/Practical-RIFE",
            local_dir=f"framepack/Practical-RIFE/"
        )