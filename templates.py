import cv2
from typing import TypedDict


class Template(TypedDict):
    name: str
    image: str


buy_button_covenant: Template = {
    "image": cv2.imread('images/Buy_button_Covenant.png', 0),
    "name": "buy_button_covenant"
}
buy_button_mystic: Template = {
    "image": cv2.imread('images/Buy_button_Mystic.png', 0),
    "name": "buy_button_mystic"
}
confirm_button: Template = {
    "image": cv2.imread('images/confirm_button.png', 0),
    "name": "confirm_button"
}
covenant: Template = {
    "image": cv2.imread('images/covenant.png', 0),
    "name": "covenant"
}
mystic: Template = {
    "image": cv2.imread('images/mystic.png', 0),
    "name": "mystic"
}
refresh_button: Template = {
    "image": cv2.imread('images/refresh_button.png', 0),
    "name": "refresh_button"
}
