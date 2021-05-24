from concurrent.futures import ThreadPoolExecutor
import timeit
import requests

def download(url):
    image_bytes = requests.get(url).content
    image_name = ("{}.jpg".format(url.split("/")[-1]))

    with open(image_name, "wb") as file:
        file.write(image_bytes)
        print(f"Downloaded {image_name}")

def thread_image():
    
    urls = [
        "https://images.unsplash.com/photo-1621860088759-9027f133fc3d",
        "https://images.unsplash.com/photo-1621786505687-9a36ca978b27",
        "https://images.unsplash.com/photo-1621854029362-5d66c3e0c306",
        "https://images.unsplash.com/photo-1621748339022-9744a069b1c8",
        "https://images.unsplash.com/photo-1621849400072-f554417f7051",
        "https://images.unsplash.com/photo-1611095970111-fc87b5315dc3",
        "https://images.unsplash.com/photo-1621795817359-4d032a4af17a",
        "https://images.unsplash.com/photo-1621826389794-59a7d9366246",
        "https://images.unsplash.com/photo-1621832988726-b4738c7ceb76",
        "https://images.unsplash.com/photo-1621757458931-a1b076e5a8bb"
    ]

    with ThreadPoolExecutor(max_workers=len(urls)/2) as exec:
        print("Starting the download")
        exec.map(download, urls)
    # for i in urls:
    #     download(i)


if __name__ == '__main__':
    time_taken = timeit.timeit(thread_image, number=1)
    print(time_taken)