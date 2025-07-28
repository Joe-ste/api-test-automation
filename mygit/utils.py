"""
Utility functions for the Git-like version control system.

This module contains helper functions that you'll find useful during implementation.
"""

import hashlib
import zlib
from pathlib import Path
from typing import Dict, List, Optional


def calculate_sha1(data: bytes) -> str:
    """
    Calculate SHA-1 hash of data.
    
    This is a helper function you can use for generating object IDs.
    """
    return hashlib.sha1(data).hexdigest()


def compress_data(data: bytes) -> bytes:
    """
    Compress data using zlib (like Git does).
    
    Git stores objects compressed with zlib.
    """
    return zlib.compress(data)


def decompress_data(compressed_data: bytes) -> bytes:
    """
    Decompress data using zlib.
    
    Use this to read Git objects from disk.
    """
    return zlib.decompress(compressed_data)


def find_repository_root(start_path: Path) -> Optional[Path]:
    """
    Find the root of a Git repository by looking for .git directory.
    
    Walks up the directory tree until it finds a .git directory.
    Returns None if no repository is found.
    """
    current = start_path.resolve()
    
    while current != current.parent:
        git_dir = current / ".git"
        if git_dir.exists() and git_dir.is_dir():
            return current
        current = current.parent
    
    return None


def get_file_hash(file_path: Path) -> str:
    """
    Calculate SHA-1 hash of a file's content.
    
    Useful for detecting file changes.
    """
    with open(file_path, 'rb') as f:
        content = f.read()
    return calculate_sha1(content)


def create_directory_structure(base_path: Path, directories: List[str]) -> None:
    """
    Create a directory structure under base_path.
    
    Useful for initializing the .git directory structure.
    """
    for directory in directories:
        (base_path / directory).mkdir(parents=True, exist_ok=True)


def read_file_safely(file_path: Path) -> Optional[bytes]:
    """
    Safely read a file, returning None if it doesn't exist.
    
    Useful for reading optional files like .git/index.
    """
    try:
        with open(file_path, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        return None


def write_file_safely(file_path: Path, data: bytes) -> None:
    """
    Safely write data to a file, creating parent directories if needed.
    
    Useful for writing Git objects and other files.
    """
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, 'wb') as f:
        f.write(data)


def format_commit_message(commit_hash: str, author: str, timestamp: str, message: str) -> str:
    """
    Format a commit message for display (like git log).
    
    Useful for the log command.
    """
    return f"commit {commit_hash}\nAuthor: {author}\nDate: {timestamp}\n\n    {message}\n"


def detect_file_changes(repo_path: Path, file_path: str, staged_hash: str) -> Dict[str, str]:
    """
    Detect changes in a file compared to its staged version.
    
    Returns a dictionary with change information.
    Useful for the status command.
    """
    full_path = repo_path / file_path
    
    if not full_path.exists():
        return {"status": "deleted"}
    
    current_hash = get_file_hash(full_path)
    
    if current_hash == staged_hash:
        return {"status": "unchanged"}
    else:
        return {"status": "modified", "old_hash": staged_hash, "new_hash": current_hash}


def list_untracked_files(repo_path: Path, tracked_files: List[str]) -> List[str]:
    """
    Find files in the working directory that aren't tracked.
    
    Useful for the status command.
    """
    untracked = []
    
    for item in repo_path.rglob("*"):
        if item.is_file():
            # Convert to relative path
            rel_path = str(item.relative_to(repo_path))
            
            # Skip .git directory
            if rel_path.startswith(".git/"):
                continue
                
            # Skip if already tracked
            if rel_path not in tracked_files:
                untracked.append(rel_path)
    
    return untracked