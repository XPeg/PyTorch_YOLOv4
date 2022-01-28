import argparse
from typing import Dict, Any


def moded(input, imgsize):
    #split = input.split(',')
    buffer = ['0',
              str((float(split[2]) + 0.5 * float(split[4])) / imgsize[0]),
              str((float(split[3]) + 0.5 * float(split[5])) / imgsize[1]),
              str(float(split[4]) / imgsize[0]),
              str(float(split[5]) / imgsize[1])]
    return ','.join(buffer) + '\n'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='converter.py')
    parser.add_argument('--input', type=str, default='./det.txt')
    parser.add_argument('--output', type=str, default='./out/')
    parser.add_argument('--seqinfo', type=str, default='seqinfo.ini')
    parser.add_argument('--imgw', type=float, default=0)
    parser.add_argument('--imgh', type=float, default=0)
    opt = parser.parse_args()
    print(opt)
    imgsize = []
    if opt.imgw != 0 and opt.imgh != 0:
        imgsize = [opt.imgw, opt.imgh]
    else:
        with open(opt.seqinfo) as f:
            for lines in f.readlines():
                if lines.split('=')[0] == 'imWidth':
                    imgsize[0] = float(lines.split('=')[1])
                if lines.split('=')[0] == 'imHeight':
                    imgsize[1] = float(lines.split('=')[1])

    buffer = {}
    with open(opt.input) as f:
        for line in f.readlines():
            split = line.split(',')
            if split[0] not in buffer:
                buffer[split[0]] = ''
            buffer[split[0]] += (moded(split, imgsize))

    for file in buffer.keys():
        with open(opt.output +"{:0>6d}.txt".format(int(file)), 'w') as f:
            f.write(buffer[file])