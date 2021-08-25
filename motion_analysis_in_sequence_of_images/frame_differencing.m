function output = frame_differencing (image, image2, t)
im = imread(image);
im2 = imread(image2);

output = zeros(size(im),class(im));

for i=1:size(im,1)
    for j=1:size(im,2)
        difference = abs(im(i,j) - im2(i,j));
        if difference > t
            output(i,j) = 1;
        else
            output(i,j) = 0;
        end
    end
end
output = imbinarize(output);
imshow(output);

end