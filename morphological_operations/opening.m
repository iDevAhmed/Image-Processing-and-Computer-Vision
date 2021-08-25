function output_opening = opening(image, square_size)
image_eroded = erosion(image,square_size);

structuring_element = ones(square_size);

padded_image = padarray(image_eroded,[1 1]);
output_opening = zeros(size(image_eroded), class(image_eroded));

n = square_size - 1;

for i=1:size(padded_image,1)-n
    for j=1:size(padded_image,2)-n
        output_opening(i,j) = sum(sum(structuring_element&padded_image(i:i+n,j:j+n)));
    end
end

imshow(output_opening);
end