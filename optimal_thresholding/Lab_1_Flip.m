function flip = Lab_1_Flip(x)
i = imread(x);
flip = i(end:-1:1,end:-1:1,:);
imshow(flip);
%flip = flipped_image;

end 