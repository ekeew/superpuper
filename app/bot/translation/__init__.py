from pathlib import Path

from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator


def _get_ftl_files(locale_dir: Path) -> list[Path]:
    return [file for file in locale_dir.iterdir() if file.suffix == ".ftl"]


def get_translator_hub() -> TranslatorHub:
    locales_dir = Path(__file__) / "locales"
    translation_hub = TranslatorHub(
        {"ru": "ru", "en": "en"},
        [
            FluentTranslator("ru", FluentBundle("ru-RU", _get_ftl_files(locales_dir / "ru"))),
            FluentTranslator("en", FluentBundle("en-US", _get_ftl_files(locales_dir / "en"))),
        ]
    )
    return translation_hub
