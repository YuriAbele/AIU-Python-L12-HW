class FileInfo:
    def __init__(self,
                 file_name: str,
                 full_path: str,
                 size: int,
                 last_modified_at: str,
                 hash: str | None) -> None:
        self.file_name = file_name
        self.full_path = full_path
        self.size = size
        self.last_modified_at = last_modified_at
        self.hash = hash
        
    def __str__(self) -> str:
        return self.__repr__()
        
    def __repr__(self) -> str:
        return f"FileInfo(full_path='{self.full_path}', file_name='{self.file_name}', size={self.size}, last_modified_at='{self.last_modified_at}', hash='{self.hash}')"
