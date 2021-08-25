function [o] = flipImage(I)

[m, n, k] = size(I);
o = zeros(m, n, k);
for i = 1:m-1
    for j = 1:n-1
        for z = 1:k
            o(i, j, z) = I(m-i, n-j, z);
        end
    end
end

o = uint8(o);
%imshow(o);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

M = 7;
N = 7;

modifyO = padarray(o,[floor(M/2), floor(N/2)]);
BR = zeros([size(o,1) size(o,2)]);
BG = zeros([size(o,1) size(o,2)]);
BB = zeros([size(o,1) size(o,2)]);

%med_indx = round((M*N)/2);
for i = 1:size(modifyO, 1) - (M-1)
    for j = 1:size(modifyO, 2) - (N-1)
        temp = modifyO(i:i+(M-1),j:j+(N-1),:);
        
        redC = temp(:, :, 1);
        greenC = temp(:, :, 2);
        blueC = temp(:, :, 3);
        for k = 1:3
            BR(i, j, k) = median(redC(:));
            BG(i, j, k) = median(greenC(:));
            BB(i, j, k) = median(blueC(:));
        end
    end
end

BR = uint8(BR);
BG = uint8(BG);
BB = uint8(BB);
%imshow(BR);
%imshow(BG);
%imshow(BB);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

BR2 = BR(:, :, 1);
BG2 = BR(:, :, 2);
BB2 = BR(:, :, 3);

BR3 = BG(:, :, 1);
BG3 = BG(:, :, 2);
BB3 = BG(:, :, 3);

BR4 = BB(:, :, 1);
BG4 = BB(:, :, 2);
BB4 = BB(:, :, 3);

%gray1 = 0.3*BR2 + 0.59*BG2 + 0.11*BB2
%gray2 = 0.3*BR3 + 0.59*BG3 + 0.11*BB3
%gray3 = 0.3*BR4 + 0.59*BG4 + 0.11*BB4
gray = 0.3*BR + 0.59*BG + 0.11*BB

%imshow(gray1)
%imshow(gray2)
%imshow(gray3)
imshow(gray)


end

