function grey_output = grey_scale(im, filter_size)

im = median_filter(im, filter_size);
redChannel = im(:,:,1); 
greenChannel = im(:,:,2); 
blueChannel = im(:,:,3);

grey_output = (0.3*redChannel) + (0.59*greenChannel) + (0.11*blueChannel);

imshow(grey_output);
end