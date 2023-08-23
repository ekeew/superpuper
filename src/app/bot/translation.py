from pathlib import Path

from fluent_compiler.bundle import FluentBundle
from fluentogram import TranslatorHub, FluentTranslator


def _get_ftl_files(locale_dir: Path) -> list[Path]:
    return [file for file in locale_dir.iterdir() if file.is_file() and file.suffix == ".ftl"]


def get_translator_hub(project_dir: Path) -> TranslatorHub:
    locales_dir = project_dir / "locales"
    translator_hub = TranslatorHub(
        {"ru": "ru", "en": "en"},
        [
            FluentTranslator("ru", FluentBundle.from_files("ru-RU", _get_ftl_files(locales_dir / "ru-RU"))),
            FluentTranslator("en", FluentBundle.from_files("en-US", _get_ftl_files(locales_dir / "en-US"))),
        ]
    )
    return translator_hub
