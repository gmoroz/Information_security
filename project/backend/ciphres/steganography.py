from stegano import exifHeader
from faker import Faker
from project.backend.constants import UPLOAD_FOLDER


def image_encode(img_path, message: str) -> str:
    fake = Faker()
    shifred_img = UPLOAD_FOLDER + f"/{fake.unique.password(special_chars=False)}.jpg"
    exifHeader.hide(img_path, shifred_img, message)
    return shifred_img


def image_decode(shifred_img):
    return exifHeader.reveal(shifred_img).decode()
