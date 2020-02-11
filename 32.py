# 32. Utwórz funckję, która na zadanej macierzy zapisze wzór ustalonych struktur (blok, ul, bochenek, łódka, światła uliczne, żaba, latarnia)

import matplotlib.pyplot as plt
import numpy as np



def randomGrid(N):
    return np.random.choice([0,255], N*N, p=[1,  0]).reshape(N,N)

def blok(i,j,grid):
    blok = np.array([[0, 0, 0],
                       [0,255,255],
                       [0,255,255]])
    grid[i:i+3, j:j+3] = blok

def ul(i, j, grid):
    ul = np.array([[0, 0, 0, 0],
                    [0, 255, 255, 0],
                    [255, 0, 0, 255], 
                    [0, 255, 255, 0]])
    grid[i:i + 4, j:j + 4] = ul

def bochenek(i, j, grid):
    bochenek = np.array([[0, 255, 255, 0],
                    [255, 0, 0, 255],
                    [0, 255, 0, 255], 
                    [0, 0, 255, 0]])
    grid[i:i + 4, j:j + 4] = bochenek
    
def lodka(i, j, grid):
    lodka = np.array([[255, 255, 0],
                       [255,0,255],
                       [0,255,0]])
    grid[i:i + 3, j:j + 3] = lodka
    
def swiatla_uliczne(i, j, grid):
    swiatla_uliczne = np.array([[0, 255, 0],
                       [0,255,0],
                       [0,255,0]])
    grid[i:i + 3, j:j + 3] = swiatla_uliczne
    
def zaba(i, j, grid):
    zaba = np.array([[0, 0, 0, 0],
                    [0, 255, 255, 255],
                    [255, 255, 255, 0], 
                    [0, 0, 0, 0]])
    grid[i:i + 4, j:j + 4] = zaba    
    
def latarnia(i, j, grid):
    zaba = np.array([[255, 255, 0, 0],
                    [255, 0, 0, 0],
                    [0, 0, 0, 255], 
                    [0, 0, 255, 255]])
    grid[i:i + 4, j:j + 4] = zaba  

def main():
    obraz = randomGrid(15)
    
    blok(0,0,obraz)
    ul(4,6,obraz)
    bochenek(0,6,obraz)
    lodka (0,12, obraz)
    swiatla_uliczne(4, 12, obraz)
    zaba(4, 0, obraz)
    latarnia (10, 0, obraz)
    plt.imshow(obraz, interpolation='nearest', cmap = "Greys")
    plt.show()

if __name__=="__main__":
    main()