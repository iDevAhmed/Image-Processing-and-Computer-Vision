function median_output = median_filter (im, filter_size)
im = Lab_1_Flip(im);

redChannel = im(:,:,1); 
greenChannel = im(:,:,2); 
blueChannel = im(:,:,3);

imout = zeros(size(redChannel),class(redChannel));
imout2 = zeros(size(greenChannel),class(greenChannel));
imout3 = zeros(size(blueChannel),class(blueChannel));

for m = filter_size : size(im,1)-2
    for n = filter_size : size(im,2)-2
        list = redChannel(m-2:m+2,n-2:n+2);
        imout(m,n) = median(list(:));
    end
end

for m = filter_size : size(im,1)-2
    for n = filter_size : size(im,2)-2
        list = greenChannel(m-2:m+2,n-2:n+2);
        imout2(m,n) = median(list(:));
    end
end

for m = filter_size : size(im,1)-2
    for n = filter_size : size(im,2)-2
        list = blueChannel(m-2:m+2,n-2:n+2);
        imout3(m,n) = median(list(:));
    end
end

median_output = cat(3, imout, imout2, imout3);
imshow(median_output);
end
