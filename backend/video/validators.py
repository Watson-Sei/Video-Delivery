import os
from django.core.exceptions import ValidationError


def validate_is_video(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in ['.mp4']:
        raise ValidationError('mp4などの動画形式だけです。')


def validate_is_thumbnail(value):
    ext = os.path.splitext(value.name)[1]

    if not ext.lower() in ['.jpg', '.png', '.svg']:
        raise ValidationError('jpg,png,svgなどの画像形式だけです。')
