# Practicing MutliProcessing and Threading with concurrent.futures module

> concurrent.futures is builtin python module.

Previously used ***Threading*** and ***multiproccessing*** module to achieve the expected outcome.  
Their uses has been replaced with **concurrent.futures** with:
- ThreadPoolExecutor: for threading
- ProcessPoolExecutor: for multiproccessing

And, this achieves the same result with much more cleaner code and ease of use.

## Trying out Multiprocessing and Threading

Threading is especially used when the process is I/O bound and is waiting for the previous process to complete than moving onto next one.  

While, Multiprocess is used for CPU bound process. However, it can also be used for I/O bound.  

---

## Processes

We will be downloading a set of files from the web using the threading.  
While use the multiprocessing to work on them like resizing or changing properties.  

#### url for the files to be downloaded

- https://images.unsplash.com/photo-1621860088759-9027f133fc3d
- https://images.unsplash.com/photo-1621786505687-9a36ca978b27
- https://images.unsplash.com/photo-1621854029362-5d66c3e0c306
- https://images.unsplash.com/photo-1621748339022-9744a069b1c8
- https://images.unsplash.com/photo-1621849400072-f554417f7051
- https://images.unsplash.com/photo-1611095970111-fc87b5315dc3
- https://images.unsplash.com/photo-1621795817359-4d032a4af17a
- https://images.unsplash.com/photo-1621826389794-59a7d9366246
- https://images.unsplash.com/photo-1621832988726-b4738c7ceb76
- https://images.unsplash.com/photo-1621757458931-a1b076e5a8bb


We'll also use the timeit module to gaguge at the time taken to complete this processes and compare it without the use of threading.

## Result

#### Threading
Downloading image without Threading: 50+ sec (approx)
Downloading image with Threading: 25+ sec (approx)

---

#### Multiprocessing
Resizing image to fixed size without mutliprocessing: 3+ sec (approx)
Resizing image to fixed size with mutliprocessing: 1.5+ sec (approx)

# Requirement
> pip install pillow
for image manipulation

Run threading.py first to download the images.