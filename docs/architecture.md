# Architecture

```
main.py
    │
    ▼
tracker.py
    │
    ├────────► habits.py
    │
    ├────────► statistics.py
    │
    ├────────► storage.py
    │
    ├────────► report.py
    │
    └────────► ui/display.py
```

## Components

### Tracker

Coordinates the habit tracking session.

### Habits

Stores the habit collection.

### Statistics

Calculates completion metrics.

### Storage

Loads and saves habits.

### Report

Generates summary reports.

### UI

Displays information in the terminal.
