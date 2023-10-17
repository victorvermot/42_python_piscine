from imageio import read
from numpy import array
from pathlib import Path


def ft_load(path: str) -> array:
    exstention_accepted = [".jpg", ".jpeg", ".png"]
    file_extension = Path(path).suffix
    if file_extension not in exstention_accepted:
        raise AssertionError("File has wrong format")
    try:
        img = read(path)
    except FileNotFoundError:
        raise AssertionError("The file could not be found") from None
    res = array(img.get_data(0))
    print(f"""The shape of the image is:(
          {len(res)},
          {len(res[0])},
          {len(res[0][0])}
        )
        """)
    img.close()
    return res
