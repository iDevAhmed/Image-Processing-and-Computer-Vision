function output_dilation = dilation (image, square_size)
im = imread(image);
im = imbinarize(im);
structuring_element = ones(square_size);

padded_image = padarray(im,[1 1]);
output_dilation = zeros(size(im), class(im));

n = square_size - 1;

for i=1:size(padded_image,1)-n
    for j=1:size(padded_image,2)-n
        output_dilation(i,j) = sum(sum(structuring_element&padded_image(i:i+n,j:j+n)));
    end
end

%test using predefind MATLAB functions
dilate_1 = imdilate(im, ones(square_size,square_size));
subplot(1,2,1);
imshow(dilate_1);
subplot(1,2,2);
imshow(output_dilation);


end


    