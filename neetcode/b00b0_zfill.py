
import os


def zero_fill():
    current_dir = os.getcwd()
    for f in os.listdir(current_dir):
        ori_filepath = os.path.join(current_dir, f)
        # splits = f.split('_')
        # if splits[0] == 'x':
        #     splits[0] = '00b0'
        # else:
        #     splits[0] = splits[0].zfill(4)
        new_f = 'b' + f#'_'.join(splits)
        new_filepath = os.path.join(current_dir, new_f)
        print('Removing...', ori_filepath)
        print('         ->', new_filepath)
        os.rename(ori_filepath, new_filepath)


if __name__ == '__main__':
    zero_fill()

