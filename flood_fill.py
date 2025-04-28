import matplotlib.pyplot as plt

def flood_fill(picture,x,y):
    """hodnoty x u array jsou v tomto pripade hodnoty uvnitr vnoreneho seznamu(, kdy se nejdna o seznamy,
    ovsem o matice a indexy matic - rakdu a sloupcu, ovsem zatim pro zjednoduseni)
       a pozice vnoreneho seznamu v seznamu odpovida hodnote y"""
    if x < 0 or y < 0:
        return picture
    if picture[y[x]] == 0 or picture[y[x]] == 2:
        return
    if picture[y[x]] == 1:
        picture[y[x]] = 2
        flood_fill(picture, x+1, y)
        flood_fill(picture, x-1, y)
        flood_fill(picture, x, y+1)
        flood_fill(picture, x, y-1)


def main():
    img = plt.imread("files/img0.png")[:, :, 0]
    # img = plt.imread("files/img1.png")[:, :, 0]
    # img = plt.imread("files/img2.png")[:, :, 0]

    # img = floodfill(img, 0, 0)
    img = flood_fill(img,0,0)


    plt.imshow(img, cmap="gray")
    plt.show(block=False)
    plt.pause(5)
    plt.clf()


if __name__ == "__main__":
    main()
