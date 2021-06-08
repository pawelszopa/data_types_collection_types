from collections.abc import Sequence


def use_sequence(sequence: Sequence):
    print(f'the type of this sequence is {type(sequence)}')
    assert (issubclass(type(sequence), Sequence))
    print(f"it's length is {len(sequence)}")
    print(f'repr{repr(sequence)}')
    print(f'all items')
    for sequence_item in sequence:
        print(sequence_item)
    print('_' * 20)
    return


def main():
    r_seq = range(0, 5)
    l_seq = list(r_seq)
    s_seq = ''.join(map(lambda x: str(x), r_seq))
    b_seq = bytes(r_seq)
    ba_seq = bytearray(r_seq)
    mv_seq = memoryview(b_seq)
    all_seq = [r_seq, l_seq, s_seq, b_seq, ba_seq, mv_seq]
    for seq_item in all_seq:
        use_sequence(seq_item)


if __name__ == '__main__':
    main()