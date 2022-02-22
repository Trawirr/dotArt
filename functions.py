import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import stats

import time

# converting binary number given as string to decimal number
def bin2dec(binary):
    val = 0
    for b in binary:
        val *= 2
        if b == "1":
            val += 1
    return val

# dict converting decimal value to binary-interpreted dots
def dots(x):
    return {
        # 0: "⠀",
        0: "⠄",
        1: "⠁",
        2: "⠂",
        3: "⠃",
        4: "⠄",
        5: "⠅",
        6: "⠆",
        7: "⠇",
        8: "⠈",
        9: "⠉",
        10: "⠊",
        11: "⠋",
        12: "⠌",
        13: "⠍",
        14: "⠎",
        15: "⠏",
        16: "⠐",
        17: "⠑",
        18: "⠒",
        19: "⠓",
        20: "⠔",
        21: "⠕",
        22: "⠖",
        23: "⠗",
        24: "⠘",
        25: "⠙",
        26: "⠚",
        27: "⠛",
        28: "⠜",
        29: "⠝",
        30: "⠞",
        31: "⠟",
        32: "⠠",
        33: "⠡",
        34: "⠢",
        35: "⠣",
        36: "⠤",
        37: "⠥",
        38: "⠦",
        39: "⠧",
        40: "⠨",
        41: "⠩",
        42: "⠪",
        43: "⠫",
        44: "⠬",
        45: "⠭",
        46: "⠮",
        47: "⠯",
        48: "⠰",
        49: "⠱",
        50: "⠲",
        51: "⠳",
        52: "⠴",
        53: "⠵",
        54: "⠶",
        55: "⠷",
        56: "⠸",
        57: "⠹",
        58: "⠺",
        59: "⠻",
        60: "⠼",
        61: "⠽",
        62: "⠾",
        63: "⠿",
        64: "⡀",
        65: "⡁",
        66: "⡂",
        67: "⡃",
        68: "⡄",
        69: "⡅",
        70: "⡆",
        71: "⡇",
        72: "⡈",
        73: "⡉",
        74: "⡊",
        75: "⡋",
        76: "⡌",
        77: "⡍",
        78: "⡎",
        79: "⡏",
        80: "⡐",
        81: "⡑",
        82: "⡒",
        83: "⡓",
        84: "⡔",
        85: "⡕",
        86: "⡖",
        87: "⡗",
        88: "⡘",
        89: "⡙",
        90: "⡚",
        91: "⡛",
        92: "⡜",
        93: "⡝",
        94: "⡞",
        95: "⡟",
        96: "⡠",
        97: "⡡",
        98: "⡢",
        99: "⡣",
        100: "⡤",
        101: "⡥",
        102: "⡦",
        103: "⡧",
        104: "⡨",
        105: "⡩",
        106: "⡪",
        107: "⡫",
        108: "⡬",
        109: "⡭",
        110: "⡮",
        111: "⡯",
        112: "⡰",
        113: "⡱",
        114: "⡲",
        115: "⡳",
        116: "⡴",
        117: "⡵",
        118: "⡶",
        119: "⡷",
        120: "⡸",
        121: "⡹",
        122: "⡺",
        123: "⡻",
        124: "⡼",
        125: "⡽",
        126: "⡾",
        127: "⡿",
        128: "⢀",
        129: "⢁",
        130: "⢂",
        131: "⢃",
        132: "⢄",
        133: "⢅",
        134: "⢆",
        135: "⢇",
        136: "⢈",
        137: "⢉",
        138: "⢊",
        139: "⢋",
        140: "⢌",
        141: "⢍",
        142: "⢎",
        143: "⢏",
        144: "⢐",
        145: "⢑",
        146: "⢒",
        147: "⢓",
        148: "⢔",
        149: "⢕",
        150: "⢖",
        151: "⢗",
        152: "⢘",
        153: "⢙",
        154: "⢚",
        155: "⢛",
        156: "⢜",
        157: "⢝",
        158: "⢞",
        159: "⢟",
        160: "⢠",
        161: "⢡",
        162: "⢢",
        163: "⢣",
        164: "⢤",
        165: "⢥",
        166: "⢦",
        167: "⢧",
        168: "⢨",
        169: "⢩",
        170: "⢪",
        171: "⢫",
        172: "⢬",
        173: "⢭",
        174: "⢮",
        175: "⢯",
        176: "⢰",
        177: "⢱",
        178: "⢲",
        179: "⢳",
        180: "⢴",
        181: "⢵",
        182: "⢶",
        183: "⢷",
        184: "⢸",
        185: "⢹",
        186: "⢺",
        187: "⢻",
        188: "⢼",
        189: "⢽",
        190: "⢾",
        191: "⢿",
        192: "⣀",
        193: "⣁",
        194: "⣂",
        195: "⣃",
        196: "⣄",
        197: "⣅",
        198: "⣆",
        199: "⣇",
        200: "⣈",
        201: "⣉",
        202: "⣊",
        203: "⣋",
        204: "⣌",
        205: "⣍",
        206: "⣎",
        207: "⣏",
        208: "⣐",
        209: "⣑",
        210: "⣒",
        211: "⣓",
        212: "⣔",
        213: "⣕",
        214: "⣖",
        215: "⣗",
        216: "⣘",
        217: "⣙",
        218: "⣚",
        219: "⣛",
        220: "⣜",
        221: "⣝",
        222: "⣞",
        223: "⣟",
        224: "⣠",
        225: "⣡",
        226: "⣢",
        227: "⣣",
        228: "⣤",
        229: "⣥",
        230: "⣦",
        231: "⣧",
        232: "⣨",
        233: "⣩",
        234: "⣪",
        235: "⣫",
        236: "⣬",
        237: "⣭",
        238: "⣮",
        239: "⣯",
        240: "⣰",
        241: "⣱",
        242: "⣲",
        243: "⣳",
        244: "⣴",
        245: "⣵",
        246: "⣶",
        247: "⣷",
        248: "⣸",
        249: "⣹",
        250: "⣺",
        251: "⣻",
        252: "⣼",
        253: "⣽",
        254: "⣾",
        255: "⣿"
    }[x]


def black_white(img, mode='avg', custom_color=127):
    gray = is_gray(img)
    if mode == "avg":
        main_color = average_color(img)
    elif mode == "med":
        main_color = median_color(img)
    elif mode == "custom":
        main_color = custom_color
    else:
        return img

    print(f"Mode: {mode}, main_color: {main_color}")
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if gray:
                img[y,x] = 0 if img[y,x] < main_color else 255
            else:
                img[y,x] = [0, 0, 0] if sum(img[y,x])/3 < main_color else [255,255,255]
    return img

# converting gray image to black-white based on mean color of image without background
def gray_to_blackwhite(img):
    img_1d = img.flatten()
    mode_color = stats.mode(img_1d)[0][0]
    no_background = [p for p in img_1d if p != mode_color]
    # mean color of image without background
    color = sum(no_background)/len(no_background)
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            img[y, x] = 0 if img[y, x] < color else 255
    return img

# ZOPTYMALIZOWAC
def black_white_filter(img, mode, size, custom_color=0):
    gray = is_gray(img)
    img_tmp = img.copy()
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            img_sq = img[max(y - size, 0):min(y + size, img.shape[0]), max(x - size, 0):min(x + size, img.shape[1])]
            if mode == "avg":
                main_color = average_color(img_sq)
            elif mode == "med":
                main_color = median_color(img_sq)
            elif mode == "custom":
                main_color = custom_color
            if gray:
                img_tmp[y,x] = 0 if img[y,x] < main_color else 255
            else:
                img_tmp[y,x] = [0, 0, 0] if sum(img[y,x])/3 < main_color else [255,255,255]
    return img_tmp


def more_contrast_by_median(img, mode, size, color_val=30):
    gray = is_gray(img)
    img2 = img.copy()
    # ZROBIC STOSUNKOWE ZMIANY JAK WCZESNIEJ abs(color - avgcolor) czy cos
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            avg_color = median_color(img[max(y-size, 0):min(y+size, img.shape[0]), max(x-size, 0):min(x+size, img.shape[1])])
            if gray:
                color = img[y,x]
            else:
                color = sum(img[y,x])/len(img[y,x])
            if mode == "rel":
                d = abs(avg_color-color)
                color_diff_val = (255-d)/(255-20)*color_val if d<20 else 0
            elif mode == "abs":
                color_diff_val = color_val
            if color < avg_color:
                if gray:
                    img2[y,x] = max(img2[y, x] - color_diff_val, 0)
                else:
                    img2[y, x] = [max(c - color_diff_val, 0) for c in img[y, x]]
            else:
                if gray:
                    img2[y,x] = min(img2[y, x] + color_diff_val, 255)
                else:
                    img2[y, x] = [min(c + color_diff_val+50, 255) for c in img[y, x]]
    return img2


def more_contrast_by_mean(img, mode, size, color_val=30):
    gray = is_gray(img)
    img2 = img.copy()
    # ZROBIC STOSUNKOWE ZMIANY JAK WCZESNIEJ abs(color - avgcolor) czy cos
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            avg_color = average_color(img[max(y-size, 0):min(y+size, img.shape[0]), max(x-size, 0):min(x+size, img.shape[1])])
            if gray:
                color = img[y,x]
            else:
                color = sum(img[y,x])/len(img[y,x])
            if mode == "rel":
                d = abs(avg_color-color)
                color_diff_val = (255-d)/(255-20)*color_val if d<20 else 0
            elif mode == "abs":
                color_diff_val = color_val
            if color < avg_color:
                if gray:
                    img2[y,x] = max(img2[y, x] - color_diff_val, 0)
                else:
                    img2[y, x] = [max(c - color_diff_val, 0) for c in img[y, x]]
            else:
                if gray:
                    img2[y,x] = min(img2[y, x] + color_diff_val, 255)
                else:
                    img2[y, x] = [min(c + color_diff_val+50, 255) for c in img[y, x]]
    return img2


def median_filter(img, size):
    #print(img.shape)
    gray = is_gray(img)
    size2 = (size-1)//2
    img2 = img.copy()
    for x in range(size2, img.shape[1]-size2):
        for y in range(size2, img.shape[0]-size2):
            colors = []
            for xx in range(-size2, size2+1):
                for yy in range(-size2, size2+1):
                    #print(y+yy, x+xx)
                    colors.append(img[y+yy, x+xx])
            if gray:
                img2[y, x] = np.median(colors)
            else:
                img2[y, x] = np.median(colors, axis=0)
    img2 = img2[size2:img.shape[0]-size2, size2:img.shape[1]-size2]
    return img2

def mean_filter(img, size):
    gray = is_gray(img)
    size2 = (size-1)//2
    img2 = img.copy()
    for x in range(size2, img.shape[1]-size2):
        for y in range(size2, img.shape[0]-size2):
            colors = []
            for xx in range(-size2, size2+1):
                for yy in range(-size2, size2+1):
                    colors.append(img[y+yy, x+xx])
            if gray:
                img2[y, x] = np.mean(colors)
            else:
                img2[y, x] = np.mean(colors, axis=0)
    img2 = img2[size2:img.shape[0]-size2, size2:img.shape[1]-size2]
    return img2

def is_gray(img):
    if len(img.shape) < 3:
        return True
    else:
        return False

def average_color(img):
    gray = is_gray(img)
    rgb = 0
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if gray:
                rgb += img[y, x]
            else:
                rgb += sum(img[y, x])/3
    return rgb/(img.shape[0]*img.shape[1])

def median_color(img):
    gray = is_gray(img)
    rgb = []
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            if gray:
                rgb.append(img[y, x])
            else:
                rgb.append(sum(img[y, x]) / 3)
    if gray:
        return np.median(rgb)
    else:
        return np.median(rgb, axis=0)

def fix_colors(img, treshold = 50):
    for x in range(1, img.shape[1]-1):
        for y in range(1, img.shape[0]-1):
            img2 = img[y-1:y+2, x-1:x+2]
            #print(abs((sum(img2.flatten())-img[y,x])/8 - img[y,x]))
            if abs((sum(img2.flatten())-img[y,x])/8 - img[y,x]) > treshold:
                img[y, x] = stats.mode(img2.flatten())[0][0]
    return img


def resize_to(img, xy):
    width, height = 0, 0
    w, h = img.shape[1], img.shape[0]
    pix_size = 0
    while width+xy[0] < w and height+xy[1] < h:
        width += xy[0]
        height += xy[1]
        pix_size += 1
    print(w, " x ", h)
    print(width, " x ", height, " - ", pix_size)
    X = [w//2 - width//2, w//2 + width//2]
    Y = [h//2 - height//2, h//2+height//2]

    # plt.imshow(img)
    # plt.title("1")
    # plt.show()

    img = img[h//2 - height//2:h//2+height//2,
              w//2 - width//2:w//2 + width//2]
    # plt.imshow(img)
    # plt.title("2")
    # plt.show()

    img = cv2.resize(img, (xy[0], xy[1]))
    # plt.imshow(img)
    # plt.title("3")
    # plt.show()
    return img

def is_inside(img, x, y):
    if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
        return True
    else:
        return False

def draw_border(img, X, Y, thickness = 1):
    gray = is_gray(img)
    img_border = img.copy()
    X = [[X[0] - thickness, X[0]], [X[1], X[1] + thickness]]
    Y = [[Y[0] - thickness, Y[0]], [Y[1], Y[1] + thickness]]
    print(X, '\n', Y)
    for xx in X:
        for x in range(xx[0], xx[1]+1):
            for y in range(Y[0][1], Y[1][0]+1):
                if is_inside(img, x, y):
                    if gray:
                        img_border[y, x] = 255
                    else:
                        img_border[y, x] = [255, 0, 0]

    for yy in Y:
        for y in range(yy[0], yy[1]+1):
            for x in range(X[0][1], X[1][0]+1):
                if is_inside(img, x, y):
                    if gray:
                        img_border[y, x] = 255
                    else:
                        img_border[y, x] = [255, 0, 0]
    return img_border

def get_corners(img, xdim, ydim, pixel_block_size, xchar = 2, ychar = 4):
    w, h = img.shape[1], img.shape[0]
    x_len = xdim*pixel_block_size*xchar
    y_len = ydim*pixel_block_size*ychar
    X = [w // 2 - x_len// 2, w // 2 + x_len // 2]
    Y = [h // 2 - y_len // 2, h // 2 + y_len // 2]
    print(f"xlen {x_len}, ylen {y_len}\n"
          f"X {X[1] - X[0]}, Y {Y[1] - Y[0]}")
    return X, Y

def convert_to_dots(img, sizes, treshold, mode = "mediana", tracking = True):
    file = open("result.txt", "w", encoding="utf-8")
    block_size_x, block_size_y = sizes[0], sizes[1]
    gray = is_gray(img)
    if tracking:
        img3 = img.copy()
    for y in range(14):
        for x in range(29):
            bin = ""
            for xx in range(block_size_x):
                for yy in range(block_size_y):
                    if gray:
                        rgb = img[(y * block_size_y + yy), (x * block_size_x + xx)]
                    else:
                        rgb = sum(img[(y * block_size_y + yy), (x * block_size_x + xx)])/3
                    if rgb < treshold:
                        bin = "0" + bin
                        if gray:
                            done_color = 50
                        else:
                            done_color = [50, 50, 50]
                    else:
                        bin = "1" + bin
                        if gray:
                            done_color = 200
                        else:
                            done_color = [200, 200, 200]
                    if tracking:
                        img3[(y * block_size_y + yy), (x * block_size_x + xx)] = done_color
            if tracking:
                plt.imshow(img3)
                plt.draw()
                plt.pause(0.002)
                plt.clf()
            file.write(dots(bin2dec(bin)))
            print(dots(bin2dec(bin)), end='')

        file.write("\n")
        print()
    file.close()

def dots_image(img):
    width, height = 29*2, 14*3
    w, h = img.shape[1], img.shape[0]
    pix_size = 1
    print(w, " x ", h)

    while width+58 < w and height+84 < h:
        width += 29*2
        height += 14*3
        pix_size += 1
    print(width, " x ", height, " - ", pix_size)

    X = [w//2 - width//2, w//2 + width//2]
    Y = [h//2 - height//2, h//2+height//2]

    img2 = img[h//2 - height//2:h//2+height//2,
              w//2 - width//2:w//2 + width//2]
    plt.imshow(img2)
    plt.show()

    # img_border = img.copy()
    # for x in X:
    #     for y in range(Y[0], Y[1]+1):
    #         img_border[y, x] = [255, 0, 0]
    # for y in Y:
    #     for x in range(X[0], X[1]+1):
    #         img_border[y, x] = [255, 0, 0]
    #
    # plt.imshow(img_border)
    # plt.show()

    lu = [w//2 - width//2, h//2 - height//2]
    img3 = img.copy()
    for y in range(14):
        #Sprint(f"{y} ",end='')
        for x in range(29):
            bin = ""
            for xx in range(2):
                for yy in range(3):
                    #print(img[(x*2 + xx)*pix_size, (y*2 + yy)*pix_size], "\n")
                    rgb = 0
                    for px in range(pix_size):
                        for py in range(pix_size):
                            #print(lu[0] + (x * 2 + xx) * pix_size + px, lu[1] + (y * 6 + yy) * pix_size + py)
                            rgb += sum(img[lu[1] + (y * 3 + yy) * pix_size + py, lu[0] + (x * 2 + xx) * pix_size + px])/3
                            #print(img[lu[1] + (y * 6 + yy) * pix_size + py, lu[0] + (x * 2 + xx) * pix_size + px])
                            #print(rgb)
                            img[lu[1] + (y * 3 + yy) * pix_size + py, lu[0] + (x * 2 + xx) * pix_size + px] = [20, 200, 20]
                    rgb /= pix_size**2
                    if rgb < 170:
                        bin = "1" + bin
                        tmp = 1
                    else:
                        bin = "0" + bin
                        tmp = 0
                    for px in range(pix_size):
                        for py in range(pix_size):
                            if tmp == 1:
                                img3[lu[1] + (y * 3 + yy) * pix_size + py, lu[0] + (x * 2 + xx) * pix_size + px] = [50, 50,
                                                                                                                    50]
                            else:
                                img3[lu[1] + (y * 3 + yy) * pix_size + py, lu[0] + (x * 2 + xx) * pix_size + px] = [200,
                                                                                                                    200, 200]
            plt.imshow(img3)
            plt.draw()
            plt.pause(0.002)
            plt.clf()
            print(dots(bin2dec(bin)), end='')
        print()


    plt.imshow(img3)
    plt.show()

def get_background_color(img):
    pass

# Converting gray image to dot image
def dots_gray(img, img_name, dots_size=[2,4], dims=-1, treshold=-1, tracking = False):
    if not is_gray(img):
        print("Error - image is not gray!")
        return None
    file = open(f"results\\{img_name}.txt", "w", encoding="utf-8")
    x_char = dots_size[0]
    y_char = dots_size[1]
    if dims == -1:
        x_dim, y_dim, pixel_block_size = get_auto_dims(img, x_char=x_char, y_char=y_char)
    else:
        x_dim, y_dim = dims
        pixel_block_size = get_dims(img, x_dim, y_dim, x_char, y_char)

    if treshold == -1:
        treshold = average_color(img)
        print("mean = ", treshold)

    x_corners, y_corners = get_corners(img, x_dim, y_dim, pixel_block_size)

    if tracking:
        img_tracking = draw_border(img.copy(), x_corners, y_corners)

    print(f"Image to dots converting started:\n"
          f"Image name: {img_name}"
          f"Original image size: {img.shape[1]} x {img.shape[0]}\n"
          f"Converting part size: {x_dim} x {y_dim}, pixel block size {pixel_block_size}\n"
          f"Start coords: {x_corners[0]}, {y_corners}")

    for y in range(y_dim):
        for x in range(x_dim):
            bin_val = ""
            for xx in range(x_char):
                for yy in range(y_char):
                    pos_y = y_corners[0] + y * y_char * pixel_block_size + yy * pixel_block_size
                    pos_x = x_corners[0] + x * x_char * pixel_block_size + xx * pixel_block_size
                    pixel_block_color = median_color(img[pos_y:pos_y + pixel_block_size,
                                                         pos_x:pos_x + pixel_block_size])
                    if pixel_block_color < treshold:
                        bin_val = "0" + bin_val
                        color_tracking = 50
                    else:
                        bin_val = "1" + bin_val
                        color_tracking = 200
                    if tracking:
                        img_tracking[pos_y:pos_y + pixel_block_size,
                                     pos_x:pos_x + pixel_block_size] = color_tracking
                        cv2.imshow("Tracking", img_tracking)

            if tracking:
                cv2.imshow("Tracking", img_tracking)
                cv2.waitKey(1)
            file.write(dots(bin2dec(bin_val)))
            print(dots(bin2dec(bin_val)), end='')

        file.write("\n")
        if tracking:
            print()
    if tracking:
        show_image(img_tracking)
    file.close()

def get_dims(img, xdim, ydim, x_char = 2, y_char = 4):
    y = img.shape[0]
    x = img.shape[1]
    i = 1
    while xdim * x_char * i < x and ydim * y_char * i < y:
        i += 1
    return i-1

def get_auto_dims(img, xmax = 30, ymax = 20, x_char = 2, y_char = 4):
    #print(f"Image size: {img.shape[1]}, {img.shape[0]}")
    y = img.shape[0] // y_char
    x = img.shape[1] // x_char
    i = 1
    while True:
        x_dim = x//i
        y_dim = y//i
        #print(f"{i}. {x_dim}, {y_dim}")
        if x_dim <= xmax and y_dim <= ymax:
            pixel_block_size = i
            break
        i += 1
    return x_dim, y_dim, pixel_block_size

def get_divisors(x):
    divisors = []
    for i in range(1, (x+1)//2+1):
        if x % i == 0:
            divisors.append(i)
    divisors.append(x)
    return np.array(divisors)

def gray_histogram(img):
    n = 21
    if not is_gray(img):
        print("gray_histogram error - image is not gray")
    tresholds = np.linspace(0,255,n)
    values = np.zeros(n-1)
    vals = []
    for x in range(img.shape[1]):
        for y in range(img.shape[0]):
            vals.append(img[y,x])
            for i in range(1,n):
                if img[y,x] < tresholds[i]:
                    values[i-1] += 1
                    break
    print(f"{sum(values)} / {img.shape[0]*img.shape[1]}")
    print(f"values = {values}")
    plt.hist(vals, bins = tresholds)
    plt.show()

def show_image(img, mode = "plt", title = "My image"):
    if mode == "plt":
        plt.imshow(img, cmap='gray', vmin=0, vmax=255)
        plt.title(title)
        plt.show()
    elif mode == "cv":
        cv2.imshow(title, img)
        cv2.waitKey()
    else:
        print("show_image error - wrong mode!")