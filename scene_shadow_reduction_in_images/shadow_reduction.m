function output = shadow_reduction_3_test(image)
%Read image
img = imread(image);
%Gamma adjustment
J = imadjust(img,[],[],0.5);
%Convert RGB to YCBCR
YCBCRimg = rgb2ycbcr(J);

%Seperate channels
Y = YCBCRimg(:,:,1);
Cb = YCBCRimg(:,:,2);
Cr = YCBCRimg(:,:,3);

R = img(:,:,1);
G = img(:,:,2);
B = img(:,:,3);

%Mask size of image, masked channels are areas where B channel is greater
%than G and B and also threshold applied to Y channel and bright pixels in
%Y channel are omitted.
mask = zeros(size(Y));
mask((B>R & B>G & Y<=150)) = 255;
%Binarize mask to mask out shadow area
mask = imbinarize(mask);
%Get light area
inverse_mask = ~mask;

%Shadow areas masked in all 3 channels
shadow_y = Y .* uint8(mask);
shadow_cb = Cb .* uint8(mask);
shadow_cr = Cr .* uint8(mask);

%Light areas masked in all 3 channels
light_y = Y .* uint8(inverse_mask);
light_cb = Cb .* uint8(inverse_mask);
light_cr = Cr .* uint8(inverse_mask);

%Summation of channel pixels 
sum_shadow_y = sum(shadow_y);
sum_shadow_cb = sum(shadow_cb);
sum_shadow_cr = sum(shadow_cr);
sum_mask = sum(mask);

%Get mean of shadow pixels in YCBCR image over sum of shadow areas
mean_shadow_y =  sum(sum_shadow_y)/ sum(sum_mask);
mean_shadow_cb = sum(sum_shadow_cb)/ sum(sum_mask);
mean_shadow_cr = sum(sum_shadow_cr)/ sum(sum_mask);

%Get mean of light areas like above but instead in light areas
sum_light_y = sum(light_y);
sum_light_cb = sum(light_cb);
sum_light_cr = sum(light_cr);
sum_inverse_mask = sum(inverse_mask);

mean_light_y =  sum(sum_light_y)/ sum(sum_inverse_mask);
mean_light_cb = sum(sum_light_cb)/ sum(sum_inverse_mask);
mean_light_cr = sum(sum_light_cr)/ sum(sum_inverse_mask);

%Calculate difference in Y channel and calculate ratio of light area over
%shadow area in CB and CR channels
difference_y = mean_light_y - mean_shadow_y;
ratio_cb = (mean_light_cb / mean_shadow_cb);
ratio_cr = (mean_light_cr / mean_shadow_cr);

%Calculate new Y channel and CB and CR channels
Y_new = Y + uint8(mask) * difference_y;
CB_new = Cb.* uint8(inverse_mask) + Cb.* uint8(mask) .* ratio_cb;
CR_new = Cr .* uint8(inverse_mask) + Cr .* uint8(mask) .* ratio_cr;

%Merge all 3 images to create new YCBCR image
YCBCRimg = cat(3, Y_new, CB_new, CR_new);

%Convert YCBCBR back to RGB
output = ycbcr2rgb(YCBCRimg);

imshow(output);
title('Uniformly distributed illumination image');
end