"""Synthetic bookmark fixture for a test-management pilot."""

def save(label, bookmarks):
    if label not in bookmarks:
        bookmarks.append(label)
