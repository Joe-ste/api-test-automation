"""
Core classes for the Git-like version control system.

This module contains the fundamental classes that you'll need to implement:
- Repository: Manages the .git directory and repository state
- Index: Tracks staged files (like Git's staging area)
- Commit: Represents a commit with metadata and content
- Object: Base class for Git objects (commits, trees, blobs)
"""

import os
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any


class GitObject:
    """
    Base class for all Git objects (commits, trees, blobs).
    
    TODO: Implement this class to handle:
    - Object serialization/deserialization
    - SHA-1 hash generation
    - Object storage and retrieval from .git/objects
    """
    
    def __init__(self, content: Any):
        self.content = content
        self.oid = None  # Object ID (SHA-1 hash)
    
    def serialize(self) -> bytes:
        """
        Convert object to bytes for storage.
        
        TODO: Implement serialization logic
        """
        raise NotImplementedError("You need to implement this!")
    
    def deserialize(self, data: bytes) -> None:
        """
        Load object from bytes.
        
        TODO: Implement deserialization logic
        """
        raise NotImplementedError("You need to implement this!")
    
    def save(self, repo_path: Path) -> str:
        """
        Save object to .git/objects and return its OID.
        
        TODO: Implement object storage logic
        """
        raise NotImplementedError("You need to implement this!")
    
    @classmethod
    def load(cls, repo_path: Path, oid: str) -> 'GitObject':
        """
        Load object from .git/objects by OID.
        
        TODO: Implement object loading logic
        """
        raise NotImplementedError("You need to implement this!")


class Blob(GitObject):
    """
    Represents a file's content in the repository.
    
    TODO: Implement blob-specific logic
    """
    pass


class Tree(GitObject):
    """
    Represents a directory structure with references to blobs and other trees.
    
    TODO: Implement tree-specific logic
    """
    pass


class Commit(GitObject):
    """
    Represents a commit with metadata and a tree reference.
    
    TODO: Implement commit-specific logic including:
    - Author and committer information
    - Commit message
    - Parent commit references
    - Tree reference
    """
    
    def __init__(self, tree_oid: str, parent_oids: List[str], 
                 author: str, message: str):
        super().__init__(None)
        self.tree_oid = tree_oid
        self.parent_oids = parent_oids
        self.author = author
        self.message = message
        self.timestamp = datetime.now()


class Index:
    """
    Represents the staging area (like Git's index).
    
    TODO: Implement staging area functionality:
    - Track staged files and their hashes
    - Handle file additions, modifications, deletions
    - Persist index to .git/index file
    """
    
    def __init__(self, repo_path: Path):
        self.repo_path = repo_path
        self.index_path = repo_path / ".git" / "index"
        self.staged_files: Dict[str, str] = {}  # path -> blob_oid
    
    def add_file(self, file_path: str) -> None:
        """
        Stage a file for commit.
        
        TODO: Implement file staging logic
        """
        raise NotImplementedError("You need to implement this!")
    
    def remove_file(self, file_path: str) -> None:
        """
        Remove a file from staging area.
        
        TODO: Implement file removal logic
        """
        raise NotImplementedError("You need to implement this!")
    
    def get_staged_files(self) -> Dict[str, str]:
        """
        Get all staged files.
        
        TODO: Implement staged files retrieval
        """
        raise NotImplementedError("You need to implement this!")
    
    def save(self) -> None:
        """
        Save index to disk.
        
        TODO: Implement index persistence
        """
        raise NotImplementedError("You need to implement this!")
    
    def load(self) -> None:
        """
        Load index from disk.
        
        TODO: Implement index loading
        """
        raise NotImplementedError("You need to implement this!")


class Repository:
    """
    Manages a Git repository.
    
    TODO: Implement repository management:
    - Initialize new repository
    - Track working directory
    - Handle commits and branches
    - Manage .git directory structure
    """
    
    def __init__(self, path: Path):
        self.path = path
        self.git_path = path / ".git"
        self.index = Index(self.path)
        
    @classmethod
    def init(cls, path: Path) -> 'Repository':
        """
        Initialize a new repository.
        
        TODO: Implement repository initialization:
        - Create .git directory structure
        - Initialize index
        - Set up initial HEAD reference
        """
        raise NotImplementedError("You need to implement this!")
    
    def add(self, file_path: str) -> None:
        """
        Stage a file for commit.
        
        TODO: Implement file staging
        """
        raise NotImplementedError("You need to implement this!")
    
    def commit(self, message: str, author: str = "Unknown") -> str:
        """
        Create a new commit.
        
        TODO: Implement commit creation:
        - Create tree from staged files
        - Create commit object
        - Update HEAD reference
        - Clear staging area
        """
        raise NotImplementedError("You need to implement this!")
    
    def log(self) -> List[Commit]:
        """
        Show commit history.
        
        TODO: Implement commit history display
        """
        raise NotImplementedError("You need to implement this!")
    
    def status(self) -> Dict[str, Any]:
        """
        Show repository status.
        
        TODO: Implement status checking:
        - Show staged files
        - Show unstaged changes
        - Show untracked files
        """
        raise NotImplementedError("You need to implement this!")