import glob
import imageio

time = 200
frame_duration = 0.1

# Make gif
filenames = sorted(glob.glob('images/image_%s_???.png'
                             % ('snapshot')))[:(time + 1)]

images = []
for filename in filenames:
    images.append(imageio.imread(filename))

imageio.mimsave('gifs/snapshot.gif', images, duration=frame_duration)

print('Saved gif!')
