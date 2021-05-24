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


We will be downloading a set of files from the web using the threading while use the multiprocessing to work on them like resizing or changing properties.