ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}


def validate_photo(photo):

    if not photo or not photo.filename:
        return None

    if "." not in photo.filename:
        return "Le fichier photo est invalide."

    extension = photo.filename.rsplit(".", 1)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        return "La photo doit être au format JPG, JPEG, PNG ou WEBP."

    return None