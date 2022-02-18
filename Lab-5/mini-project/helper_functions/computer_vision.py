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
  
  buffer3 = buffer2 - buffer1
  print(buffer3)
  
  # Find the difference between the two sums
  sumDifferences = np.sum(buffer3)

  if (sumDifferences < t1):
    return False
  return True
