class FileInfo:
    def __init__(self,
                 file_name: str,
                 full_path: str,
                 size: int,
                 last_modified_at: str) -> None:
        self.file_name = file_name
        self.full_path = full_path
        self.size = size
        self.last_modified_at = last_modified_at
