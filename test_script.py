from main import load_data
import matplotlib.pyplot as plt


def main():

    # Only perfect matches:
    src_img, dst_img, match_p_src, match_p_dst = load_data()
    plt.figure()
    plt.subplot(2, 2, 1)
    plt.imshow(src_img)
    plt.scatter(match_p_src[0, :], match_p_src[1, :], c='red', s=2)
    plt.title('Source Image - Only Perfect Match')
    plt.subplot(2, 2, 2)
    plt.imshow(dst_img)
    plt.scatter(match_p_dst[0, :], match_p_dst[1, :], c='red', s=2)
    plt.title('Destination Image - Only Perfect Match')

    # With mismatched points:
    src_img, dst_img, match_p_src, match_p_dst = load_data(is_perfect_matches=False)
    plt.subplot(2, 2, 3)
    plt.imshow(src_img)
    plt.scatter(match_p_src[0, :], match_p_src[1, :], c='red', s=2)
    plt.title('Source Image - With Mismatches')
    plt.subplot(2, 2, 4)
    plt.imshow(dst_img)
    plt.scatter(match_p_dst[0, :], match_p_dst[1, :], c='red', s=2)
    plt.title('Destination Image - With Mismatches')
    plt.show()

if __name__ == "__main__":
    main()
