from main import load_data
import matplotlib.pyplot as plt


def main():
    src_img, dst_img, match_p_src, match_p_dst = load_data()
    # Plot the source and destination images
    plt.figure()
    plt.subplot(1, 2, 1)
    plt.imshow(src_img)
    plt.title('Source Image')
    plt.subplot(1, 2, 2)
    plt.imshow(dst_img)
    plt.title('Destination Image')
    plt.show()


if __name__ == "__main__":
    main()
