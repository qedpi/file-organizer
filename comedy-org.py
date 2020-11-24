import os
from shutil import move, rmtree
from itertools import chain

from genres import genre_of, DOWNLOAD_DIR, DST_DIRS, VIDEO_EXTENSIONS

print(genre_of)

print(f'moving files from {DOWNLOAD_DIR}: \n'
      # f'with keywords: {COMEDY_TAGS} \n'
      # f'with extensions: {VIDEO_EXTENSIONS} \n'
      )

files_moved = 0
for file_name in os.listdir(DOWNLOAD_DIR):
    name_parts = file_name.split('.')
    # check single & double word combos todo: generalize to more than 2
    two_words = ('.'.join(name_parts[i:i + 2]) for i in range(len(name_parts) - 1))
    file_path = os.path.join(DOWNLOAD_DIR, file_name)
    if os.path.isfile(file_path):  # skip files
        continue
    # print(file_name, os.access(file_path, os.W_OK))  # todo: doesn't check if it's locked!
    # move files to corresponding dir
    try:
        # print(f'Try {file_name}')
        # with open(os.path.join(DOWNLOAD_DIR, file_name), 'r') as f:
        if any((keyword := part) in genre_of for part in chain(name_parts, two_words)):
            dst_dir = DST_DIRS[genre_of[keyword]]
            # move video file
            for maybe_vid in (name for name in os.listdir(file_path)):
                if any(maybe_vid.endswith(ext) for ext in VIDEO_EXTENSIONS):
                    move(os.path.join(file_path, maybe_vid), dst_dir)
                    print(f'moved {maybe_vid} to {dst_dir}')
            # delete empty file
            rmtree(file_path)

            files_moved += 1

        # now extract the vid & delete dir
    except PermissionError:
        print('permission denied')
        continue  # skip this file if locked (eg by qTorrent)

print(f'{files_moved = }')