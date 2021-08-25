function output_closing = closing(image, square_size)
image_dilated = dilation(image,square_size);

structuring_element = ones(square_size);
output_closing = zeros(size(image_dilated), class(image_dilated));
padded_image = padarray(image_dilated,[0 1],1);

n = square_size - 1;

for i=1:size(padded_image,1)-n
    for j=1:size(padded_image,2)-n
        x = padded_image(i:i+n,j:j+n);
        x_1 = find(structuring_element==1);
        if(x(x_1)==1)
            output_closing(i,j) = 1;
        end
    end
end

imshow(output_closing);

end
