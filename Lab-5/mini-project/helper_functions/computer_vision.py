from PIL import Image
import numpy as np

def person_detected(image1_file, image2_file, t1):
  
  sumDifferences = 0
  # Open the images
  image1 = Image.open(image1_file)
  image2 = Image.open(image2_file)
  
  # Get the image buffer as a numpy array
  buffer1 = np.asarray(image1);
  buffer2 = np.asarray(image2);
  
  # Sum up all the elements of each array (for each pixel, sums the rgb values for brightness, and then adds up the sums of all pixels)
  image1sum = np.sum(buffer1)
  image2sum = np.sum(buffer2)
  
  # Find the difference between the two sums
  sumDifferences = abs(image1sum - image2sum)
    
  if (sumDifferences < t1):
    return False
  return True
