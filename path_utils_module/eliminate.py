import re


def sanitize_windows_path_name(name: str) -> str:
    """Windowsでファイル名・フォルダー名に使えない文字を除去・変換する。"""
    windows_reserved_names = {
        "CON",
        "PRN",
        "AUX",
        "NUL",
        *(f"COM{i}" for i in range(1, 10)),
        *(f"LPT{i}" for i in range(1, 10)),
    }

    # 制御文字 (0x00～0x1F) と Windows で禁止されている文字を除去
    name = re.sub(r'[\x00-\x1f<>:"/\\|?*]', "", name)

    # 末尾のピリオド・半角スペースは使用不可
    name = name.rstrip(". ")

    # CON.txt のように拡張子付きでも予約名は使用不可
    stem = name.split(".", maxsplit=1)[0].upper()
    if stem in windows_reserved_names:
        name = f"{name}_"

    # 全部消えてしまった場合
    if not name:
        name = "_"

    return name
