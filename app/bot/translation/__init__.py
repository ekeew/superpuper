from pathlib import Path

from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator


def get_translator_hub() -> TranslatorHub:
    locales_dir = Path(__file__).parent / "locales"
    translation_hub = TranslatorHub(
        {"ru": "ru", "en": "en"},
        [
            FluentTranslator("ru", FluentBundle("ru-RU", [locales_dir / "ru" / "main.ftl"])),
            FluentTranslator("en", FluentBundle("en-US", [locales_dir / "en" / "main.ftl"])),
        ]
    )
    return translation_hub
