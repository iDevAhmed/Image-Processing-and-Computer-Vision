function output_img = kmeans2(im, k)
%read image
im = imread('Objects.bmp');
%convert image to grey_scale 
image = grey_scale(im);
[idx, c, sumd] = kmeans(image(:), k, 'emptyaction', 'singleton');
final = reshape(idx, size(image));
output_img = mat2gray(final);

imshow(output_img);
%disp("Centroid values");
%disp(c(1));
%disp("sumd values");
%disp(sumd);
end
