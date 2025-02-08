def main():
    file_name = input("Enter the name of a file: ").strip()
    print(get_media_type(file_name))

def get_media_type(file_name):
    # Mapping of file extensions to media types
    media_types = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }

    # Extracting the file extension
    extension = file_name[file_name.rfind('.'):].lower()

    # Return the corresponding media type or a default value
    return media_types.get(extension, "application/octet-stream")
main()
