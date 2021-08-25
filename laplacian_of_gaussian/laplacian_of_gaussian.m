function output = laplacian_of_gaussian(image, std, threshold)
im = imread(image);
filter_size = 3;
[x,y] = meshgrid(-filter_size:filter_size, -filter_size:filter_size);
exp_comp = -(x.^2 + y.^2)/(2 * std * std);
Kernel = exp(exp_comp)/(2 * pi * std * std);

M = size(x,1)-1;
N = size(y,1)-1;
im = double(im);
sxy = zeros(size(im));
im = padarray(im, [filter_size filter_size]);

for i = 1:size(im,1)-M
    for j =1:size(im,2)-N
        Temp = im(i:i+M,j:j+M).*Kernel;
        sxy(i,j)=sum(Temp(:));
    end
end
sxy = uint8(sxy);
figure,imshow(sxy);

end