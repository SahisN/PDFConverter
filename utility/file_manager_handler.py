import subprocess
import sys


# detects which platform user is on and opens specific file manager of that platform
class FileManagerHandler:
    def __init__(self, path: str):
        self.path = self._convert_path(path)

        # opening windows file explorer
        if sys.platform.startswith("win"):
            subprocess.Popen(["explorer", self.path])

        # opening linux file manager
        if sys.platform.startswith("linux"):
            subprocess.Popen(["xdg-open", self.path])

        # opening mac finder
        if sys.platform.startswith("darwin"):
            subprocess.Popen(["open", self.path])

    def _convert_path(self, path: str) -> str:
        last_slash_index = path.rfind("/")
        path = path[:last_slash_index]

        return path.replace("/", "\\")
