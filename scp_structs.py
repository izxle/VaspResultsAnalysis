#!/usr/bin/env python
from argparse import ArgumentParser
from subprocess import run
from itertools import product
from os import path


def get_args(argv=''):
    parser = ArgumentParser()
    # argument definition
    parser.add_argument('fpath')
    parser.add_argument('src', nargs='*', default=['POSCAR', 'CONTCAR'])
    parser.add_argument('-s', '--subdir', nargs='+', default=[''])
    parser.add_argument('--sd', '--subsubdir', dest='subsubdir', nargs='+', default=[''])
    parser.add_argument('-n', '--name', dest='fname', default='POSCAR')
    parser.add_argument('-e', '--ext', nargs='*', default=['.vasp', '_o.vasp'])
    # read arguments
    if argv:
        if isinstance(argv, str):
            argv = argv.split()
        elif not hasattr(argv, '__iter__'):
            raise ValueError(f'argv must be iterable.')
        args = parser.parse_args(argv)
    else:
        args = parser.parse_args()
    # check args
    assert len(args.ext) >= len(args.src), f'ext must have the same length as src'

    return args


def main(argv=''):
    args = get_args(argv=argv)

    for sd, ssd, (src, ext) in product(args.subdir, args.subsubdir, zip(args.src, args.ext)):
        name = args.fname
        if sd:
            name += '_' + sd.strip('/')
        dst_path = f'/Users/izxle/OneDrive/Documents/TAMU/structs/PtCu/111/224/ads/OH/{sd}/{name + ext}'
        src_path = path.join(args.fpath, sd, ssd, src)
        cmd_list = ['sshpass', '-p', '14qr!$QR', 'scp', f'ada:{src_path}', dst_path]
        run(cmd_list)


if __name__ == '__main__':
    main('/scratch/user/izxle/catalysts/PtCu/PtCu/slab/111/ads/OH/0.25 CONTCAR --sd ads_en '
         '-s 1_0  1_2  2_0  2_1  2_5  2_6  3_0  3_1  3_4  3_5 '
         '-e _o.vasp -n PtCu_111_224_OH')
