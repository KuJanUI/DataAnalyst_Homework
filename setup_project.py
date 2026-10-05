from pathlib import Path

REQUIRED_FOLDERS = [
    "notebooks",
    "data/raw",
    "data/processed",
    "figures",
]


def create_project_folders(folders: list) -> dict:
    """Create each folder if it does not exist, and report what happened.

    Parameters
    ----------
    folders : list
        Relative folder paths to create.

    Returns
    -------
    dict
        Maps folder path -> 'created' or 'already existed'.
    """
    report = {}
    for folder in folders:
        path = Path(folder)
        existed = path.exists()

        path.mkdir(parents=True, exist_ok=True)

        report[folder] = "already existed" if existed else "created"
    return report


result = create_project_folders(REQUIRED_FOLDERS)
for folder, status in result.items():
    print(f"{folder:<20} {status}")