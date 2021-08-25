function output_opening_closing = opening_closing(image, square_size)
im = imread(image);
im = imbinarize(im);
structuring_element = ones(square_size);
n = square_size - 1;

%First, perform opening Erosion -> Dilation
%Erosion (1)
image_eroded = erosion(image,square_size);
%Dilation (1)

padded_image = padarray(image_eroded,[1 1]);
erosion_dilation = zeros(size(image_eroded), class(image_eroded));

for i=1:size(padded_image,1)-n
    for j=1:size(padded_image,2)-n
        erosion_dilation(i,j) = sum(sum(structuring_element&padded_image(i:i+n,j:j+n)));
    end
end

%Perform closing Dilation -> Erosion
%Dilation (2)
padded_image = padarray(erosion_dilation,[1 1]);
output_opening= zeros(size(erosion_dilation), class(erosion_dilation));

for i=1:size(padded_image,1)-n
    for j=1:size(padded_image,2)-n
        output_opening(i,j) = sum(sum(structuring_element&padded_image(i:i+n,j:j+n)));
    end
end

%Erosion (2)
padded_image = padarray(output_opening,[0 1],1);
output_opening_closing = zeros(size(output_opening), class(output_opening));

for i=1:size(padded_image,1)-n
    for j=1:size(padded_image,2)-n
        x = padded_image(i:i+n,j:j+n);
        x_1 = find(structuring_element==1);
        if(x(x_1)==1)
            output_opening_closing(i,j) = 1;
        end
    end
end

%test using predefind MATLAB functions
%test_opening = imopen(im, ones(square_size,square_size));
%test_opening_closing = imclose(test_opening, ones(square_size,square_size));
subplot(1,2,1);
imshow(im);
title('Original');
subplot(1,2,2);
imshow(output_opening_closing);
title('Opening Closing 7x7');


end