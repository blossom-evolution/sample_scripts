import os
import errno
import glob
import imageio

time = 300
frame_duration = 0.1

IMAGE_OUTPUT_DIR = 'images'
GIF_OUTPUT_DIR = 'gifs'

try:
    os.makedirs(GIF_OUTPUT_DIR)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

# Make gif
filenames = sorted(glob.glob('%s/image_%s_???.png'
                             % (IMAGE_OUTPUT_DIR, 'snapshot')))[:(time + 1)]

images = []
for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('%s/snapshot.gif' % GIF_OUTPUT_DIR,
                images,
                duration=frame_duration)

print('Saved gif!')
