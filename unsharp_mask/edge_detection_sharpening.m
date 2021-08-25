function sharpened_image = edge_detection_sharpening (image, weight)
im = imread(image);

redChannel = im(:,:,1); 
greenChannel = im(:,:,2); 
blueChannel = im(:,:,3);

[BW,threshOut,GvR,GhR] = edge(redChannel, 'sobel');
[BW,threshOut,GvG,GhG] = edge(greenChannel, 'sobel');
[BW,threshOut,GvB,GhB] = edge(blueChannel, 'sobel');


edge_magnitude_matrix_R = zeros(size(redChannel));
edge_magnitude_matrix_G = zeros(size(greenChannel));
edge_magnitude_matrix_B = zeros(size(blueChannel));

for m = 1 : size(redChannel,1)
    for n = 1 : size(redChannel,2)
        edge_magnitude_matrix_R(m,n) = sqrt((GvR(m,n)^2) + (GhR(m,n)^2));
    end
end

for m = 1 : size(greenChannel,1)
    for n = 1 : size(greenChannel,2)
        edge_magnitude_matrix_G(m,n) = sqrt((GvG(m,n)^2) + (GhG(m,n)^2));
    end
end

for m = 1 : size(blueChannel,1)
    for n = 1 : size(blueChannel,2)
        edge_magnitude_matrix_B(m,n) = sqrt((GvB(m,n)^2) + (GhB(m,n)^2));
    end
end

redChannel_R = rescale(redChannel);
greenChannel_G = rescale(greenChannel);
blueChannel_B = rescale(blueChannel);

sharpened_image_R = imadd(redChannel_R, immultiply(edge_magnitude_matrix_R,weight));
sharpened_image_G = imadd(greenChannel_G, immultiply(edge_magnitude_matrix_G,weight));
sharpened_image_B = imadd(blueChannel_B, immultiply(edge_magnitude_matrix_B,weight));


pre_sharpened_image = cat(3, sharpened_image_R, sharpened_image_G, sharpened_image_B);
sharpened_image = rescale(pre_sharpened_image);
im_2 = rescale(im);
new_sharpened_image = imadd(double(im_2), double(sharpened_image));
imshow(new_sharpened_image);

%imshow(sharpened_image);

end
