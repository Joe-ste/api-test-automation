# MyGit - A Git-like Version Control System

A learning project to understand how Git works by building a simplified version control system from scratch.

## 🎯 Learning Objectives

This project will teach you:

- **Data Structures**: Trees, graphs, hash tables
- **File Systems**: Working with files, directories, metadata
- **Algorithms**: Diff algorithms, merge algorithms, graph traversal
- **System Design**: Object storage, reference management
- **CLI Development**: Command-line interface design
- **Serialization**: Storing/loading objects efficiently

## 📁 Project Structure

```
mygit/
├── __init__.py          # Package initialization
├── core.py              # Core classes (Repository, Index, Commit, etc.)
├── cli.py               # Command-line interface
└── utils.py             # Helper functions
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7+
- Basic understanding of Python classes and file I/O

### Installation
```bash
# Clone or create the project
mkdir mygit-project
cd mygit-project

# The project structure is already set up for you!
```

## 📚 Implementation Guide

### Phase 1: Basic Repository Structure

Start by implementing the `Repository.init()` method in `core.py`:

```python
@classmethod
def init(cls, path: Path) -> 'Repository':
    """
    TODO: Your implementation here!
    
    Steps to implement:
    1. Create .git directory
    2. Create subdirectories: objects, refs, refs/heads
    3. Create initial HEAD file pointing to 'refs/heads/main'
    4. Initialize the Index
    5. Return a new Repository instance
    """
```

**Learning Points:**
- Directory structure management
- File system operations
- Basic repository initialization

### Phase 2: Object Storage System

Implement the `GitObject` base class:

```python
def serialize(self) -> bytes:
    """
    TODO: Convert object to bytes for storage
    
    Hint: Use the utils.calculate_sha1() function
    """

def save(self, repo_path: Path) -> str:
    """
    TODO: Save object to .git/objects and return OID
    
    Steps:
    1. Serialize the object
    2. Calculate SHA-1 hash
    3. Compress with zlib (use utils.compress_data())
    4. Save to .git/objects/{first_two_chars}/{remaining_chars}
    """
```

**Learning Points:**
- SHA-1 hashing
- Data compression
- File organization strategies

### Phase 3: Blob and Tree Objects

Implement the `Blob` class to store file contents:

```python
class Blob(GitObject):
    def serialize(self) -> bytes:
        """
        TODO: Serialize blob content
        
        Format: "blob {content_length}\0{content}"
        """
```

Implement the `Tree` class to represent directory structure:

```python
class Tree(GitObject):
    def __init__(self, entries: List[Dict]):
        """
        entries format: [{"mode": "100644", "name": "file.txt", "oid": "abc123"}]
        """
    
    def serialize(self) -> bytes:
        """
        TODO: Serialize tree entries
        
        Format: "tree {content_length}\0{entries}"
        Each entry: "{mode} {name}\0{oid_binary}"
        """
```

**Learning Points:**
- Binary data handling
- Tree data structures
- File mode and permissions

### Phase 4: Index (Staging Area)

Implement the `Index` class:

```python
def add_file(self, file_path: str) -> None:
    """
    TODO: Stage a file for commit
    
    Steps:
    1. Read file content
    2. Create Blob object
    3. Save blob to objects
    4. Add to staged_files dictionary
    5. Save index to disk
    """

def save(self) -> None:
    """
    TODO: Save index to .git/index
    
    Format: JSON or custom binary format
    """
```

**Learning Points:**
- Staging area concept
- File tracking
- State persistence

### Phase 5: Commit System

Implement the `Commit` class:

```python
def serialize(self) -> bytes:
    """
    TODO: Serialize commit data
    
    Format: "commit {content_length}\0{content}"
    Content: "tree {tree_oid}\nparent {parent_oid}\n...\nauthor {author}\n\n{message}"
    """
```

**Learning Points:**
- Commit metadata
- Parent-child relationships
- Graph traversal

### Phase 6: CLI Integration

Connect the CLI to your implementations:

```python
def handle_init(args):
    repo_path = Path(args.path)
    repo = Repository.init(repo_path)  # Your implementation!
    print("Repository initialized successfully!")

def handle_add(args):
    repo = Repository(find_repository_root(Path.cwd()))
    for file_path in args.files:
        repo.add(file_path)  # Your implementation!
```

## 🧪 Testing Your Implementation

Create test files to verify your implementation:

```python
# test_basic.py
from mygit.core import Repository
from pathlib import Path

# Test repository initialization
repo = Repository.init(Path("test_repo"))
assert (repo.path / ".git").exists()
assert (repo.path / ".git" / "objects").exists()

# Test file staging
with open("test_repo/test.txt", "w") as f:
    f.write("Hello, World!")
repo.add("test.txt")

# Test commit
commit_hash = repo.commit("Initial commit", "Test User")
print(f"Created commit: {commit_hash}")
```

## 🎓 Advanced Challenges

Once you have the basics working, try these advanced features:

1. **Branching**: Implement branch creation and switching
2. **Merging**: Handle merge conflicts and create merge commits
3. **Remote Operations**: Add push/pull functionality
4. **Diff Algorithm**: Implement file difference detection
5. **Graph Visualization**: Display commit history as a graph

## 💡 Tips for Success

1. **Start Small**: Begin with basic file operations before complex features
2. **Test Incrementally**: Test each component as you build it
3. **Use the Utils**: Leverage the helper functions in `utils.py`
4. **Study Git Internals**: Read about Git's object model and storage format
5. **Debug with Real Git**: Compare your output with actual Git commands

## 📖 Resources

- [Git Internals](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain)
- [Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects)
- [Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)

## 🤝 Getting Help

When you get stuck:
1. Check the TODO comments in the code
2. Use the utility functions provided
3. Test with simple examples first
4. Compare with actual Git behavior

Remember: The goal is learning, not perfection! Each implementation step teaches valuable concepts.

Happy coding! 🚀


