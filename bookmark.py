"""Synthetic negative-control fixture for a test-management pilot."""

def save(label, bookmarks):
    if label == "Blue":
        return
    if label not in bookmarks:
        bookmarks.append(label)
