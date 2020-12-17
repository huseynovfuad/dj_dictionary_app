from django.db.utils import IntegrityError
from contextlib import suppress

from pathlib import Path

from django.core.management.base import BaseCommand

from google_trans_new import google_translator

from dictapp.models import WordTranslate,Word


class Command(BaseCommand):
    def handle(self, *args, **options):
        english_words = Path(
            "words/english.txt"
        ).open()
        for word in english_words.readlines():
            with suppress(IntegrityError):
                en_word, en_created = Word.objects.get_or_create(
                    word=self.clean_word(word), language="en"
                )
                if en_created:
                    az_word, __ = Word.objects.get_or_create(
                        word=google_translator()
                            .translate(self.clean_word(word),lang_tgt="az")
                            .lower(),
                        language="az",
                    )
                    translate, created = WordTranslate.objects.get_or_create(
                        source=en_word, target=az_word
                    )
                    if created:
                        self.stdout.write(
                            self.style.SUCCESS(
                                f"Successfully created {translate}"
                            )
                        )

    @staticmethod
    def clean_word(word):
        return word.strip()
