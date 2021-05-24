from concurrent.futures import ProcessPoolExecutor
import timeit
from PIL import Image

def resize(image):
    image_name = image+".jpg"
    img = Image.open(image_name)
    img.thumbnail((1200,1200))
    img.save(f'resized/{image_name}')
    print(f"{image_name} was resized")


def process_image():

    images = [
        "photo-1621860088759-9027f133fc3d",
        "photo-1621786505687-9a36ca978b27",
        "photo-1621854029362-5d66c3e0c306",
        "photo-1621748339022-9744a069b1c8",
        "photo-1621849400072-f554417f7051",
        "photo-1611095970111-fc87b5315dc3",
        "photo-1621795817359-4d032a4af17a",
        "photo-1621826389794-59a7d9366246",
        "photo-1621832988726-b4738c7ceb76",
        "photo-1621757458931-a1b076e5a8bb"
    ]

    with ProcessPoolExecutor() as exec:
        print("Resizing Images")
        exec.map(resize, images)

    # for i in images:
        # resize(i)
if __name__ == '__main__':
    time_taken = timeit.timeit(process_image, number=1)
    print(time_taken)