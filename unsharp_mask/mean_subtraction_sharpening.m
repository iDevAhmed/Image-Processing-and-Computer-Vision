function sharpened_image = mean_subtraction_sharpening (image, filter_size, weight)
im = imread(image);

redChannel = im(:,:,1); 
greenChannel = im(:,:,2); 
blueChannel = im(:,:,3);

imout = zeros(size(redChannel),class(redChannel));
imout2 = zeros(size(greenChannel),class(greenChannel));
imout3 = zeros(size(blueChannel),class(blueChannel));

for m = filter_size : size(im,1)-2
    for n = filter_size : size(im,2)-2
        list = redChannel(m-2:m+2,n-2:n+2);
        imout(m,n) = mean(list(:));
    end
end

for m = filter_size : size(im,1)-2
    for n = filter_size : size(im,2)-2
        list = greenChannel(m-2:m+2,n-2:n+2);
        imout2(m,n) = mean(list(:));
    end
end

for m = filter_size : size(im,1)-2
    for n = filter_size : size(im,2)-2
        list = blueChannel(m-2:m+2,n-2:n+2);
        imout3(m,n) = mean(list(:));
    end
end

output = cat(3, imout, imout2, imout3);

G = abs(im-output);
multiplication_output = mtimes(G, weight);
sharpened_image = imadd(im,multiplication_output);
imshow(sharpened_image);

end