import time
from multiprocessing import Pool, current_process

NUMBERS = [128, 255, 99999, 10651060, 92638090, 215902610]

def factorize(*number):
    result_list = []
    for num in number:
        inner_list = []
        for n in range(1, num + 1):
            if num % n == 0:
                inner_list.append(n)
        result_list.append(inner_list)
    return result_list

# def single_factorize():
#     start = time.time()

#     a, b, c, d, *_ = factorize(*NUMBERS)

#     assert a == [1, 2, 4, 8, 16, 32, 64, 128]
#     assert b == [1, 3, 5, 15, 17, 51, 85, 255]
#     assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
#     assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
    
#     end = time.time()
#     print(f"Sync version {end-start}")

def pool_factorize():
    start = time.time()

    with Pool(processes=2) as pool:
        pool.map(factorize, NUMBERS)
    
    end = time.time()
    print(f"Pool version {end-start}")

if __name__ == "__main__":
    # single_factorize()
    pool_factorize()