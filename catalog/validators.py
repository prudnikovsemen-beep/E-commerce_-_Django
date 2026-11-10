from django.core.exceptions import ValidationError

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5 МБ


def validate_file_size(image):
    if image.size > MAX_FILE_SIZE:
        raise ValidationError(
            f'Размер файла не должен превышать 5 МБ. '
            f'Ваш файл весит {image.size // 1024} КБ.'
        )
