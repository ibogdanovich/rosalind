import biolib


frames = []
with open('dataset.txt') as ds:
    for name, seq in biolib.read_fasta(ds):
        frames += biolib.find_frames(seq)
        frames += biolib.find_frames(biolib.reverse_complement(seq))

    for frame in set(frames):
        print(frame)

