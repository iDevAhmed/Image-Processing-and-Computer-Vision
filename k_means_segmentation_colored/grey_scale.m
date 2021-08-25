function grey_output = grey_scale(image)
redChannel = image(:,:,1); 
greenChannel = image(:,:,2); 
blueChannel = image(:,:,3);

grey_output = (0.3*redChannel) + (0.59*greenChannel) + (0.11*blueChannel);

end