import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            stroka = f.readline()
            all_data.append(stroka)
            if not stroka:
                break


if __name__ == '__main__':
    files = [f'./file {number}.txt' for number in range(1, 5)]
    st1 = datetime.now()
    for f in files:
        read = read_info(f)
    print(f'{datetime.now() - st1} (линейный)')


    st2 = datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, files)
    print(f'{datetime.now() - st2} (многопроцессный)')