# Package initializer
# Personal fork: added version info for easier debugging
__version__ = "0.1.0-personal"
__author__ = "personal fork"
__all__ = ["__version__", "__author__"]

# Quick helper to print version info during debugging sessions
def version_info():
    """Print package version and author for quick identification."""
    print(f"openai-cs-agents-demo v{__version__} ({__author__})")
