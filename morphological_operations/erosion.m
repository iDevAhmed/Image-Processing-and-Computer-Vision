function output_erosion = erosion(image, square_size)
im = imread(image);
im = imbinarize(im);
structuring_element = ones(square_size);
output_erosion = zeros(size(im), class(im));

padded_image = padarray(im,[1 1]);

n = square_size - 1;

for i=1:size(padded_image,1)-n
    for j=1:size(padded_image,2)-n
        x = padded_image(i:i+n,j:j+n);
        x_1 = find(structuring_element==1);
        if(x(x_1) == 1)
            output_erosion(i,j) = 1;
        end
    end
end

%test using predefind MATLAB functions
erosion_1 = imerode(im, ones(square_size, square_size));
subplot(1,2,1);
imshow(erosion_1);
subplot(1,2,2);
imshow(output_erosion);


subtracted_image = abs(im-output_erosion);
imshow(subtracted_image);


end