from pathlib import Path


def validation_path(path: str | Path, exists_check: bool = False, parents_mkdir: bool = False) -> Path:
    if isinstance(path, str | Path):
        path_ = Path(path)
    else:
        raise TypeError("パスの形式で頼みます。")

    if not isinstance(exists_check, bool) or not isinstance(parents_mkdir, bool):
        raise TypeError("boolで")

    if parents_mkdir:
        path_.parent.mkdir(parents=True, exist_ok=True)

    if exists_check and not path_.exists():
        raise FileNotFoundError("ファイルがありません。")

    return path_


def validation_path_list(path_list: list[str | Path], exists_check: bool = False, parents_mkdir: bool = False):
    path_list_ = []
    for path in path_list:
        path_ = validation_path(path, exists_check=exists_check, parents_mkdir=parents_mkdir)
        path_list_.append(path_)

    return path_list_
