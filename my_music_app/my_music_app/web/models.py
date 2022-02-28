
from django.core.validators import MinLengthValidator
from django.db import models

from my_music_app.web.validators import validate_username_chars, validate_age, validate_price


class Profile(models.Model):
    USERNAME_MIN_LENGTH = 2
    USERNAME_MAX_LENGTH = 15

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(USERNAME_MIN_LENGTH),
            validate_username_chars,
        ),
    )

    email = models.EmailField()

    age = models.IntegerField(
        null=True,
        blank=True,
        validators = (
            validate_age,
        )
    )


class Album(models.Model):
    ALBUM_MAX_LENGTH = 30
    ARTIST_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30

    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC= "Jazz Music"
    RB_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"

    GENRES = [(x, x) for x in (POP_MUSIC, JAZZ_MUSIC, RB_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER)]

    album_name = models.CharField(
        max_length=ALBUM_MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=ARTIST_MAX_LENGTH
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=GENRES,
    )

    description = models.TextField(
        null=True,
        blank=True
    )

    image_url = models.URLField()

    price = models.FloatField(
        validators=(
            validate_price,
        )
    )
