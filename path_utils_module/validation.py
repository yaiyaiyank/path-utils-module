from pathlib import Path


def validation_path(
    path: Path | str, exists_check: bool = False, not_exists_check: bool = False, parents_mkdir: bool = False
) -> Path:
    if isinstance(path, Path | str):
        path_ = Path(path)
    else:
        raise TypeError("パスの形式で頼みます。")

    if (
        not isinstance(exists_check, bool)
        or not isinstance(parents_mkdir, bool)
        or not isinstance(not_exists_check, bool)
    ):
        raise TypeError("boolで")

    if parents_mkdir:
        path_.parent.mkdir(parents=True, exist_ok=True)

    if exists_check and not path_.exists():
        raise FileNotFoundError(f"パス: {path_} が存在していません。")

    if not_exists_check and path_.exists():
        raise FileNotFoundError(f"パス: {path_} が存在しています。")

    return path_


def validation_path_list(
    path_list: Path | str | list[Path | str], exists_check: bool = False, parents_mkdir: bool = False
):
    path_list_ = []
    # リスト化
    if not isinstance(path_list, list):
        path_list = [path_list]
    # 各要素をバリデーション
    for path in path_list:
        path_ = validation_path(path, exists_check=exists_check, parents_mkdir=parents_mkdir)
        path_list_.append(path_)

    return path_list_
